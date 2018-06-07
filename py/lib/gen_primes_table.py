from lib.prime import each_primes, sieve_of_atkin

upper = 1000000;
primes = sieve_of_atkin(upper)
filename = "primes_{}.txt".format(str(upper))
with open(filename, 'w', encoding="utf-8") as f:
    for num in primes:
        f.write(str(num) + ', ')

print('finished')
