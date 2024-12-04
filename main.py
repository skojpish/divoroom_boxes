import asyncio

from aiogram import Dispatcher
from loguru import logger
from settings import bot, redis_storage
from commands.handlers import router as commands_router
from boxes.handlers import router as boxes_router
from paper.handlers import router as cards_router
from custom_things.handlers import router as custom_router


async def main() -> None:
    dp = Dispatcher(storage=redis_storage)

    dp.include_routers(commands_router, boxes_router, cards_router, custom_router)

    try:
        logger.info("---BOT STARTING---")
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        logger.critical(f"Fail to start bot! Reason: {e}")


if __name__ == "__main__":
    asyncio.run(main())
