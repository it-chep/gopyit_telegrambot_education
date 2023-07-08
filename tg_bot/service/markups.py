from telebot import types


class ReplyMarkup:

    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    def get_reply_markup(self):
        self.markup.add('Привет, держи reply кнопку')
        return self.markup

    def get_more_reply_markups(self):
        self.markup.add('Привет, держи reply кнопку 1')
        self.markup.add('Привет, держи reply кнопку 2')
        self.markup.add('Привет, держи reply кнопку 3')
        self.markup.add('Привет, держи reply кнопку 4')
        self.markup.add('Привет, держи reply кнопку 5')
        self.markup.add('Привет, держи reply кнопку 6')
        return self.markup

    def phone_number_markup(self):
        phone_button = types.KeyboardButton(text="Поделиться номером телефона", request_contact=True)
        self.markup.add(phone_button)
        return self.markup

    def geo_markup(self):
        geo_button = types.KeyboardButton(text="Поделиться геолокацией", request_location=True)
        self.markup.add(geo_button)
        return self.markup

    def clean_markup(self):
        self.markup.keyboard.clear()
        return self.markup


class InlineMarkup:

    def __init__(self):
        self.markup = types.InlineKeyboardMarkup(row_width=5)

    def get_inline_markup(self):
        btn = types.InlineKeyboardButton('Первая inline кнопка', callback_data='btn1')
        self.markup.add(btn)
        return self.markup

    def get_more_inline_markup(self):
        btn1 = types.InlineKeyboardButton('1', callback_data='btn1')
        btn2 = types.InlineKeyboardButton('2', callback_data='btn2')
        btn3 = types.InlineKeyboardButton('3  ', callback_data='btn3')
        btn4 = types.InlineKeyboardButton('4', callback_data='btn4')
        btn5 = types.InlineKeyboardButton('5', callback_data='btn5')

        self.markup.add(btn1, btn2, btn3, btn4, btn5)
        return self.markup

    def url_markup(self):
        btn_with_url = types.InlineKeyboardButton('Ссылка на канал GOPYIT',
                                                  url='https://www.youtube.com/watch?v=_Guix7ZKa1Q&t=19s')

        self.markup.add(btn_with_url)
        return self.markup
