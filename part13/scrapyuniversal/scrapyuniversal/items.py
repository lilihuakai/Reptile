# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class ScrapyuniversalItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class NewItem(Item):
    """docstring for NewItem"""
    title = Field()
    url = Field()
    text = Field()
    datetime = Field()
    source = Field()
    website = Field()
