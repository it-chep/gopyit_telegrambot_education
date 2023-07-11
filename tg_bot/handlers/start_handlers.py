from tg_bot.service.markups import InlineMarkup, ReplyMarkup
from tg_bot.service.message_service import MessageService
from tg_bot.service.users_service import TelegramUserService
from tg_bot.repository.repository import Repository


def start(message, bot):
    msg = MessageService().get_start_message()
    markup = ReplyMarkup()
    Repository().redis.set(key=f'{message.chat.id}', value='1234')
    reply_markup = markup.universal_reply_markup([
        [('Поделиться номером телефона', 'phone')]
    ])

    bot.send_message(message.chat.id, msg, reply_markup=reply_markup)
    return


def fork(message, bot):
    ...
