import time
import random


def is_prime(x):
    for i in range(2,int(x**0.5)+1,1):
        if x%i == 0:
            return False
    return True

