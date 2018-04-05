import math

target = 1000000 - 1
indices = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
order_str = ''
cnt = len(indices) - 1

while target != 0 :
    div, mod = divmod(target, math.factorial(cnt))
    order_str += indices[div]

    target = mod
    cnt -= 1
    del indices[div]

for index in indices :
    order_str += index

print(order_str)
