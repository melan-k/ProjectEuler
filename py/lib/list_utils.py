def get_circular_nums(num):
    route = list(num)
    route_ = route[:]
    row = []
    box = route_
    row.append(box)
    for node in range(len(route)-1):
       row.append(box)
       row[node+1] = row[node][:]
       row[node+1].append(row[node][0])
       row[node+1].pop(0)

    cnums = []
    for elem in row:
        sum = 0
        for idx, c in enumerate(elem):
            sum += int(c) * 10 ** (len(elem) - (idx + 1))
        cnums.append(sum)
    return cnums
