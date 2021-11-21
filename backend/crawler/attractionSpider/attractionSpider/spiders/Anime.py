import scrapy
from scrapy.linkextractors import LinkExtractor
import pandas as pd
from .wiki import WikiSpider

# para rodar o crawler use o comando scrapy crawl
# os argumentos devem ser nome da spider e um -a an, que sera o nome do anime
# exemplo para pegar Attack on titan:
# scrapy crawl Anime -a an='Attack on titan'


class AnimeSpider(scrapy.Spider):
    def __init__(self, an=None, md=1, *args, **kwargs):
        super(AnimeSpider, self).__init__(*args, **kwargs)
        self.animeName = an.split()
        self.maxDep = md
    name = 'Anime'

    def start_requests(self):
        url = 'https://www.google.com/search?q='
        url += ''.join([i+'+' for i in self.animeName])
        url1 = url+'wiki'
        url2 = url+'myanimelist'
        #print(url1,url2)
        #yield scrapy.Request(url=url1, callback=self.getLink,meta={'domain':'wikipedia.org','name':'wikipedia'})
        yield scrapy.Request(url=url2, callback=self.getLink,meta={'domain':'myanimelist.net','name':'myanimelist'})


    def getLink(self, response):
        xlink = LinkExtractor()
        links = []
        for l in xlink.extract_links(response):
            if response.meta['domain'] in l.url:
                links.append(l.url)
        print(links)
        if len(links) > self.maxDep:
            lim = self.maxDep
        else:
            lim = len(links)
        print(lim)
        for i in range(lim):
            url = links[i]
            if url is not None:
                #print(f'resquest - link:{i}')
                if response.meta['name'] == 'myanimelist':
                    yield scrapy.Request(url=url, callback=self.parse_mal)
                elif response.meta['name'] == 'wikipedia':
                    print('---------------------mandou request para o WIKI:------------------\n')
                    print(url)
                    yield scrapy.Request(url=url, callback=self.parse_wiki)

    
    def parse(self, response):
        xlink = LinkExtractor()
        wikiLinks = []
        malLinks = []
        for link in xlink.extract_links(response):
            if 'wikipedia' in link.text.lower():
                #print(link)
                wikiLinks.append(link.url)
            elif 'myanimelist' in link.text.lower():
                malLinks.append(link.url)
        print(malLinks)
        if len(wikiLinks) > self.maxDep:
            lim = self.maxDep
        else:
            lim = len(wikiLinks)
        print(lim)
        for i in range(lim):
            if wikiLinks[i] is not None:
                #print(f'resquest - link:{i}')
                print('entrouuuuuuuuuuu---------------------------------')
                yield scrapy.Request(url=wikiLinks[i], callback=self.parse_wiki)

    def parse_wiki(self, response):
        name = response.css('#firstHeading i::text').get()
        description = ''.join([k for k in response.css('.infobox_v2+ p').css('::text').extract()])
        #genres = [k for k in response.css('.ambox-content+ .infobox_v2 td+ td').css('::text').extract() if len(k) > 1]# ------ nao funciona
        anime = {'name':name, 'description':description}
        yield {'name':name, 'description':description}
    
    def parse_mal(self, response):

        jp_name = response.css('.h1_bold_none strong::text').get()
        en_name = response.css('.title-inherit::text').get()
        en_synopsis = ''
        temp = response.css('.pb16~ p::text').extract()
        temp = temp[:-1]
        for i in range(len(temp)):
            for j in ['\n', '\r']:
                temp[i] = temp[i].replace(j, '')
        en_synopsis = en_synopsis.join(temp)
        del temp

        tt = [i.strip() for i in response.css('#content > table .borderClass div').css('::text').extract()]
        tt = [i for i in tt if len(i)> 0]
        tt = tt[tt.index('Type:'):tt.index('Rating:')+10]
        comp = []
        for i in tt:
            if i not in comp:
                comp.append(i)
        comp = comp[:comp.index('Statistics')]
        comp = [i for i in comp if len(i)>1]
        try:
            comp.pop(comp.index('Broadcast:')+1)
            comp.pop(comp.index('Broadcast:'))
        except:
            pass
        indexers = [i for i in comp if ':' in i]
        dic = {'jp_name':jp_name, 'en_name':en_name, 'en_synopsis':en_synopsis}
        for i in indexers:
            dic[i] = None
        for i in range(len(indexers)):
            ac = i
            nac = i+1
            if nac >= len(indexers):
                dic[indexers[i]] = comp[comp.index(indexers[ac])+1:]
                break        
            dic[indexers[i]] = comp[comp.index(indexers[ac])+1:comp.index(indexers[nac])]

        for i in dic:
            try:
                if len(dic[i])<=1:
                    dic[i] = dic[i][0]
            except:
                print(dic[i])
        
        
        # try:
        #     num_ep = int(response.css('.spaceit_pad:nth-child(16)::text').extract()[1].replace('\n',''))
        # except:
        #     num_ep = None
        # studios = [i for i in [i.replace('\n','').strip() for i in response.css('.spaceit_pad:nth-child(23)').css('::text').extract()]if i != 'Studios:' and len(i) >=1]
        # try:
        #     source = response.css('.spaceit_pad:nth-child(24)::text').extract()[1].replace('\n','').strip()
        # except:
        #     source = None
        # genres = list(set([i for i in [i.replace('\n','').strip() for i in response.css('.spaceit_pad:nth-child(25)').css('::text').extract()] if len(i)>=2 and i != 'Genres:']))
        # try:
        #     rating = response.css('.spaceit_pad:nth-child(29)::text').extract()[1].replace('\n','').strip()
        # except:
        #     rating = None

        yield dic
        

        
            
        
