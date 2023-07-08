from tg_bot.cache import RedisCache


class Repository:

    redis = RedisCache('redis://localhost:6379/1', {})

