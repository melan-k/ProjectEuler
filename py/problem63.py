from lib.math_utils import calc_digit

cnt = 0
for i in range(1, 1000):
    for j in range(1, 1000):
        if calc_digit(i ** j) == j:
            cnt += 1

print(cnt)
