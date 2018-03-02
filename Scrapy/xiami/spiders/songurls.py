# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from xiami.items import SongUrlItem

class SongUrlsSpider(scrapy.Spider):
    name='SongUrls'
    allowed_domains=['xiami.com']
    
    #from page 1 to page 401, put all links to start_urls
    start_url_list=[]
    url_fixed='http://www.xiami.com/genre/songs/gid/16/page/'
    #extend to 1-401
    for i in range(1,150):
        start_url_list.extend([url_fixed+str(i)])
    start_urls=start_url_list
    
    def parse(self,response):
        urls=response.xpath('//div[@class = "info"]/p[1]/strong/a/@href').extract()

        for url in urls:
            song_url=response.urljoin(url)
            url_item=SongUrlItem()
            url_item['song_url']=song_url
            yield url_item
