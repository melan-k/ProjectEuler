from lib.math_utils import each_num_of_points

num_sum = 1
denom_sum = 1
for denom in range(98, 10, -1):
    for num in range(11, denom):
        if denom % 10 == 0 and num % 10 == 0:
            continue
        if denom % 11 == 0 or num % 11 == 0:
            continue
        original = num / denom
        common = set(each_num_of_points(num)) & set(each_num_of_points(denom))
        if len(common) != 1 or common == {0}:
            continue
        # print("{}/{} : {}".format(num, denom, common))
        removal = list(common)[0]
        if (denom - removal) % 10 == 0:
            denom_ = int((denom - removal) / 10)
        else:
            denom_ = denom - removal * 10
        if (num - removal) % 10 == 0:
            num_ = int((num - removal) / 10)
        else:
            num_ = num - removal * 10
        if num_ >= denom_:
            continue

        # print("{}/{} => {}/{} = {}".format(num, denom, num_, denom_, original))
        if (num_ / denom_) == original:
            num_sum *= num_
            denom_sum *= denom_

print(int(denom_sum / num_sum))
