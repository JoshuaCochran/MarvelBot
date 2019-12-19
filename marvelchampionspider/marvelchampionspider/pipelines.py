# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class MarvelchampionspiderPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        meta = {'filename': item['title']}
        for x in item.get(self.images_urls_field, []):
            return scrapy.Request(x, meta=meta)

    def file_path(self, request, response=None, info=None):
        image_guid = request.meta.get('filename', '')
        return '%s.jpg' % (image_guid)
