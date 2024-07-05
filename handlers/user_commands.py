from aiogram import Router, F, Bot
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery
from database.database import Users
from keyboards.inline import Kb_maker
# from aiogram.fsm.context import FSMContext
# from utils.states import ?
from dotenv import load_dotenv
import os

dotenv_path = os.path.join("data", '.env')
load_dotenv(dotenv_path=dotenv_path)

admin_uids = os.getenv("ADMIN_UID") #list
user: Router = Router()

@user.message(Command("start"))
async def start_message(msg: Message):
    Users().create_db()
    user_exists = Users.cursor.execute(f"SELECT * FROM users WHERE uid = {msg.from_user.id}").fetchone()
    if user_exists:
        pass
    else:
        Users.cursor.execute(f"INSERT INTO users (uid, username) VALUES ({msg.from_user.id}, '{msg.from_user.username}')")
    Users().save()
    
    buttons, callbacks = ['Кнопка'],['button']
    
    if msg.from_user.id in admin_uids:
        buttons.append('⚙ Админ панель')
        callbacks.append('admin')
    
    await msg.answer(f"""Привет, {msg.from_user.first_name}!""", reply_markup=Kb_maker().callback_buttons(titles=buttons, callbacks=callbacks, rows=2))
