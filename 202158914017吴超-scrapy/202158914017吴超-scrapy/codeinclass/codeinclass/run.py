# -*- coding: UTF-8 -*-
from scrapy import cmdline
#导入cmd命令窗口
cmdline.execute("scrapy crawl cqwu -o a.csv" .split())
#运行爬虫并生产csv文件