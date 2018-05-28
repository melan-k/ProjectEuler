def calc_score(name) :
    sum_ = 0
    for s in name :
        sum_ += ord(s) - (ord('A') - 1)
    return sum_

with open('names.txt', 'r') as f :
    names_array = f.read().replace("\"", "").split(',')
    sorted_array = sorted(names_array)
    scores_array = []
    for index, name in enumerate(sorted_array, start = 1) :
        score = calc_score(name)
        print("{} : {} => {}".format(index + 1, name, score))
        scores_array.append(score * (index))

sum_ = 0
for score in scores_array :
    sum_ += score
print(sum_)
