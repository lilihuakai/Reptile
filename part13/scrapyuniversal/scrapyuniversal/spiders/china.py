import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapyuniversal.items import *
from scrapyuniversal.loader import *


class ChinaSpider(CrawlSpider):
    name = 'china'
    allowed_domains = ['tech.china.com']
    start_urls = ['https://tech.china.com/articles/']

    rules = (
        Rule(LinkExtractor(allow='article\/.*\.html', restrict_xpaths='//div[@id="rank-defList"]//div[@class="item_con"]'), callback='parse_item'),
        # Rule(LinkExtractor(restrict_xpaths='//div[@class="pages"]//a[contains(., "下一页")]')),
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        loader = ChinaLoader(item=NewItem(), response=response)
        loader.add_xpath('title', '//h1[@id="chan_newsTitle"]/text()')
        loader.add_value('url', response.url)
        loader.add_xpath('text', '//div[@id="chan_newsDetail"]//text()')
        loader.add_xpath('datetime', '//span[@class="time"]/text()', re='\d+-\d+-\d+\s\d+:\d+:\d+')
        loader.add_xpath('source', '//span[@class="source"]/text()', re='来源：(.*)')
        loader.add_value('website', '中华网')

        # item = NewItem()
        # item['title'] = response.xpath('//h1[@id="chan_newsTitle"]/text()').extract_first()
        # item['url'] = response.url
        # item['text'] = ''.join(response.xpath('//div[@id="chan_newsDetail"]//text()').extract()).strip()
        # item['datetime'] = response.xpath('//span[@class="time"]/text()').re_first('\d+-\d+-\d+\s\d+:\d+:\d+')
        # item['source'] = response.xpath('//span[@class="source"]/text()').re_first('来源：(.*)').strip()
        # item['website'] = "中华网"

        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        yield loader.load_item()
        # return item
