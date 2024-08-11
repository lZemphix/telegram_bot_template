from aiogram import Router, F 
import os 
import logging
from aiogram.types import CallbackQuery
from database.actions import table_actions
from dotenv import load_dotenv
from keyboards.keyboard import KeyboardBuilder
# from aiogram.filters import StateFilter
# from aiogram.fsm.context import FSMContext
# from utils.states import *

logging.basicConfig(level=logging.DEBUG, filename="logs/admin.log", 
                    format="%(asctime)s - %(levelname)s - %(message)s") 

load_dotenv()

admin_uids = os.getenv("ADMIN_UIDS").replace(" ", "").split(",") #list
admin = Router()

@admin.callback_query(F.data == "admin")
async def admin_panel(clb: CallbackQuery):
    await clb.message.delete()
    await clb.message.answer("Выберите нужный вариант", reply_markup=KeyboardBuilder().callback_buttons(recreate_tables="Пересоздать таблицы", main="Главное меню"))
    
@admin.callback_query(F.data == "recreate_tables")
async def create_tables_command(clb: CallbackQuery):
    await table_actions.drop_tables()
    await table_actions.create_tables()
    await clb.message.answer("Таблицы были созданы", reply_markup=KeyboardBuilder().callback_buttons(admin="Админ панель"))

