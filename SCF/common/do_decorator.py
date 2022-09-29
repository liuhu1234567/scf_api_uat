import time


class Timer:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        ret = self.func(*args, **kwargs)
        print(f'Time:{time.time() - start}')
        return ret


@Timer
def add(a, b):
    time.sleep(1)
    return a + b


print(add(2, 3))
