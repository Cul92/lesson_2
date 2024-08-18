numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for is_primes in numbers:
    if is_primes > 1:
        for i in range(2, is_primes):
            if (is_primes % i) == 0:
                not_primes.append(is_primes)
                break
        else:
            primes.append(is_primes)
print(primes)
print(not_primes)
