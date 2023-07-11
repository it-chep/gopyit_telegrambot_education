from tg_bot.models import AllMessages, TechnicalMessages


class MessageService:

    def __init__(self):
        self.all = AllMessages
        self.tech = TechnicalMessages

    def get_start_message(self) -> str:
        return self.tech.objects.filter(name__contains='Приветственное сообщение').get().text

