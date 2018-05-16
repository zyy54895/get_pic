# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request

# class GetPicPipeline(object):
#     def process_item(self, item, spider):
#         return item

# 下载图片Pipeline
class DownImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['pic_url']:
            yield Request(image_url)

    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        return 'full/%s' % (image_guid)