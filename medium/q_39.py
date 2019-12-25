def fib_recur(n):
    assert n >= 0, "n > 0"
    if n <= 1:
        return n
    return fib_recur(n - 1) + fib_recur(n - 2)


for i in range(1, 20):
    print(fib_recur(i), end=' ')

gt = (str(i) for i in range(10))
print("".join(gt, ))

from collections import namedtuple

City = namedtuple("City", "name age")

ck = City("gc", 23)
print(ck.name)