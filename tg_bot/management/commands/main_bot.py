from django.conf import settings
from django.core.management import BaseCommand
import telebot
from tg_bot.service.users_service import TelegramUserService
from .states import StateForm

from tg_bot.handlers.reply_handlers import *
from tg_bot.handlers.inline_handlers import *
from tg_bot.handlers.content_type_handlers import *
from ...handlers.start_handlers import *

bot = telebot.TeleBot(settings.BOT_TOKEN)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        while True:
            try:
                print('Bot Online')
                bot.polling()
            except Exception as e:
                print(e)


bot.register_message_handler(lambda message: start(message, bot), commands=['start'])

bot.register_message_handler(lambda message: test_reply(message, bot), commands=['reply'])
bot.register_message_handler(lambda message: test_more_reply(message, bot), commands=['more_reply'])

bot.register_message_handler(lambda message: answer_test_reply(message, bot), regexp='Привет, держи reply кнопку')
bot.register_message_handler(lambda message: test_some_reply(message, bot), regexp='Привет, держи reply кнопку 1')


bot.register_message_handler(lambda message: send_number(message, bot), commands=['phone'])
bot.register_message_handler(lambda message: get_number(message, bot), content_types=['contact'])


bot.register_message_handler(lambda message: send_geo(message, bot), commands=['geo'])
bot.register_message_handler(lambda message: get_geo(message, bot), content_types=['location'])

bot.register_message_handler(lambda message: get_inline_markup(message, bot), commands=['inline'])
bot.register_message_handler(lambda message: get_more_inline_markup(message, bot), commands=['more_inline'])

bot.register_callback_query_handler(
    lambda callback_query: callback_query.data == "btn1",
    lambda callback: reaction_on_inline_button(callback, bot)
)

bot.register_callback_query_handler(
    lambda callback_query: callback_query.data == "btn2",
    lambda callback: reaction_some_inline_button(callback, bot)
)

bot.register_message_handler(lambda message: get_url_markup(message, bot), commands=['url'])

bot.register_message_handler(lambda message: send_photo(message, bot), content_types=['photo'])
bot.register_message_handler(lambda message: send_voice(message, bot), content_types=['voice'])
bot.register_message_handler(lambda message: send_voice_note(message, bot), content_types=['video_note'])
bot.register_message_handler(lambda message: send_video(message, bot), content_types=['video'])
bot.register_message_handler(lambda message: send_sticker(message, bot), content_types=['sticker'])
bot.register_message_handler(lambda message: send_document(message, bot), content_types=['document'])

bot.register_message_handler(lambda message: new_chat_member(message, bot), content_types=['new_chat_members'])
bot.register_message_handler(lambda message: left_chat_member(message, bot), content_types=['left_chat_member'])


bot.register_message_handler(lambda message: fork(message, bot))

