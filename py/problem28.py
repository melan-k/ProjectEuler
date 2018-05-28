def get_value_of_rightup(n) :
    if n == 1 :
        return 1
    else :
        return get_value_of_rightup(n - 1) + 8 * (n - 1)

upper = 501 # n * 2 - 1 = length(1001) => n = 501
sum_ = 1
for n in range(2, upper + 1) :
    right_up = get_value_of_rightup(n);
    left_up = right_up - 2 * (n - 1)
    left_down = left_up - 2 * (n - 1)
    right_down = left_down - 2 * (n - 1)

    sum_ += right_up + left_up + left_down + right_down

print(sum_)
