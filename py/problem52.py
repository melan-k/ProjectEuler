from lib.math_utils import calc_digit, each_num_of_points
result = 0
for i in range(10, 1000000):
    digit = calc_digit(i)
    if digit != calc_digit(i * 6):
        continue
    x1 = set(each_num_of_points(i))
    x2 = set(each_num_of_points(i*2))
    x3 = set(each_num_of_points(i*3))
    x4 = set(each_num_of_points(i*4))
    x5 = set(each_num_of_points(i*5))
    x6 = set(each_num_of_points(i*6))
    if len(x1) != digit or len(x2) != digit or len(x3) != digit or \
       len(x6) != digit or len(x6) != digit or len(x6) != digit:
        continue;
    if x1==x2 and x1==x3 and x1==x4 and x1==x5 and x1==x6:
        print(i)

print(result)
