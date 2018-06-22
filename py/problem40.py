sum_str = ''
for i in range(1, 1000000):
    sum_str += str(i)
result = 1
for i in range(6):
    result *= int(sum_str[1 * (10**i) - 1])
print(result)
