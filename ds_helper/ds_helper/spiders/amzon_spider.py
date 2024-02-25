import scrapy
from ds_helper.items import AmzonScraperItem

class AmzonSpiderSpider(scrapy.Spider):
    name = "amzon_spider"
    allowed_domains = ["amzon.com", "www.amazon.com"]
    start_urls = ["https://amzon.com"]

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES':  "'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725",
}
    

    def parse(self, response):
        key_word = 'games'
        url = 'https://www.amazon.com/s?k=games'
        yield response.follow(url, callback=self.parser_middle_man)

    def parser_middle_man (self, response):
        print('hello')
        products = response.css("div.s-result-item[data-component-type=s-search-result]")
        for product in products:
            new_url_ = product.css("h2>a::attr(href)").get()
            new_url = f'https://www.amazon.com{new_url_}'
        
            yield response.follow(new_url, callback=self.parse_product)

    def parse_product(self, response):
        table_rows = response.css("table tr")
        product_item = AmzonScraperItem()
        product_item['product_name'] = response.css('span#productTitle ::text').get()
        product_item['image_url'] = response.css('div.imgTagWrapper ::attr(src)').get()
        product_item['number_of_reviews'] = response.css('span#acrCustomerReviewText ::text').get()
        product_item['stars_out_of_five'] = response.xpath('//*[@id="acrPopover"]/span[1]/a/span/text()').get()
        product_item['prrice'] = response.css('span.a-offscreen ::text').get()
        product_item['discount'] = response.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]/text()').get()
        #note you need to put the about throughe a pipelin bc there is a lot of extra puncuation in the text
        product_item['about'] =  response.css('span.a-list-item ::text').getall()
        #need to add a pipe line to clean data
        product_item['seller_rank'] = response.xpath('//*[@id="productDetails_detailBullets_sections1"]').get()
        product_item['ASIN'] = table_rows[4].css('td.a-size-base ::text').get()

        yield product_item