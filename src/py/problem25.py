import math

def calc_digit(num) :
    if num == 0 :
        return 0
    return int(math.log10(abs(num)) + 1)

cnt = 2
f1 = 0
f2 = 1
upper_digit = 1000

while True :
    buf = f2
    f2 += f1
    f1 = buf
    if calc_digit(f2) >= upper_digit :
        break
    cnt += 1

print("f({}) : {}".format(cnt, f2))
