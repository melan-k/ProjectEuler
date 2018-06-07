import math
def each_primes(upper) :
    assert(upper > 1)
    limit = math.floor(math.sqrt(upper))
    begin = 2
    nums = list(range(begin, upper))
    primes = []
    while begin < limit :
        for num in nums :
            if num % begin == 0 :
                nums.remove(num)
        primes.append(begin)
        begin = nums[0]

    for prime in nums :
        primes.append(prime)

    return primes

def primes_count(upper) :
    return len(each_primes(upper))

def divisors(num) :
    pass

def is_prime(num) :
    return each_primes(num)[-1] == num

def sieve_of_atkin(limit):
    results = [2,3,5]
    sieve = [False]*(limit+1)
    factor = int(math.sqrt(limit))+1
    for i in range(1,factor):
        for j in range(1, factor):
            n = 4*i**2+j**2
            if (n <= limit) and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3*i**2+j**2
            if (n <= limit) and (n % 12 == 7):
                sieve[n] = not sieve[n]
            if i>j:
                n = 3*i**2-j**2
                if (n <= limit) and (n % 12 == 11):
                    sieve[n] = not sieve[n]
    for index in range(5,factor):
        if sieve[index]:
            for jndex in range(index**2, limit, index**2):
                sieve[jndex] = False
    for index in range(7,limit):
        if sieve[index]:
            results.append(index)
    return results

def get_each_primes_till_one_million():
    with open('./lib/primes_1000000.txt', 'r', encoding = 'utf-8') as f :
        return f.read().rstrip().split(',')
