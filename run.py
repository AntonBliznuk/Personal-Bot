import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import TOKEN

from app.handlers.MainHandlers import router
from app.handlers.FSM_Сryptocurrency import router_cripto
from app.handlers.FSM_Shares import router_shares
from app.DataManagement import create_table

# Initialize the Bot with the provided TOKEN
bot = Bot(token=TOKEN)

# Initialize the Dispatcher for handling updates
dp = Dispatcher()


async def main():
    # Register routers for different types of handlers
    dp.include_router(router)
    dp.include_router(router_cripto)
    dp.include_router(router_shares)

    # Start polling for updates from the bot
    await dp.start_polling(bot)


if __name__ == '__main__':
    # Configure logging to show informational messages
    logging.basicConfig(level=logging.INFO)

    # Create necessary database tables
    create_table()

    try:
        # Run the main function to start the bot
        asyncio.run(main())
    except KeyboardInterrupt:
        # Handle manual interruption (Ctrl+C) gracefully
        print("Exit")
