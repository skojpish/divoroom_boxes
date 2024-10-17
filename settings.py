from os import getenv

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from redis.asyncio import Redis
from aiogram.fsm.storage.redis import RedisStorage


BOT_TOKEN = getenv("BOT_TOKEN")
MASTER_ID = getenv("MASTER_ID")
MASTER_USERNAME = getenv("MASTER_USERNAME")

REDIS_HOST = getenv("REDIS_HOST")
REDIS_PORT = getenv("REDIS_PORT")

REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"

WEB_SERVER_HOST = "127.0.0.1"
WEB_SERVER_PORT = 8080

WEBHOOK_PATH = "/webhook_boxes"
BASE_WEBHOOK_URL = "https://divoroombot.ru"

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))

redis_instance = Redis.from_url(REDIS_URL)

redis_storage = RedisStorage(redis=redis_instance)
