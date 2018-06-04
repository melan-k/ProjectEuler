a = range(1, 1001)
sum = 0;
for i in a:
    sum += i ** i;

print(str(sum)[-11:])
