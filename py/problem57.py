from lib.math_utils import calc_digit
a = 1
b = 1
cnt = 0
for n in range(1, 1001):
    tmp = b
    b = (a + b)
    a = b + tmp
    if calc_digit(a) > calc_digit(b):
        cnt += 1
print(cnt)
