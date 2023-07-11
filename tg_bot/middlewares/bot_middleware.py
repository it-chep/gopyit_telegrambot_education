from telebot import BaseMiddleware, CancelUpdate, SkipHandler
from tg_bot.models import TGUsers, BannedUsers
from tg_bot.repository.repository import Repository


class CustomMiddleware:
    def __init__(self):
        self.repo = TGUsers
        self.cache = Repository()
        self.ban = BannedUsers

    def registration_middleware(self, update):
        if self.cache.redis.get(key=f'phone_{update.from_user.id}'):
            return True
        try:
            self.repo.objects.filter(tg_id=update.from_user.id).get()
            return True
        except:
            return False

    def check_banned(self, update, context=None):
        if self.cache.redis.get(key=f'{update.from_user.id}') is not None:
            return False
        try:
            return self.ban.objects.filter(update.from_user.id).get()
        except:
            return False


class Middleware(BaseMiddleware):

    def __init__(self):
        super().__init__()
        self.middleware = CustomMiddleware()
        self.update_types = ['message', 'callback_query']

    def pre_process(self, message, data):

        if self.middleware.check_banned(message):
            return SkipHandler()

        if message.text == '/start':
            return
        is_registered = self.middleware.registration_middleware(message)
        if not is_registered:
            return SkipHandler()

    def post_process(self, message, data, exception):
        ...
