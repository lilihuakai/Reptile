#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from scrapy.loader.processors import TakeFirst
from scrapy.loader.processors import Join
from scrapy.loader.processors import Compose
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import SelectJmes


processor = SelectJmes('foo')
print(processor({'foo': 'bar'}))

processor = MapCompose(str.upper, lambda s: s.strip())
print(processor(['hello', 'world', 'python']))

processor = Compose(str.upper, lambda s: s.strip())
print(processor(" hello world"))

processor = Join(',')
# processor = Join()
print(processor(['one', 'two', 'three']))

processor = TakeFirst()
print(processor(['', 1, 2, 3]))
