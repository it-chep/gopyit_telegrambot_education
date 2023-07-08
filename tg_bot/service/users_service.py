from tg_bot.models import TGUsers


class TelegramUserService:

    def __init__(self):
        pass

    def update_user_email(self, email, tg_id):
        user = TGUsers.objects.get(tg_id=tg_id)
        user.email = email
        user.save()

        return

    def update_user_phone(self, phone, tg_id):
        user = TGUsers.objects.get(tg_id=tg_id)
        user.phone = phone
        user.save()

        return

    def update_user_name(self, name, tg_id):
        user = TGUsers.objects.get(tg_id=tg_id)
        user.name = name
        user.save()

        return user
