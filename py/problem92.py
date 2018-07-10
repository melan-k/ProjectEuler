from lib.math_utils import each_num_of_points
cnt = 0
route_1 = set()
route_89 = set()
upper = 10000000
for n in range(upper - 1, 1, -1):
    value = n
    tmp = set()
    while(True):
        sum = 0
        for i in each_num_of_points(value):
            sum += i ** 2
        tmp.add(sum)
        if sum == 1 or sum in route_1:
            route_1 = route_1 | tmp # update the filter
            break
        if sum == 89 or sum in route_89:
            cnt += 1
            route_89 = route_89 | tmp # update the filter
            break
        value = sum
print(cnt)
