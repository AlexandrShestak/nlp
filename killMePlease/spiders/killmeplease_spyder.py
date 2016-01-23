from scrapy import Spider
from scrapy.selector import Selector

from killMePlease.items import KillMePleaseItem

class KillMePleaseSpider(Spider):
    name = "kmp"
    allowed_domains = ["http://killpls.me/"]
    start_urls = ["http://killpls.me"]

    def parse(self, response):
        posts = Selector(response).xpath('/html/body/div[@class="container"]/div/div[@id="stories"]')
        for post in posts:
            item = KillMePleaseItem()
            item['post_text'] = post.xpath(
                '/html/body/div[@class="container"]/div/div[@id="stories"]/div[@class="row"]/div[@class="col-xs-12" and contains(@style,"margin:0.5em 0;line-height:1.785em")]/text()').extract()[0]
            item['stars'] = post.xpath(
                '/html/body/div[@class="container"]/div/div[@id="stories"]/'
                'div[@class="row"]/div[@class="col-xs-12"]/div/b').extract()[0]
            yield item





