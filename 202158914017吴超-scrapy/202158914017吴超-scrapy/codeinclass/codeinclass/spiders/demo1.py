import scrapy


class Demo1Spider(scrapy.Spider):
    name = "demo1"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://baidu.com"]

    def parse(self, response):
        pass
