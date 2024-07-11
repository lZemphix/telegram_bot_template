from aiogram import Router, F, Bot 
# from aiogram.filters import StateFilter
from aiogram.types import Message, CallbackQuery
# from database.database import database
from keyboards.inline import Kb_maker
# from aiogram.fsm.context import FSMContext
# from utils.states import *
from dotenv import load_dotenv
import asyncio, os

dotenv_path = os.path.join("data", '.env')
load_dotenv(dotenv_path=dotenv_path)

admin_uids = os.getenv("ADMIN_UIDS").replace(" ", "").split(", ") #list
admin: Router = Router()

@admin.callback_query(F.data == "admin")
async def admin_panel(clb: CallbackQuery):
    await clb.message.delete()
    await clb.message.answer(f"""Выберите нужеый вариант""", reply_markup = Kb_maker().callback_buttons(["Очистить базу данных", "Добавить пользователя", "Бан пользователя"],["clear_db", "add_user", "ban_user"]))

