# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CodeinclassItem(scrapy.Item):
    title = scrapy.Field()  # 文章标题
    type = scrapy.Field()  # 文章类型(原创/转载/翻译)
    url = scrapy.Field()  # 文章链接
    date = scrapy.Field()  # 文章发布日期
    read_num = scrapy.Field()  # 文章阅读量
    content = scrapy.Field()
class BaidutiebaItem(scrapy.Item):
    title = scrapy.Field()  # 标题
    url = scrapy.Field()  # 链接
    date = scrapy.Field()  # 发布日期
    read_num = scrapy.Field()  # 阅读量



