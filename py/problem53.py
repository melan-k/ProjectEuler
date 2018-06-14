from lib.math_utils import comb, even
count = 0
for n in range(23, 101):
    for r in range(1, n):
        if comb(n,r) > 1000000:
            count += 1
print(count)
