# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import CrawlSpider, Rule
from webscraper.items import WebscraperItem


class AmazingSpider(CrawlSpider):
	name = 'amazing'
	depth_limit = 2
	allowed_domains = ['']
	start_urls = ['']
	rules = (
		Rule(LinkExtractor(allow=('quora.com')), callback='parse_item', follow=True),
	)

	def parse_item(self, response):
		item = WebscraperItem()
		item['url'] = response.url
		item['content'] = response.xpath('//p//text()').extract()
		return item
