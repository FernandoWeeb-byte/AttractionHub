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
import os
import time
import subprocess
from crochet import setup
setup()


#process.start(stop_after_crawl=True)

class CrawlerView(APIView):
    def post(self,request):
        animeName = request.data['anime']
        animeName += " anime"
        spider = AnimeSpider
        
        process = CrawlerRunner(get_project_settings())
        process.crawl(spider, an = animeName)

            
         # the script will block here until the crawling is finished

        # d = process.crawl(spider, an = animeName)
        # #d.addBoth(lambda _: reactor.stop())
        # reactor.run()
        

        return JsonResponse({'task_id': 1, 'status': 'started' })






