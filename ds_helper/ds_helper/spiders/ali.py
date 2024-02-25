import scrapy
from ds_helper.items import AliItems

class AliSpider(scrapy.Spider):
    name = "ali"
    allowed_domains = ["www.aliexpress.us"]
    start_urls = ["https://www.aliexpress.us/"]

    def parse(self, response):
        new_url = f'https://www.aliexpress.us/w/wholesale-{self.cat}.html?spm=a2g0o.home.search.0'
        yield response.follow(new_url, callback=self.parser_middle_man)

    def parser_middle_man(self, response):
        Items = AliItems
        produts = response.css('div.list--galleryWrapper--29HRJT4').get()
        for product in produts:
            Items['link'] = product.xpath('//*[@id="card-list"]/div[1]/div/a/@href').get()
            Items['product_name'] =  response.css('h3.multi--titleText--nXeOvyr ::text').get()
            product['image_url'] =  response.css('img.images--item--3XZa6xf ::attr(src)').get()
            product['amount_sold'] = response.css('span.multi--trade--Ktbl2jB ::text').get()
            prices = response.css('div.multi--price-sale--U-S0jtj').get()
            x = ''
            for price in prices:
                x += response.xpath('//*[@id="card-list"]/div[1]/div/a/div[2]/div[3]/div[1]/span[1]/text()').get()
            Items['prrice'] = x


    