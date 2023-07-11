from typing import Optional

from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, WebAppInfo, \
    KeyboardButtonRequestChat, KeyboardButtonRequestUser, KeyboardButtonPollType, ReplyKeyboardMarkup


class CustomReplyKeyboardMarkup(ReplyKeyboardMarkup):
    def __init__(self, resize_keyboard: Optional[bool] = None, one_time_keyboard: Optional[bool] = None,
                 selective: Optional[bool] = None, row_width: int = 3,
                 input_field_placeholder: Optional[str] = None, is_persistent: Optional[bool] = None):
        super().__init__(resize_keyboard, one_time_keyboard, selective, row_width, input_field_placeholder, is_persistent)

    def add(self, *args, row_width=None):
        return super().add(*args, row_width=row_width)

    def row(self, *args):
        return super().row(*args)

    def to_json(self):
        return super().to_json()


class CustomKeyboardButton(KeyboardButton):
    def __init__(self, text: str, request_contact: Optional[bool] = None,
                 request_location: Optional[bool] = None, request_poll: Optional[KeyboardButtonPollType] = None,
                 web_app: Optional[WebAppInfo] = None, request_user: Optional[KeyboardButtonRequestUser] = None,
                 request_chat: Optional[KeyboardButtonRequestChat] = None):
        super().__init__(text, request_contact, request_location, request_poll, web_app, request_user, request_chat)

    def to_json(self):
        return super().to_json()

    def to_dict(self):
        return super().to_dict()


class CustomInlineKeyboardMarkup(InlineKeyboardMarkup):
    def __init__(self, keyboard=None, row_width=3):
        super().__init__(keyboard, row_width)

    def add(self, *args, row_width=None):
        return super().add(*args, row_width=row_width)

    def row(self, *args):
        return super().row(*args)

    def to_json(self):
        return super().to_json()

    def to_dict(self):
        return super().to_dict()


class CustomInlineKeyboardButton(InlineKeyboardButton):
    @classmethod
    def de_json(cls, json_string):
        return super().de_json(json_string)

    def __init__(self, text, url=None, callback_data=None, web_app=None, switch_inline_query=None,
                 switch_inline_query_current_chat=None, switch_inline_query_chosen_chat=None, callback_game=None,
                 pay=None, login_url=None, **kwargs):
        super().__init__(text, url, callback_data, web_app, switch_inline_query, switch_inline_query_current_chat,
                         switch_inline_query_chosen_chat, callback_game, pay, login_url, **kwargs)

    def to_json(self):
        return super().to_json()

    def to_dict(self):
        return super().to_dict()