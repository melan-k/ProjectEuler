# -*- coding: utf-8 -*-

from lib.prime import get_each_primes_till_one_million
from lib.calc_digit import calc_digit

primes = get_each_primes_till_one_million()

def get_circular_nums(num):
    route = list(num)
    route_ = route[:]
    row = []
    box = route_
    row.append(box)
    for node in range(len(route)-1):
       row.append(box)
       row[node+1] = row[node][:]
       row[node+1].append(row[node][0])
       row[node+1].pop(0)

    cnums = []
    for elem in row:
        sum = 0
        for idx, c in enumerate(elem):
            sum += int(c) * 10 ** (len(elem) - (idx + 1))
        cnums.append(sum)
    return cnums

circular_primes = []
for prime in primes:
    circular_nums = get_circular_nums(prime)
    f = True
    for circular_num in circular_nums:
        if str(circular_num) not in primes:
            f = False
            break
    if f:
        circular_primes.append(prime)

print(len(circular_primes))
