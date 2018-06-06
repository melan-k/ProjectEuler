from math import factorial

sum = 0
for cnt in range(1, 100000):
    a = list(str(cnt))
    sum_ = 0
    for n in a:
        sum_ += factorial(int(n))
    if sum_ == cnt:
        sum += cnt

print(sum - factorial(2) - factorial(1))
