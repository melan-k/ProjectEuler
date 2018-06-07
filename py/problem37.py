from lib.prime import get_each_primes_till_one_million

def trunc_to_left(str_prime):
    str = list(str_prime)
    a = []
    for idx, c in enumerate(str):
        if idx == 0:
            a.append(c)
        else:
            a.append(a[idx - 1] + c)
    return a

def trunc_to_right(str_prime):
    str = list(str_prime)
    a = []
    for idx, c in enumerate(str):
        if idx == 0:
            a.append(str[-1])
        else:
            a.append(str[-1 - idx] + a[idx - 1])
    return a

primes = get_each_primes_till_one_million()
sum = 0
for prime in primes:
    f = False;
    trancated = []

    if int(prime) > 1000000:
        break
    if prime[0] in ["1", "4", "6", "8", "9"]:   # non-prime single digit number
        continue
    if prime[-1] in ["1", "9"]: # odd and non-prime number
        continue;

    trancated = trunc_to_left(prime)
    for t_prime in trancated:
        if t_prime not in primes:
            f = True
            break
    if f:       # filtering...
        continue

    trancated = trunc_to_right(prime)
    for t_prime in trancated:
        if t_prime not in primes:
            f = True
            break

    if not f and int(prime) > 10:
        sum += int(prime)

print(sum)
