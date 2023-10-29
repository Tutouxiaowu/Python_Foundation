import requests
import scrapy
import re

from codeinclass.items import CodeinclassItem


class CqwuSpider(scrapy.Spider):
    name = "cqwu"
    start_urls = ["https://www.cqwu.edu.cn/channel_24893_031.html"]
    def parse(self, response):
        #获取标题
        title_list= response.xpath('/html/body/div/div[2]/div[2]/ul/li/a/div[2]/h4/text()').extract()
        #获取网址url
        url_list = response.xpath('/html/body/div/div[2]/div[2]/ul/li/a/@href').extract()
        #获取发布时间
        time_list = response.xpath('/html/body/div/div[2]/div[2]/ul/li/a/div[3]/p[1]/text()').extract()
        for i in range(len(url_list)):
            url_list[i] = url_list[i].replace('/','https://www.cqwu.edu.cn/')
        content_list = response.xpath('/html/body/div/div[2]/div[2]/ul/li/a/div[2]/p/text()').extract()
        item = CodeinclassItem()
        for title in title_list:
           item['title'] = title
        for time in time_list:
            item['date'] = time
        for url in url_list:
            item['url'] = url
        for content in content_list:
            item['content'] = content
        yield item
        # print(content_list)
        # print(time_list)
        # print(title_list)
        next = response.xpath('/html/body/div/div[2]/div[3]/div/a[12]/@href').extract_first()
        next = 'https://www.cqwu.edu.cn/'+ str(next)
        # print(next)
        yield scrapy.Request(url=next, callback=self.parse)