from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

class KeyboardBuilder:      

    @staticmethod
    def callback_buttons(*, rows: int = 1, **button_details): 
        """button_details: callback_data=button_title"""  
        __inline_builder = InlineKeyboardBuilder()
        for callback_data, title in button_details.items():
            __inline_builder.button(text=title, callback_data=callback_data)
        return __inline_builder.adjust(rows).as_markup()
    
    @staticmethod
    def url_buttons(*, rows: int = 1, main_button: bool = False, **button_details):
        """button_details: url=button_title"""  
        __inline_builder = InlineKeyboardBuilder()
        for url, title in button_details.items():
            __inline_builder.button(text=title, url=url)
        if main_button:
            __inline_builder.button(text="Главное меню", callback_data="main")
        return __inline_builder.adjust(rows).as_markup()

    @staticmethod
    def reply_buttons(*buttons, 
                     rows: int = 1, 
                     resize_keyboard: bool = None,
                     is_persistent: bool = None,
                     one_time_keyboard: bool = None,
                     input_field_placeholder: str = None,
                     selective: str = None
                     ):
        __reply_builder = ReplyKeyboardBuilder()
        for button in buttons:
            __reply_builder.button(text=button)
        return __reply_builder.adjust(rows).as_markup(resize_keyboard=resize_keyboard, 
                                                           is_persistent=is_persistent,
                                                           one_time_keyboard=one_time_keyboard,
                                                           input_field_placeholder=input_field_placeholder,
                                                           selective=selective)

keyboard = KeyboardBuilder()







