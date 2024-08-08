from aiogram import Router, F, Bot 
# from aiogram.filters import StateFilter
from aiogram.types import Message, CallbackQuery
# from database.database import database
# from aiogram.fsm.context import FSMContext
# from utils.states import *
from dotenv import load_dotenv
from keyboards.inline import KeyboardBuilder
import asyncio, os

load_dotenv()

admin_uids = os.getenv("ADMIN_UIDS").replace(" ", "").split(",") #list
admin = Router()

@admin.callback_query(F.data == "admin")
async def admin_panel(clb: CallbackQuery):
    await clb.message.delete()
    await clb.message.answer(f"""Выберите нужеый вариант""", reply_markup=KeyboardBuilder().reply_buttons(b1="Тест", b2="Тест2", b3="Тест3"))