import os
from pathlib import Path

import scrapy_poet
import scrapy_zyte_api
from dotenv import load_dotenv

BOT_NAME = "bilibili_up"

SPIDER_MODULES = ["bilibili_up.spiders"]
NEWSPIDER_MODULE = "bilibili_up.spiders"

ADDONS = {
    scrapy_poet.Addon: 300,
    scrapy_zyte_api.Addon: 500,
}

SCRAPY_POET_DISCOVER = ["bilibili_up.pages"]

# 密钥只从环境变量读取：本地走项目根目录 .env，Scrapy Cloud 走平台环境变量
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

ZYTE_API_KEY = os.environ["ZYTE_API_KEY"]
