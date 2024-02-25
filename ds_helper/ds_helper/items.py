# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmzonScraperItem(scrapy.Item):
    product_name = scrapy.Field()
    image_url = scrapy.Field()
    number_of_reviews = scrapy.Field()
    stars_out_of_five = scrapy.Field()
    prrice = scrapy.Field()
    discount = scrapy.Field()
    about = scrapy.Field()
    seller_rank = scrapy.Field()
    ASIN = scrapy.Field()

class DHItems(scrapy.Item):
    product_name = scrapy.Field()
    image_url = scrapy.Field()
    number_of_reviews = scrapy.Field()
    stars_out_of_five = scrapy.Field()
    prrice = scrapy.Field()
    amount_sold = scrapy.Field()
    dlivery_time = scrapy.Field()
    link = scrapy.Field()
    #discription = scrapy.Field()

class AliItems(scrapy.Item):
    product_name = scrapy.Field()
    image_url = scrapy.Field()
    prrice = scrapy.Field()
    amount_sold = scrapy.Field()
    link = scrapy.Field()
