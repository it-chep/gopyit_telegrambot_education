import telebot
from django.conf import settings
from django.core.management import BaseCommand
from tg_bot.bot_configure.bot import Bot
from telebot import apihelper

from tg_bot.service.users_service import TelegramUserService
from .states import StateForm

from tg_bot.handlers.reply_handlers import *
from tg_bot.handlers.inline_handlers import *
from tg_bot.handlers.content_type_handlers import *
from ...handlers.start_handlers import *
from tg_bot.middlewares.bot_middleware import Middleware

apihelper.ENABLE_MIDDLEWARE = True

bot = Bot(token=settings.BOT_TOKEN, use_class_middlewares=True)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        while True:
            try:
                bot.setup_middleware(Middleware())
                print('Bot Online')
                bot.infinity_polling()

            except Exception as e:
                print(e)


bot.register_message_handler(lambda message: start(message, bot), commands=['start'])


# Education

bot.register_message_handler(lambda message: reply_handler(message, bot), commands=['reply'])

bot.register_message_handler(lambda message: get_number(message, bot), content_types=['contact'])


bot.register_message_handler(lambda message: get_geo(message, bot), content_types=['location'])

bot.register_message_handler(lambda message: get_inline_markup(message, bot), commands=['inline'])

bot.register_callback_query_handler(
    lambda callback: reaction_on_inline_button(callback, bot),
    lambda callback_query: callback_query.data == "btn1",
)

bot.register_message_handler(lambda message: send_photo(message, bot), content_types=['photo'])
bot.register_message_handler(lambda message: send_voice(message, bot), content_types=['voice'])
bot.register_message_handler(lambda message: send_voice_note(message, bot), content_types=['video_note'])
bot.register_message_handler(lambda message: send_video(message, bot), content_types=['video'])
bot.register_message_handler(lambda message: send_sticker(message, bot), content_types=['sticker'])
bot.register_message_handler(lambda message: send_document(message, bot), content_types=['document'])

bot.register_message_handler(lambda message: new_chat_member(message, bot), content_types=['new_chat_members'])
bot.register_message_handler(lambda message: left_chat_member(message, bot), content_types=['left_chat_member'])


bot.register_message_handler(lambda message: fork(message, bot), content_types=['text'])

