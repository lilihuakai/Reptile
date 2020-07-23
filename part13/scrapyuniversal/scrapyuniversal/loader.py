#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose


class NewsLoader(ItemLoader):
    """docstring for NewsLoader"""
    default_output_processor = TakeFirst()


class ChinaLoader(NewsLoader):
    """docstring for ChinaLoader"""
    text_out = Compose(Join(), lambda s: s.strip())
    source_out = Compose(Join(), lambda s: s.strip())

