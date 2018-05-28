import math

pandigital = []
def to_pandigital_num(a) :
    digit = len(a)
    sum_ = 0
    for i in a :
        digit -= 1
        sum_ += i * (10 ** digit)
    return sum_

def each_pandigital(digit, a_=[]) :
    assert(digit > 0 and digit < 10)
    global pandigital

    a = a_
    for i in range(1, digit + 1) :
        if i in a :
            continue
        a.append(i)
        each_pandigital(digit, a)
        if len(a) == digit :
            pandigital.append(to_pandigital_num(a))

print(each_pandigital(3))
