from scrapy import Spider
from scrapy.selector import Selector
from kmp.items import KmpItem


class KillMePleaseSpider(Spider):
    name = "kmp"
    allowed_domains = ["http://killpls.me/"]
    start_urls = ["http://killpls.me"]

    def parse(self, response):
        posts = Selector(response).xpath(
            '/html/body/div[@class="container"]/div/div[@id="stories"]'
            '/div[@class="row"]/div[@class="col-xs-12" '
            'and contains(@style,"margin:0.5em 0;line-height:1.785em")]')
        stars = Selector(response).xpath(
            '/html/body/div[@class="container"]/div/div[@id="stories"]/'
            'div[@class="row"]/div[@class="col-xs-12"]/div/b')
        count = 0
        for post in posts:
            item = KmpItem()
            """item['post_text'] = post.xpath(
                '/html/body/div[@class="container"]/div/div[@id="stories"]'
                '/div[@class="row"]/div[@class="col-xs-12" '
                'and contains(@style,"margin:0.5em 0;line-height:1.785em")]/text()').extract()[0]
            item['stars'] = post.xpath(
                '/html/body/div[@class="container"]/div/div[@id="stories"]/'
                'div[@class="row"]/div[@class="col-xs-12"]/div/b').extract()[0]"""

            item['post_text'] = post.xpath('text()').extract()[0]
            item['stars'] = stars[count].extract()
            count += 1
            yield item
