from lib.prime import get_each_primes_till_xx

primes = get_each_primes_till_xx(1000000)
max_chain = 1
for idx, prime in enumerate(primes):
    tmp = prime
    chain = 1
    for i in range(idx+1, len(primes)):
        # print("tmp += {} + {}".format(tmp, primes[i]))
        tmp += primes[i]
        if tmp >= 1000000:
            break
        chain += 1
        if chain > max_chain and tmp in primes:
            print("{}start => {} : {}".format(prime, tmp, chain))
            max_chain = chain

print(max_chain)
