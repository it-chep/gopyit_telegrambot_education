from tg_bot.models import TGUsers
from tg_bot.logging import Logger

logger = Logger('TelegramService')


class TelegramUserService:

    def __init__(self):
        self.tg = TGUsers

    def get_user_by_id(self, message):
        try:
            self.tg.objects.filter(tg_id=message.from_user.id).get()
            return True
        except:
            return False

    def register_user(self, message):
        if self.get_user_by_id(message):
            return
        try:
            username = message.from_user.username
        except:
            username = ''

        user = self.tg.objects.create(
            tg_id=message.from_user.id,
            name=message.from_user.first_name + message.from_user.last_name,
            username=username,
            phone=message.contact.phone_number
        )
        user.save()
        logger.info(f'New user tg_id = {message.from_user.id}')
        return

    def update_user_email(self, email, tg_id):
        user = self.tg.objects.get(tg_id=tg_id)
        user.email = email
        user.save()
        logger.info(f'User with tg_id {tg_id} have updated email to {email}')

        return

    def update_user_phone(self, phone, tg_id):
        user = self.tg.objects.get(tg_id=tg_id)
        user.phone = phone
        user.save()
        logger.info(f'User with tg_id {tg_id} have updated phone to {phone}')

        return

    def update_user_name(self, name, tg_id):
        user = self.tg.objects.get(tg_id=tg_id)
        user.name = name
        user.save()
        logger.info(f'User with tg_id {tg_id} have updated name to {name}')

        return user
