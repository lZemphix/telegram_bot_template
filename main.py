import asyncio, os
from dotenv import load_dotenv
from database.actions import table_actions
from aiogram import Bot, Dispatcher
from handlers import user_commands, admin_commands
from utils import middlewares

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()



async def main():
    dp.include_routers(user_commands.user, admin_commands.admin)
    dp.update.outer_middleware(middlewares.banMiddleware())
    await table_actions.create_tables()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try: 
        asyncio.run(main())
    except KeyboardInterrupt: 
        print("Bot was stoped!")
    # except Exception as e: print(e)
