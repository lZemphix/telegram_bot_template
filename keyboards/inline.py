from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

    

class KeyboardBuilder:

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
        
    def __init__(self) -> None:
        self.__inline_builder = InlineKeyboardBuilder()
        self.__reply_builder = ReplyKeyboardBuilder()

    def callback_buttons(self, *, rows: int = 1, **button_details):   
        for title, callback_data in button_details.items():
            self.__inline_builder.button(text=title, callback_data=callback_data)
        return self.__inline_builder.adjust(rows).as_markup()

    def url_buttons(self, *, rows: int = 1, main_button: bool = False, **button_details):
        for title, url in button_details.items():
            self.__inline_builder.button(text=title, url=url)
        if main_button:
            self.__inline_builder.button(text="Главное меню", callback_data="main")
        return self.__inline_builder.adjust(rows).as_markup()

    def callback_main_button(self):    
        self.__inline_builder.button(text="Главное меню", callback_data="main")
        return self.__inline_builder.as_markup()
    
    def reply_buttons(self, **buttons):
        for name, titles in buttons:
            self.__reply_builder.button(text=titles)
        return self.__reply_builder.adjust().as_markup(resize_keyboard=True)









