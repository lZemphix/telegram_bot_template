from aiogram import Router, F, Bot 
# from aiogram.filters import StateFilter
from aiogram.types import Message, CallbackQuery
from database.actions import *
# from aiogram.fsm.context import FSMContext
# from utils.states import *
from dotenv import load_dotenv
from keyboards.keyboard import KeyboardBuilder
import os, logging

logging.basicConfig(level=logging.DEBUG, filename="logs/admin.log", format="%(asctime)s - %(levelname)s - %(message)s") 

load_dotenv()

admin_uids = os.getenv("ADMIN_UIDS").replace(" ", "").split(",") #list
admin = Router()

@admin.callback_query(F.data == "admin")
async def admin_panel(clb: CallbackQuery):
    await clb.message.delete()
    await clb.message.answer(f"""Выберите нужный вариант""", reply_markup=KeyboardBuilder().callback_buttons(recreate_tables="Пересоздать таблицы", main="Главное меню"))
    
@admin.callback_query(F.data == "recreate_tables")
async def create_tables_command(clb: CallbackQuery):
    await drop_tables()
    await create_tables()
    await clb.message.answer(f"""Таблицы были созданы""", reply_markup=KeyboardBuilder().callback_buttons(admin="Админ панель"))

