def each_triangular_number(upper):
    assert(upper > 0)
    a = []
    for n in range(1, upper):
        a.append(int(0.5 * n * (n + 1)))
    return a

def get_alphabetical_index(char):
    return ord(c) - (ord('A') - 1);

tris = each_triangular_number(100)
cnt = 0
with open('p042_words.txt', 'r', encoding="utf-8") as f:
    strings = f.read().rstrip().split(',')
    for str in strings:
        sum = 0
        for c in list(str)[1:-1]: # remove comma
            sum += get_alphabetical_index(c)
        if sum in tris:
            cnt += 1
print(cnt)
