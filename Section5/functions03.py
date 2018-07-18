def double(wrapped_fn):
    def inner_function(*args,**kwargs):
        results = wrapped_fn(*args,**kwargs)
        return [results,results]
    return inner_function

@double
@double
@double
def hello():
    return "hello"
import time
def profile_me(wrapped_fn):
    def inner_fn(*args,**kwargs):
        start_time = time.time()
        result = wrapped_fn(*args,**kwargs)
        print(f"{time.time()-start_time:0.3f}s - {wrapped_fn.__name__}(*{args},**{kwargs})")
        return result
    return inner_fn


def memoize_me(wrapped_fn):
    local_cache = {}
    def inner_fn(*args,**kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key not in local_cache:
            local_cache[key] = wrapped_fn(*args,**kwargs)
        return local_cache[key]
    return inner_fn

@profile_me
@memoize_me
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

x = fib(30)
print(x)