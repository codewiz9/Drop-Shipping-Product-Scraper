# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DsHelperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # cleans up the about
        string = adapter.get('about')
        string.replace(",", "")
        x = " ".join(string.split())
        x.replace("ASINaboutdiscountimage_urlnumber_of_reviewsproduct_nameprriceseller_rankstars_out_of_five", "")
        adapter['about'] = x

        return item
