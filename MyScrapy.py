#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scrapy import Spider, Item, Field

class Post(Item):
    title = Field()

class BlogSpider(Spider):
    name, start_urls = 'blogspider', ['http://blog.scrapinghub.com']

    def parse(self, response):
        return [Post(title=e.extract()) for e in response.css("h2 a::span")]