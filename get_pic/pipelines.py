# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import json
import codecs
class GetPicPipeline(object):
    def __init__(self):
        self.f = codecs.open('content.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):

        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.f.write(line)
        return item

# 下载图片Pipeline
class DownImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['pic_url']:
            yield Request(image_url, meta={'item': item})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
            item['image_paths'] = image_paths
        return item

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        image_guid = item['title']+'.'+ request.url.split('/')[-1].split('.')[-1]
        filepath = u'full/{0}/{1}'.format(item['content'], image_guid)
        return filepath