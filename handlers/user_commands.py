from aiogram import Router, F, Bot
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery, User
from keyboards.keyboard import KeyboardBuilder
# from aiogram.fsm.context import FSMContext
# from utils.states import ?
from database.actions import users_actions, table_actions
from dotenv import load_dotenv
import os, logging

load_dotenv()
logging.basicConfig(level=logging.DEBUG, filename="logs/user_commands.log", format="%(asctime)s - %(levelname)s - %(message)s")

admin_uids: list[int] = os.getenv("ADMIN_UIDS").replace(" ", "").split(",") #list
user = Router()


async def start_message(uid, msg, username):
    try:
       (await users_actions.check_user(uid))[0]
    except:
        await users_actions.add_user(username, uid)
    if uid in admin_uids:
        await msg.answer(f"""Привет, {username}! """)
    else:
        await msg.answer(f"""Привет, {username}!""", reply_markup=KeyboardBuilder().callback_buttons(rows=1, admin="Админ панель"))

@user.message(Command("start"))
async def start_command(msg: Message):
    await start_message(msg.from_user.id, msg, msg.from_user.username)

@user.callback_query(F.data == "main")
async def main_menu(clb: CallbackQuery):
    await start_message(clb.from_user.id, clb.message, clb.from_user.username)
