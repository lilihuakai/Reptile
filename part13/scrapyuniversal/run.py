#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

from scrapyuniversal.spiders.universal import UniversalSpider
from scrapyuniversal.utils import get_config


def run():
    name = sys.argv[1]
    custom_settings = get_config(name)
    # 爬墙使用的Spider名称
    spider = custom_settings.get('spider', 'universal')
    project_settings = get_project_settings()
    settings = dict(project_settings.copy())
    # 合并配置
    settings.update(custom_settings.get('settings'))
    process = CrawlerProcess(settings)
    # 启动爬虫
    process.crawl(spider, **{'name': name})
    process.start()

if __name__ == '__main__':
    run()
