from aiogram import Router, F
import os 
import logging
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from database.actions import table_actions
from dotenv import load_dotenv
from keyboards.keyboard import keyboard
# from utils.states import *

load_dotenv()
logging.basicConfig(level=logging.DEBUG, filename="logs/admin.log", 
                    format="%(asctime)s - %(levelname)s - %(message)s") 


admin_uids = os.getenv("ADMIN_UIDS").replace(" ", "").split(",") #list
admin = Router()


@admin.message(Command('admin'))
async def admin_panel(message: Message):
    if str(message.from_user.id) in admin_uids:
        await message.delete()
        await message.answer("Выберите нужный вариант", reply_markup=keyboard.callback_buttons(recreate_tables="Пересоздать таблицы", main="Главное меню"))
    else:
        await message.answer('Недостаточно прав!')
        
@admin.callback_query(F.data == "recreate_tables")
async def create_tables_command(callback: CallbackQuery):
    await table_actions.drop_tables()
    await table_actions.create_tables()
    await callback.message.answer("Таблицы были созданы", reply_markup=keyboard.callback_buttons(admin="Админ панель"))

