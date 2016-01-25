from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
import time
from kmp.items import KmpItem


START_PAGE_NUMBER = 1710
PAGE_COUNT = 10

class KillMePleaseSpider(Spider):
    name = "kmp"
    allowed_domains = ["http://killpls.me/"]
    #start_urls = ["http://killpls.me/page/" + START_PAGE_NUMBER]


    def start_requests(self):
        for page_number in range(START_PAGE_NUMBER - PAGE_COUNT, START_PAGE_NUMBER):
            yield Request("http://killpls.me/page/" + str(page_number),  callback=self.parse)

    def parse(self, response):
        posts = Selector(response).xpath(
            '/html/body/div[    @class="container"]/div/div[@id="stories"]'
            '/div[@class="row"]/div[@class="col-xs-12" '
            'and contains(@style,"margin:0.5em 0;line-height:1.785em")]')
        stars = Selector(response).xpath(
            '/html/body/div[@class="container"]/div/div[@id="stories"]/'
            'div[@class="row"]/div[@class="col-xs-12"]/div/b')
        count = 0
        for post in posts:
            item = KmpItem()
            item['post_text'] = " ".join(post.xpath('text()').extract())
            item['stars'] = stars[count].xpath('text()').extract()
            '''item['post_text'] = [s.encode("utf-8") for s in post.xpath('text()').extract()[0]]
            item['stars'] = [s.encode("utf-8") for s in stars[count].extract()]'''
            count += 1
            yield item
        time.sleep(5)
