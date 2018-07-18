fizzes = [x if x%3 else "fizz" for x in range(1,50)]
print(fizzes)
fizzes_less_buzzes = [x if x%3 else "fizz" for x in range(1,50) if x%5]
print(fizzes_less_buzzes )

n=100
non_primes = {j for i in range(2,8) for j in range(i*2,n,i)}

primes = [x for x in range(2,n) if x not in non_primes]
print(primes)