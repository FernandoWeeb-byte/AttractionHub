import scrapy
from scrapy.linkextractors import LinkExtractor


# para rodar o crawler use o comando scrapy crawl
# os argumentos devem ser nome da spider e um -a an, que sera o nome do anime
# exemplo para pegar Attack on titan:
# scrapy crawl Anime -a an='Attack on titan'


class AnimeSpider(scrapy.Spider):
    def __init__(self, an=None, md=1, *args, **kwargs):
        super(AnimeSpider, self).__init__(*args, **kwargs)
        self.animeName = an.split()
        self.maxDep = int(md)
    name = 'anime'

    def start_requests(self):
        url = 'https://www.google.com/search?q='
        url += ''.join([i+'+' for i in self.animeName])
        url1 = url+'wiki'
        url2 = url+'myanimelist'
        url3 = url+'justwatch'
        yield scrapy.Request(url=url1, callback=self.getLink,meta={'domain':'wikipedia.org','name':'wikipedia'})
        yield scrapy.Request(url=url2, callback=self.getLink,meta={'domain':'myanimelist.net','name':'myanimelist'})
        yield scrapy.Request(url=url3, callback=self.getLink,meta={'domain':'justwatch.com','name':'justwatch'})


    def getLink(self, response):
        xlink = LinkExtractor()
        links = []
        for l in xlink.extract_links(response):
            if response.meta['domain'] in l.url:
                links.append(l.url)
        #print(links)
        if len(links) > self.maxDep:
            lim = self.maxDep
        else:
            lim = len(links)
        #print(lim)
        for i in range(lim):
            url = links[i]
            if url is not None:
                #print(f'resquest - link:{i}')
                if response.meta['name'] == 'myanimelist':
                    yield scrapy.Request(url=url, callback=self.parse_mal)
                elif response.meta['name'] == 'wikipedia':
                    yield scrapy.Request(url=url, callback=self.parse_wiki)
                elif response.meta['name'] == 'justwatch':
                    yield scrapy.Request(url=url, callback=self.parse_streaming)


    def parse_wiki(self, response):
        name = response.css('#firstHeading i::text').get()
        description = ''.join([k for k in response.css('.infobox_v2+ p').css('::text').extract()])
        #genres = [k for k in response.css('.ambox-content+ .infobox_v2 td+ td').css('::text').extract() if len(k) > 1]# ------ nao funciona
        wikiList = {'name':name, 'description':description}
        yield wikiList
    
    def parse_mal(self, response):

        jp_name = response.css('.h1_bold_none strong::text').get() #****extraindo nomes direto do site usando seletor CSS****
        en_name = response.css('.title-inherit::text').get()#****igual****
        url_image = response.css('.borderClass div div .lazyload::attr(data-src)').get()
        en_synopsis = ''#****criando var da sinopse****
        temp = response.css('.pb16~ p::text').extract()#****criando temp var para tratar sinopse****
        temp = temp[:-1]
        for i in range(len(temp)):
            for j in ['\n', '\r']:
                temp[i] = temp[i].replace(j, '')
        en_synopsis = en_synopsis.join(temp)#****juntando sinopse tratada com string vazia****
        del temp#****deletando para economizar espaço****
        infoList = [i.strip() for i in response.css('#content > table .borderClass div').css('::text').extract()]
        infoList = [i for i in infoList if len(i)> 0]
        infoList = infoList[infoList.index('Type:'):infoList.index('Rating:')+10]
        temp = []
        for i in infoList:
            if i not in temp:
                temp.append(i)
        infoList = temp.copy()
        del temp
        infoList = infoList[:infoList.index('Statistics')]
        infoList = [i for i in infoList if len(i)>1]
        try:
            infoList.pop(infoList.index('Broadcast:')+1)
            infoList.pop(infoList.index('Broadcast:'))
        except:
            pass
        indexers = [i for i in infoList if ':' in i]
        malDict = {'jp_name':jp_name, 'en_name':en_name, 'en_synopsis':en_synopsis, 'url_image': url_image}
        for i in indexers:
            malDict[i] = None
        for i in range(len(indexers)):
            ac = i
            nac = i+1
            if nac >= len(indexers):
                malDict[indexers[i]] = infoList[infoList.index(indexers[ac])+1:]
                break        
            malDict[indexers[i]] = infoList[infoList.index(indexers[ac])+1:infoList.index(indexers[nac])]
        del indexers
        for i in malDict:
            try:
                if len(malDict[i])<=1:
                    malDict[i] = malDict[i][0]
            except:
                print(malDict[i])
        
        yield malDict

    def parse_streaming(self,response):
        stream = response.css('.price-comparison--block .price-comparison__grid__row__holder div div img::attr(alt)').getall()
        streamDict = {'stream':stream}
        yield streamDict
