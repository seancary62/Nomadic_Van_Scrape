import scrapy


class CraigslistVansSpider(scrapy.Spider):
    name = 'craigslist_vans'
    allowed_domains = ['www.craigslist.org']
    start_urls = ['https://charlotte.craigslist.org/search/sss?query=van']



    def parse(self, response):

        vans = response.xpath('//div[@class="content"]/ul/li')

        for van in vans:
            yield {
                'product_name': van.xpath('.//h3/a/text()').get(),
                'post_date': van.xpath('.//time/text()').get(),
                'price':van.xpath('.//span[@class="result-price"]/text()').get(),
                'location':van.xpath('.//span[@class"result-hood"/text()').get(),
                # 'link':van.xpath('.//h3')
            }

  
