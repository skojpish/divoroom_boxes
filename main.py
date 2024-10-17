from aiogram import Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
from loguru import logger
from settings import (
    BASE_WEBHOOK_URL,
    WEB_SERVER_HOST,
    WEB_SERVER_PORT,
    WEBHOOK_PATH,
    bot,
    redis_storage,
)

from commands.handlers import router as commands_router
from boxes.handlers import router as boxes_router
from paper.handlers import router as cards_router
from custom_things.handlers import router as custom_router
from food.handlers import router as food_router


async def on_startup() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}")


def main() -> None:
    dp = Dispatcher(storage=redis_storage)

    dp.include_routers(
        commands_router, boxes_router, cards_router, custom_router, food_router
    )

    dp.startup.register(on_startup)

    app = web.Application()

    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )

    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    setup_application(app, dp, bot=bot)

    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.critical(f"Fail to start bot! Reason: {e}")
