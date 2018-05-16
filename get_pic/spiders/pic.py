# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re
from get_pic.items import GetPicItem
class PicSpider(scrapy.Spider):
    name = 'pic'
    allowed_domains = ['www.mmjpg.com']
    start_urls = ['http://www.mmjpg.com/']

    def parse(self, response):
        urls = response.xpath('//div[@class="pic"]/ul/li/a/@href').extract()
        print(urls)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.pic_parse)
        # soup = BeautifulSoup(response.text, 'lxml')
        # for ul in soup.find_all('ul'):
        #     contents = ul.find_all('li')
        #     contents_dict = {}
        # for i in range(len(contents)):
        #     content = re.findall('<a.href="(http.*?/\d+)".*?<img\salt="(.*?)".*?</a>', str(contents[i]))[0]
        #     contents_dict[content[1]] = content[0]
        # for key in contents_dict.keys():
        #     yield scrapy.Request(url=contents_dict[key], callback=self.pic_parse)

    def pic_parse(self, response):
        title = response.xpath('//div[@class="content"]/a//@alt').extract()[0]
        pic_url = response.xpath('//div[@class="content"]/a//@data-img').extract()
        print(title, pic_url)
        item = GetPicItem(pic_url=pic_url, title=title)
        yield item
        next_page = response.xpath('//div[@class="page"]/a[text()="下一张"]/@href').extract()
        if next_page:
             yield scrapy.Request(url=self.start_urls[0] + next_page[0], callback=self.pic_parse)


