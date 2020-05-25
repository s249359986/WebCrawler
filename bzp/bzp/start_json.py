
from scrapy import cmdline

cmdline.execute("scrapy crawl lagou -o scraped_data.json -s FEED_EXPORT_ENCODING=utf-8".split())