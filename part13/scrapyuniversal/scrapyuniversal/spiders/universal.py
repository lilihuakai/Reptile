import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapyuniversal.items import *
from scrapyuniversal.loader import *
from scrapyuniversal.utils import get_config
from scrapyuniversal import urls
from scrapyuniversal.rules import rules


class UniversalSpider(CrawlSpider):
    name = 'universal'

    def __init__(self, name, *args, **kwargs):
        config = get_config(name)
        self.config = config
        self.rules = rules.get(config.get('rules'))
        # self.start_urls = config.get('start_urls')
        start_urls = config.get('start_urls')
        if start_urls:
            if start_urls.get('type') == 'static':
                self.start_urls = start_urls.get('value')
            elif start_urls.get('type') == 'dynamic':
                self.start_urls = list(eval('urls.' + start_urls.get('method'))(*start_urls.get('args', [])))
        self.allow_domains = config.get('allow_domains')
        super (UniversalSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        item = self.config.get('item')
        if item:
            cls = eval(item.get('class'))()
            loader = eval(item.get('loader'))(cls, response=response)
            # 动态获取属性配置
            for key, value in item.get('attrs').items():
                for extrator in value:
                    if extrator.get('method') == 'xpath':
                        loader.add_xpath(key, *extrator.get('args'), **{'re': extrator.get('re')})
                    if extrator.get('method') == 'css':
                        loader.add_css(key, *extrator.get('args'), **{'re': extrator.get('re')})
                    if extrator.get('method') == 'value':
                        loader.add_value(key, *extrator.get('args'), **{'re': extrator.get('re')})
                    if extrator.get('method') == 'attr':
                        loader.add_value(key, getattr(response, *extrator.get('args')))
            yield loader.load_item()
