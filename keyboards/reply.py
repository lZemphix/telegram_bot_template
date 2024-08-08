from aiogram.utils.keyboard import ReplyKeyboardBuilder


# DONT WORK!!!


class Kb_maker:
    def __init__(self) -> None:
        self.builder = ReplyKeyboardBuilder()
    
    def main_button(self):
        self.builder.button(text="Главное меню", callback_data='main')
        return self.builder.as_markup()
    
    def buttons(self, title: str, rows = 1, main_button = True):
        self.builder.button(text=title)
        if main_button == True:
            self.builder.button(text="Главное меню")
        return self.builder.adjust(rows).as_markup()
