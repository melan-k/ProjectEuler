def calc_recurring_decimal_point(denom) :
    prev_mod = 1
    divmod_array = []
    index = 0
    while True :
        div, mod = divmod(prev_mod * 10, denom)

        if mod == 0 :
            break

        if not [div, mod] in divmod_array :
            divmod_array.append([div, mod])
        else :
            index = divmod_array.index([div, mod])
            return len(divmod_array) - index

        prev_mod = mod

    return 0

def get_length_of_recurring_decimal_unit(num, upper = 1000) :
    cnt = 2
    while cnt <= upper :
        if num % cnt == 0 :
            break   # no recurring decimal
        if 10 ** cnt % num == 1 :
            return cnt

        cnt += 1

    return 0

max_ = 0
max_denom = 0
# point = 0
# for denom in range(2, 1000) :
#     point = get_length_of_recurring_decimal_unit(denom)
#     if point > max_ :
#         max_ = point
#         max_denom = denom

length = 0
for denom in range(2, 1000) :
    length = get_length_of_recurring_decimal_unit(denom)
    if length > max_ :
        max_ = length
        max_denom = denom

print(max_denom)