from tg_bot.repository.repository import Repository


def start(message, bot):
    bot.send_message(message.chat.id, 'Привет заполни свою форму. Напиши email')
    Repository.redis.set(key=f'{message.chat.id}', value='email')
    return


def fork(message, bot):
    print('fork')
    text = ''
    try:
        if message.text:
            text = message.text
        else:
            text = 'Иди гуляй'
    except Exception as e:
        print(f"Error: {e}")
    bot.send_message(message.chat.id, text)
    return
