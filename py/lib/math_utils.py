import math

def calc_digit(num) :
    if num == 0 :
        return 0
    return int(math.log10(abs(num)) + 1)

def each_num_of_points(num) :
    a = []
    digit = num(calc_digit(num))
    for i in range(digit, 0, -1) :
        num_of_digit = 10 ** (i - 1)
        point = num / num_of_digit
        a.append(point)
        if point != 0 :
            num -= point * num_of_digit

    return a

def comb(n, r):
    assert((type(n)==int) and (type(r)==int))
    assert(n > r)
    return factorial(n) / (factorial(r) * factorial(n - r))
