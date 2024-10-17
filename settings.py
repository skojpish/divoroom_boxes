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

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))

redis_instance = Redis.from_url(REDIS_URL)

redis_storage = RedisStorage(redis=redis_instance)
