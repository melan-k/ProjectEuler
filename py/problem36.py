palindromes = []
for n in range(1, 1000000):
    s = str(n)
    if s == s[::-1]:
        b = str(bin(n))
        rb = b[::-1]
        if b[2:] == rb[:-2]:
            palindromes.append(n)

sum = 0
for p in palindromes:
    sum += p
print(sum)
