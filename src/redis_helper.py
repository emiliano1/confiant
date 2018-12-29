import redis

from .env import env


def get_redis():
    """ Return Redis connection """

    return redis.StrictRedis(
        host=env['redis']['host'],
        port=env['redis']['port'],
        db=env['redis']['db'],
        password=env['redis']['auth'],
    )
