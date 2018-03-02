# -*- coding: utf-8 -*-
import scrapy
from xiami.items import LyricItem

class LyricsSpider(scrapy.Spider):
    name='Lyrics'
    allowed_domains=['xiami.com']
    song_url_file='./result/SongUrls.csv'
    
    
    def __init__(self, *args, **kwargs):
        #read song_url.csv get all song url
        f = open(self.song_url_file,"r") 
        lines = f.readlines()
        #line[:-1] remove enter ion each line
        #in lines[1:] remove csv first line
        song_url_list=[line[:-1] for line in lines[1:]]
        while '' in song_url_list:
            song_url_list.remove('')
        f.close()

        self.start_urls = song_url_list
    
    def parse(self,response):
        
        lyric_lines=response.xpath('//*[@id="lrc"]/div[1]/text()').extract()
        lyric=''
        for lyric_line in lyric_lines:
            lyric+=lyric_line
        #print lyric
        
        lyricItem=LyricItem()
        lyricItem['lyric']=lyric
        lyricItem['song_url']=response.url
        yield lyricItem
