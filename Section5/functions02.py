six = (lambda x:x+1)(5)
f = lambda x:x+1
f(5), f(6), f(7)

sqrt = lambda x:x**0.5

print(sqrt(25))

def sqrt(x):
    return x**0.5

from random import randint
squares = map(lambda x:x**2,range(1,11))
randoms = map(lambda _:randint(1,150), range(100))
gt_100 = filter(lambda x: x>100, randoms)
print(list(gt_100))


import time
import threading
import functools
if __name__ == "__main__":
    for delay,value in enumerate(["one","two","three"],1):
        threading.Timer(delay, functools.partial(print,value)).start()
    time.sleep(4)

def test(a,b,c,d):
    print(f"a={a}, b={b}, c={c}, d={d}")

p=functools.partial(test,2,3,d=22)
p(56)