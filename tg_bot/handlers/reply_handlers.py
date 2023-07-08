from tg_bot.service.markups import ReplyMarkup


def test_reply(message, bot):
    markup = ReplyMarkup()
    reply_markup = markup.get_reply_markup()
    bot.send_message(message.chat.id, 'Нажми на кнопку на клавиатуре', reply_markup=reply_markup)
    return


def test_more_reply(message, bot):
    markup = ReplyMarkup()
    reply_markup = markup.get_more_reply_markups()
    bot.send_message(message.chat.id, 'Нажми на кнопку на клавиатуре', reply_markup=reply_markup)
    return


def answer_test_reply(message, bot):
    bot.send_message(message.chat.id, 'Поймал reply кнопку',)
    return


def test_some_reply(message, bot):
    bot.send_message(message.chat.id, 'Поймал reply кнопку 1',)
    return


def send_number(message, bot):
    markup = ReplyMarkup()
    reply_markup = markup.phone_number_markup()
    bot.send_message(message.chat.id, 'Нажми на кнопку на клавиатуре "Поделиться номером телефона"', reply_markup=reply_markup)
    return


def get_number(message, bot):
    bot.send_message(message.chat.id, 'Поймал мобилу')
    return


def send_geo(message, bot):
    markup = ReplyMarkup()
    reply_markup = markup.geo_markup()
    bot.send_message(message.chat.id, 'Нажми на кнопку на клавиатуре', reply_markup=reply_markup)
    return


def get_geo(message, bot):
    bot.send_message(message.chat.id, 'Знаю твой IP')
    return

