# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re

class PicSpider(scrapy.Spider):
    name = 'pic'
    allowed_domains = ['www.mmjpg.com']
    start_urls = ['http://www.mmjpg.com']

    def pic_parse(self, response):
        pass

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        # print(soup.find_all('ul'))
        for ul in soup.find_all('ul'):
            # print(ul.find_all('li'))
            contents = ul.find_all('li')
            contents_dict = {}
        for i in range(len(contents)):
            content = re.findall('<a.href="(http.*?/\d+)".*?<img\salt="(.*?)".*?</a>', str(contents[i]))[0]
            #print(content)
            contents_dict[content[1]] = content[0]
        print(contents_dict)
        for key in contents_dict.keys():
            yield scrapy.Request(url=contents_dict[key], callback=self.pic_parse)




