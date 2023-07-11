from tg_bot.service.markups import ReplyMarkup
from tg_bot.service.users_service import TelegramUserService


def get_number(message, bot):
    TelegramUserService().register_user(message)
    bot.send_message(message.chat.id, 'Записал тебя')
    ReplyMarkup().clean_markup()
    return

# Examples


def reply_handler(message, bot):
    markup = ReplyMarkup()
    reply_markup = markup.universal_reply_markup([
        [('Продлжить', ''), ('Поделиться номером телефона', 'phone'), ('Поделиться местоположением', 'geo')],
        [('Заказать кофе', ''), ('Записаться на онлайн звонок', '')],
        [('Вернуться в начало', '')]
    ])
    bot.send_message(message.chat.id, 'Нажми на кнопку на клавиатуре', reply_markup=reply_markup)
    return


# def get_number(message, bot):
#     bot.send_message(message.chat.id, 'Поймал номер телефона')
#     return


def get_geo(message, bot):
    bot.send_message(message.chat.id, 'Теперь я знаю твой IP')
    return
