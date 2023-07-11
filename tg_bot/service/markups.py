from typing import Optional, List, Tuple
from tg_bot.bot_configure.markups import *


class ReplyMarkup:

    def __init__(self):
        self.markup = CustomReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    def universal_reply_markup(self, buttons: Optional[List[List[Tuple[str, str]]]]) -> CustomReplyKeyboardMarkup:
        """
        :param buttons:
        :return: markup

        buttons = [
            [('Текст1', ''), ('Текст2', 'phone')],
            [('Текст3', 'geo'), ('Текст 4', '')],
        ]

        В наружном массиве подаются все кнопки, во внутреннем массиве указываются кнопки в строке
        """

        btns = []

        for i in buttons:
            for j in i:
                btn_type = j[1].lower()
                if btn_type == 'phone':
                    btns.append(CustomKeyboardButton(j[0], request_contact=True))
                elif btn_type == 'geo':
                    btns.append(CustomKeyboardButton(j[0], request_location=True))
                else:
                    btns.append(CustomKeyboardButton(j[0]))
            self.markup.add(*btns)
            btns = []

        return self.markup

    def clean_markup(self):
        self.markup.keyboard.clear()
        return self.markup


class InlineMarkup:

    def __init__(self):
        self.markup = CustomInlineKeyboardMarkup()

    def universal_inline_markup(self, buttons: Optional[List[List[Tuple[str, str, str]]]]):
        """
            :param buttons:
            :return: markup

            buttons = [
                [('Текст1', 'data', 'type' ), ('Текст2', 'https://google.com', 'url')],
                [('Текст3', 'data', 'type'), ('Текст 4', 'https://google.com', 'web_app')],
            ]

            В наружном массиве подаются все кнопки, во внутреннем массиве указываются кнопки в строке
        """
        btns = []

        for i in buttons:
            for j in i:
                btn_type = j[2].lower()
                if btn_type == 'url':
                    btns.append(CustomInlineKeyboardButton(text=j[0], url=j[1]))
                elif btn_type == 'web_app':
                    btns.append(CustomInlineKeyboardButton(text=j[0], web_app=j[1]))
                else:
                    btns.append(CustomInlineKeyboardButton(text=j[0], callback_data=j[1]))

            self.markup.add(*btns)
            btns = []
        return self.markup
