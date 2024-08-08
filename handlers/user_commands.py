from aiogram import Router, F, Bot
from aiogram.filters import Command, StateFilter
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message, CallbackQuery
from keyboards.inline import KeyboardBuilder
# from aiogram.fsm.context import FSMContext
# from utils.states import ?
from dotenv import load_dotenv
import os

load_dotenv()

admin_uids: list[int] = os.getenv("ADMIN_UIDS").replace(" ", "").split(",") #list
user = Router()


async def start_message(uid, msg):
    # Users().create_db()
    if uid in admin_uids:
        await msg.answer(f"""Привет, {msg.from_user.first_name}! """)
    else:
        
        await msg.answer(f"""Привет, {msg.from_user.first_name}!""", reply_markup=KeyboardBuilder().callback_buttons(rows=1, **{"Админ панель": "admin"}))

@user.message(Command("start"))
async def start_command(msg: Message):
    await start_message(msg.from_user.id, msg)

@user.callback_query(F.data == "main")
async def main_menu(clb: CallbackQuery):
    await start_message(clb.from_user.id, clb.message)
