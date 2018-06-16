import itertools
import random

for k in itertools.count():
    if all(random.randint(1,6)==2 for _ in range(3)):
        break
print(f"Took {k} tries to get 3 2's")

# for i in itertools.count(1):
#     s = "Fizz" if not i%3 else ""
#     s += "Buzz" if not i%5 else ""
#     s = s if s else str(i)
#     print(s)

# for row_class in itertools.cycle(["even","odd","nothing"]):
#     print(f"I am {row_class}")
#     print(f'<div class="{row_class}">')

# print(list(itertools.combinations(['a','b','c','d'],2)))
# print(list(itertools.permutations("abcd",2)))
# print(list(itertools.product("abc","123")))
# print(list(itertools.product([0,1],repeat=4)))

def my_counter():
    my_number = 1
    while True:
        yield my_number
        my_number = my_number + 1

for i in my_counter():
    print(i)


