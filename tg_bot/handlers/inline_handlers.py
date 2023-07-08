from tg_bot.service.markups import InlineMarkup


def get_inline_markup(message, bot):
    markup = InlineMarkup()
    reply_markup = markup.get_inline_markup()
    bot.send_message(message.chat.id, 'Держи кнопки в тексте', reply_markup=reply_markup)
    return


def get_more_inline_markup(message, bot):
    markup = InlineMarkup()
    reply_markup = markup.get_more_inline_markup()
    bot.send_message(message.chat.id, 'Держи больше кнопок в тексте', reply_markup=reply_markup)
    return


def reaction_on_inline_button(callback, bot):
    bot.send_message(callback.message.chat.id, 'Отработала первая кнопка')


def reaction_some_inline_button(callback, bot):
    bot.send_message(callback.message.chat.id, 'Отработала вторая кнопка')


def get_url_markup(message, bot):
    markup = InlineMarkup()
    reply_markup = markup.url_markup()
    bot.send_message(message.chat.id, 'А вот и ссылка в тексте', reply_markup=reply_markup)
    return
