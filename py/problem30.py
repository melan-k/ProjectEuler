import math

def calc_digit(num) :
    if num == 0 :
        return 0
    return math.floor(math.log10(abs(num)) + 1)

def calc_digit_value(value, num) :
    if num > 1 :
        return int(value / (10 ** (num - 1)))
    else :
        return value

a = []
start = 2
values= range(start, 200000)
sum_ = 0
for index,value in enumerate(values, start=start) :
    digit_num = calc_digit(value)
    sum_ = 0
    for n in range(digit_num, 0, -1) :
        digit_value = calc_digit_value(value, n)
        if digit_value > 0 :
            value -= digit_value * (10 ** (n - 1))
            sum_ += digit_value ** 5

    if sum_ == index:
        a.append(index)

sum_ = 0
for num in a :
    sum_ += num
print(sum_)
