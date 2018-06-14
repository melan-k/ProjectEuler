from lib.math_utils import get_palindrome_num, is_palindrome_num
count = 0

for n in range(1, 10000):
    tmp = n
    roop = 0
    while(True):
        tmp += get_palindrome_num(tmp)
        if is_palindrome_num(tmp):
            break

        roop += 1
        if roop >= 50:
            count += 1
            break

print(count)
