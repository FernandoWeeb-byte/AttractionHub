from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
#from .models import ScrapyItem
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings
from crawlerModule.scrapyCrawlers.scrapyCrawlers.spiders.anime import AnimeSpider
from twisted.internet import reactor
import requests
from .models import Attraction
# from crochet import setup
# setup()




class CrawlerView(APIView):
    def post(self,request):
        animeName = request.data['anime']
        animeName += " anime"
        r = requests.post('http://localhost:6800/schedule.json', data={'project':'scrapyCrawlers','spider': 'anime', 'an': animeName})
        #r = requests.post('http://localhost:6800/schedule.json', data={'project':'scrapyCrawlers','spider': 'serie', 'at': animeName})
        # spider = AnimeSpider
        # process = CrawlerProcess(get_project_settings())
        
        # process.crawl(spider, an = animeName)
        # process.start() # the script will block here until the crawling is finished

        # d = process.crawl(spider)
        # d.addBoth(lambda _: reactor.stop())
        # reactor.run()
        

        return JsonResponse({'task_id': 1, 'status': 'started' })



    def get(self,response):
        return JsonResponse({'att': 1})


