from tg_bot.service.markups import InlineMarkup


def get_inline_markup(message, bot):
    markup = InlineMarkup()
    reply_markup = markup.universal_inline_markup([[('Забить время на консультацию', 'online_entry', ''),
                                                    ('Позвать техподдержку', 'tech_support', '')],
                                                   [('YouTube', 'https://www.youtube.com/@gopai_it', 'url')]])
    bot.send_message(message.chat.id, 'Вся важная информация тут', reply_markup=reply_markup)
    return


def reaction_on_inline_button(callback, bot):
    bot.send_message(callback.message.chat.id, 'Отработала первая кнопка')
    print(callback.data)
    return


def reaction_some_inline_button(callback, bot):
    bot.send_message(callback.message.chat.id, 'Отработала вторая кнопка')
