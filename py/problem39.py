from math import sqrt

dict = {}
for a in range(1, 334):
    for b in range(a + 1, 500):
        slope = sqrt(a**2 + b**2)
        if a + b >= 1000 - slope:
            break
        if not slope.is_integer():
            continue

        p = a + b + int(slope)
        if p not in dict.keys():
            dict[p] = 1
        else:
            dict[p] += 1

max = [0, 0]    # key, value
for key, value in dict.items():
    if value > max[1]:
        max = [key, value]
print(max)
