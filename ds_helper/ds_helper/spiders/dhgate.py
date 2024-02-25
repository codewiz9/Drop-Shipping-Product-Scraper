import scrapy
from ds_helper.items import DHItems

class DhgateSpider(scrapy.Spider):
    name = "dhgate"
    allowed_domains = ["www.dhgate.com"]
    start_urls = ["https://www.dhgate.com/"]

    def parse(self, response):
        produt = 'games'
        new_url = f'https://www.dhgate.com/wholesale/search.do?separate=1&act=search&dspm=pcen.pd.searclick.1.SCCMLo2Xln69Fy7Bt6As%26resource_id%3D&sus=&searchkey={self.cat}&catalog=#pusearch1812'
        yield scrapy.Request(url=new_url, callback=self.new_parse)

    def new_parse(self, response):
        product_items = DHItems
        products = response.css('div.product-list-warp').get()
        for product in products:
            url = response.xpath('//*[@id="__next"]/div[5]/div/div/div[4]/div[2]/div[2]/div/div[1]/div/ul/li[1]/div/div[1]/a[1]/@href').get()
            product_items['link'] = url
            yield scrapy.Request(url=url, callback=self.parse_product)

    def parse_product(self, response):
        product_items = DHItems
        product_items['product_name'] = response.xpath('//*[@id="productdisplayForm"]/div/div[1]/div[1]/h1/text()').get()
        product_items['image_url'] = response.css('img.j-prod-img ::attr(src)').get()
        product_items['prrice'] = response.xpath('//*[@id="productdisplayForm"]/div/div[5]/div/div[2]/div[1]/ul/li[1]/span[1]/text()').get()
        product_items['number_of_reviews'] = response.css('span.review ::text').get()
        product_items['stars_out_of_five'] = response.css('span.star ::attr(style)').get()
        product_items['amount_sold'] = response.xpath('//*[@id="productdisplayForm"]/div/div[1]/ul/li/span[2]/span/b/text()').get()
        dlviery_1 = response.xpath('//*[@id="productdisplayForm"]/div/div[14]/div[1]/div[3]/div/div[1]/span[1]/text()').get()
        dlivery_2 = response.xpath('//*[@id="productdisplayForm"]/div/div[14]/div[1]/div[3]/div/div[1]/span[2]/text()').get()
        dlivery_3 = response.xpath('//*[@id="productdisplayForm"]/div/div[14]/div[1]/div[3]/div/div[1]/span[3]/text()').get()
        product_items['dlivery_time'] = f'{dlviery_1} {dlivery_2} {dlivery_3}'
        

