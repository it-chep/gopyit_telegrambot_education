from tg_bot.service.functional_service import FunctionalService


functions = FunctionalService()


def send_photo(message, bot):
    bot.send_message(message.chat.id, 'Фото говно (')
    functions.save_photo(message, bot)

    return


def send_voice(message, bot):
    bot.send_message(message.chat.id, 'Послушал твое аудио, полный отстой (')
    return


def send_voice_note(message, bot):
    bot.send_message(message.chat.id, 'Кружок - Говно (')
    return


def send_video(message, bot):
    bot.send_message(message.chat.id, 'Ну ты и урод (')
    return


def send_sticker(message, bot):
    stick_id = message.sticker.file_id
    bot.send_message(message.chat.id, 'Фуууу, что за говно')
    bot.send_sticker(message.chat.id, stick_id)
    return


def send_document(message, bot):
    bot.send_message(message.chat.id, 'Принял твой документ')
    return


def new_chat_member(message, bot):
    bot.delete_message(message.chat.id, message_id=message.id)
    bot.send_message(message.chat.id, 'Привет новичкам')
    return


def left_chat_member(message, bot):
    bot.delete_message(message.chat.id, message_id=message.id)
    bot.send_message(message.chat.id, 'Пока пока добрый воин')
    bot.send_message(message.from_user.id, 'Чего ушел?')
    return
