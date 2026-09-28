import scrapy_poet
import scrapy_zyte_api

BOT_NAME = "bilibili_up"

SPIDER_MODULES = ["bilibili_up.spiders"]
NEWSPIDER_MODULE = "bilibili_up.spiders"

ADDONS = {
    scrapy_poet.Addon: 300,
    scrapy_zyte_api.Addon: 500,
}

SCRAPY_POET_DISCOVER = ["bilibili_up.pages"]

#ZYTE_API_KEY = "YOUR_API_KEY"
ZYTE_API_TRANSPARENT_MODE = False
