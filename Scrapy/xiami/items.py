# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SongUrlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    song_url=scrapy.Field()

class LyricItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    lyric=scrapy.Field()
    song_url=scrapy.Field()
    
    
class SongInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    song_url=scrapy.Field()
    song_title=scrapy.Field()
    album=scrapy.Field()
    #singer=scrapy.Field()
    language=scrapy.Field()
    
    
