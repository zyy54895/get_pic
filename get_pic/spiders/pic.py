# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re

class PicSpider(scrapy.Spider):
    name = 'pic'
    allowed_domains = ['www.mmjpg.com']
    start_urls = ['http://www.mmjpg.com']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        # print(soup.find_all('ul'))
        for ul in soup.find_all('ul'):
            # print(ul.find_all('li'))
            contents = ul.find_all('li')
        for i in range(len(contents)):
            content_url = re.findall('<a.href="(http.*?/\d+)".*?</a>', str(contents[i]))
            print(content_url)



