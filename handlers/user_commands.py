from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.keyboard import keyboard
from database.actions import users_actions
from dotenv import load_dotenv
import os
import logging
# from aiogram.fsm.context import FSMContext
# from utils.states import ?

load_dotenv()

admin_uids: list[int] = os.getenv("ADMIN_UIDS").replace(" ", "").split(",") #list
user = Router()

async def start_message(uid, message, username):
    if ~(await users_actions.check_user(uid)):
        await users_actions.add_user(username=username, uid=uid)
    await message.answer(f'Привет, {username}!', reply_markup=keyboard.callback_buttons(main='Главное меню'))

@user.message(Command("start"))
async def start_command(message: Message):
    await start_message(message.from_user.id, message, message.from_user.username)

@user.callback_query(F.data == "main")
async def main_menu(callback: CallbackQuery):
    await start_message(callback.from_user.id, callback.message, callback.from_user.username)
