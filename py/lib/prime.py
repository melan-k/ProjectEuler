from math import sqrt

def each_primes(upper) :
    return sieve_of_eratosthenes(upper)

def get_primes_factors(num):
    primes = each_primes(10000)
    value = num
    idx = 0
    factors = {}
    while(True):
        if value % primes[idx] == 0:
            value /= primes[idx]
            key = str(primes[idx])
            if key not in factors.keys():
                factors[key] = 1
            else:
                factors[key] += 1
        else:
            idx += 1

        if primes[0] > value or value == 1:
            break

    return factors  # prime factors dictionary {"factor":count}

def primes_count(upper) :
    return len(each_primes(upper))

def get_divisors(num, except_self=False):
    if num < 1:
        return []
    elif num == 1:
        return [1]
    else:
        divisor_list = []
        divisor_list.append(1)
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                divisor_list.append(i)
        if except_self:
            divisor_list.append(num)

        return divisor_list

def is_prime(num) :
    return each_primes(num)[-1] == num

def number_of_primes(n_list, upper=10000):
    assert(type(n_list) == list and type(n_list[0]) == int)
    count = 0
    primes = get_each_primes_till_xx(upper)
    for n in n_list:
        if n in primes:
            count += 1
    print("{} : {}".format(n_list[0], count))
    return count

def sieve_of_atkin(limit):
    results = [2,3,5]
    sieve = [False]*(limit+1)
    factor = int(sqrt(limit))+1
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

# Eratosthenesの篩により、整数upper未満の素数を列挙する
# 参考：高橋直大『最強最速アルゴリズマー養成講座』pp.410-412
def sieve_of_eratosthenes(upper, typecode="L"):
    import array
    import textwrap

    assert upper > 1
    # 整数iが素数であるかをis_prime[i]が示す
    # 最初はすべてTrueで初期化しておく
    # 最終的にprimesではなくこれを返してもよい
    is_prime = array.array("B", (True for i in range(upper)))
    # 0, 1はいずれも素数ではない
    is_prime[0] = False
    is_prime[1] = False
    # 素数を格納する配列
    primes = array.array(typecode)
    # 篩う
    for i in range(2, upper):
        if is_prime[i]:  # iが素数であるとき
            primes.append(i)  # 素数の配列に加える
            for j in range(2 * i, upper, i):  # iを超えるiの倍数について
                is_prime[j] = False  # 素数ではないため除外する
    return primes

def get_each_primes_till_xx(num):
    filename = './lib/primes_' + str(num) + '.txt'
    with open(filename, 'r', encoding = 'utf-8') as f :
        return [int(n) for n in f.read().rstrip().split(',')[:-1]]

print(get_primes_factors(12))
