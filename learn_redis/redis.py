from redis import Redis


def inc_redis_str(redis_host, redis_port, redis_key):
    r = Redis(host=redis_host, port=redis_port)

    if not r.get(redis_key):
        r.set(redis_key, 0)
    request_cnt = r.get(redis_key)
    r.set(redis_key, int(request_cnt) + 1)
    r.expire(redis_key, 3 * 24 * 3600)
