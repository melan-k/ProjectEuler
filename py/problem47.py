from lib.prime import get_prime_factors_list, each_primes

primes = each_primes(1000000)
for num in range(646, 1000000):
    cnt = len(set(get_prime_factors_list(num, primes)))
    if not cnt == 4:
        continue

    cnt = len(set(get_prime_factors_list(num+1, primes)))
    if not cnt == 4:
        continue

    cnt = len(set(get_prime_factors_list(num+2, primes)))
    if not cnt == 4:
        continue

    cnt = len(set(get_prime_factors_list(num+3, primes)))
    if cnt == 4:
        print(num)
        break
