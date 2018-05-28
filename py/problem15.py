sum = 0
def calcRoute(width_, height_) :
    global sum
    if width_ >= 2 :
        for n in range(height_ + 1) :
            calcRoute(width_ - 1, n)
    elif width_ == 1 :
        sum += height_ + 1

    return sum

print(calcRoute(20, 20))
