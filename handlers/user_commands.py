from aiogram import Router, F, Bot
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery
from database.database_users import Users
from keyboards.inline import Kb_maker
# from aiogram.fsm.context import FSMContext
# from utils.states import ?
from dotenv import load_dotenv
import os

dotenv_path = os.path.join("data", '.env')
load_dotenv(dotenv_path=dotenv_path)

admin_uids = os.getenv("ADMIN_UIDS").replace(" ", "").split(", ")#list
user: Router = Router()

async def start_message(uid, msg):
    Users().create_db()
    if str(uid) in admin_uids:
        await msg.answer(f"""Привет, {msg.from_user.first_name}!""", reply_markup=Kb_maker().callback_buttons(titles=['кнопка'], callbacks=['button'], rows=2))
    else:
        await msg.answer(f"""Привет, {msg.from_user.first_name}!""", reply_markup=Kb_maker().callback_buttons(titles=['кнопка', '⚙ Админ панель'], callbacks=['button', 'admin'], rows=2))


@user.message(Command("start"))
async def start_command(msg: Message):
    await Users().check_user(msg)
    await start_message(msg.from_user.id, msg)

@user.callback_query(F.data == "main")
async def main_menu(clb: CallbackQuery):
    await Users().check_user(clb)
    await start_message(clb.from_user.id, clb.message)
