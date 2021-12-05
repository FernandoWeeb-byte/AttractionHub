from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from rest_framework.views import APIView
#from .models import ScrapyItem

from scrapy.crawler import CrawlerProcess, CrawlerRunner, Crawler
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings
from crawlerModule.scrapyCrawlers.scrapyCrawlers.spiders.serie import SerieSpider
from crawlerModule.scrapyCrawlers.scrapyCrawlers.spiders.anime import AnimeSpider
from crawlerModule.scrapyCrawlers.scrapyCrawlers import settings
from twisted.internet import reactor
import os
import time
import asyncio
from crochet import setup

setup()


#process.start(stop_after_crawl=True)

class CrawlerView(APIView):
    def post(self, request):
        name = request.data['title']
        attraction_type = request.data['type']
        process = CrawlerRunner(get_project_settings())
        print(request.data)
        if attraction_type == "anime":
            print("aquiCrawler")
            name += " anime"
            spider = AnimeSpider
            r = process.crawl(spider, an = name)
        elif attraction_type == "serie" or attraction_type == "movie":
            print("entrou pra fazer o request")
            spider = SerieSpider
            r = process.crawl(spider, at = name, tp = attraction_type)
         
        f = True
        f = r.addCallback(lambda _:True)
        od = time.time()
        while True:
            try:
                print(f.result) 
                if f.result:
                    return JsonResponse({'task_id': 1, 'status': 'started' })
            except Exception:
                asyncio.sleep(5)
                t = time.time()
                if t - od >= 5.0:
                    print("carregando...")
                    od = t
                    





