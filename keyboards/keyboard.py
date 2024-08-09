from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

class KeyboardBuilder:
        
    def __init__(self) -> None:
        self.__inline_builder = InlineKeyboardBuilder()
        self.__reply_builder = ReplyKeyboardBuilder()

    def callback_buttons(self, *, rows: int = 1, **button_details): 
        """button_details = callback_data=button_title"""  
        for callback_data, title in button_details.items():
            self.__inline_builder.button(text=title, callback_data=callback_data)
        return self.__inline_builder.adjust(rows).as_markup()

    def url_buttons(self, *, rows: int = 1, main_button: bool = False, **button_details):
        """button_details = url=button_title"""  
        for url, title in button_details.items():
            self.__inline_builder.button(text=title, url=url)
        if main_button:
            self.__inline_builder.button(text="Главное меню", callback_data="main")
        return self.__inline_builder.adjust(rows).as_markup()

    def callback_main_button(self):    
        self.__inline_builder.button(text="Главное меню", callback_data="main")
        return self.__inline_builder.as_markup()
    
    def reply_buttons(self, *buttons, 
                     rows: int = 1, 
                     resize_keyboard: bool = None,
                     is_persistent: bool = None,
                     one_time_keyboard: bool = None,
                     input_field_placeholder: str = None,
                     selective: str = None
                     ):
        for button in buttons:
            self.__reply_builder.button(text=button)
        return self.__reply_builder.adjust(rows).as_markup(resize_keyboard=resize_keyboard, 
                                                           is_persistent=is_persistent,
                                                           one_time_keyboard=one_time_keyboard,
                                                           input_field_placeholder=input_field_placeholder,
                                                           selective=selective)









