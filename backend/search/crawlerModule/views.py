from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from rest_framework.views import APIView
#from .models import ScrapyItem
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings
from crawlerModule.scrapyCrawlers.scrapyCrawlers.spiders.serie import SerieSpider
from crawlerModule.scrapyCrawlers.scrapyCrawlers.spiders.anime import AnimeSpider
from twisted.internet import reactor
import os
import time
import subprocess
from crochet import setup
setup()


#process.start(stop_after_crawl=True)

class CrawlerView(APIView):
    def post(self, request):
        name = request.data['title']
        attraction_type = request.data['type']
        process = CrawlerRunner(get_project_settings())
        if attraction_type == "anime":
            name += " anime"
            spider = AnimeSpider
            process.crawl(spider, an = name)
        elif attraction_type == "serie" or attraction_type == "movie":
            print("entrou pra fazer o request")
            spider = SerieSpider
            process.crawl(spider, at = name, tp = attraction_type)

            
         # the script will block here until the crawling is finished

        # d = process.crawl(spider, an = animeName)
        # #d.addBoth(lambda _: reactor.stop())
        # reactor.run()
        

        return JsonResponse({'task_id': 1, 'status': 'started' })






