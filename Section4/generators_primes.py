import time

from Section4.future_functions import is_prime

start_time = time.time()
primes = (x for x in range(1000000,1200000) if is_prime(x))

print("Primes:",primes)
print(f"Took {time.time()-start_time:0.2f} seconds")

kept_primes = []
for prime in primes:
    if input(f"keep {prime}?").lower().startswith("y"):
        kept_primes.append(prime)
        if len(kept_primes) >= 4:
            break
print("Keeping",kept_primes)
