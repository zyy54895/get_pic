# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from get_pic.items import GetPicItem
import re


class PicSpider(scrapy.Spider):
    name = 'pic'
    allowed_domains = ['www.mmjpg.com']
    start_urls = ['http://www.mmjpg.com/']

    def parse(self, response):
        sel = Selector(response)
        urls = sel.xpath('//div[@class="pic"]/ul/li/a/@href').extract()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.pic_parse)

        next_page = self.start_urls[0] + sel.xpath('//div[@class="page"]//a[text()="下一页"]/@href').extract()[0]
        print(next_page)
        yield scrapy.Request(url=next_page, callback=self.parse)

    def pic_parse(self, response):
        sel = Selector(response)
        content = sel.xpath('//div[@class="article"]/h2/text()').extract()[0]
        content = re.sub(r'\(\d+\)', '', content)
        title = response.xpath('//div[@class="content"]/a//@alt').extract()[0]
        pic_url = response.xpath('//div[@class="content"]/a//@data-img').extract()
        #print(title, pic_url)
        item = GetPicItem(pic_url=pic_url, title=title, content=content)
        yield item
        next_page = response.xpath('//div[@class="page"]/a[text()="下一张"]/@href').extract()
        if next_page:
             yield scrapy.Request(url=self.start_urls[0] + next_page[0], callback=self.pic_parse)


