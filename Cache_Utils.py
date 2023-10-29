from pymemcache.client import base

client = base.Client(('localhost', 11211))


def cache(fun):
    def wrapper(n):
        result = client.get(str(n))
        if result is None:
            result = fun(n)
            client.set(str(n), str(result))
        return int(result)
    return wrapper
