from datetime import datetime


def timeit(func):
    def wrapper():
        start = datetime.now()
        res = func()
        print(datetime.now() - start)
        return res

    return wrapper


c = []


@timeit
def one():
    c = [i for i in range(10_001) if i % 2 == 0]
    return c


@timeit
def two():
    for i in range(10_001):
        if i % 2 == 0:
            c.append(i)
    return c


print(one()[-5:])
print(one()[-5:])
