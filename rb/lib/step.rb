def step(n)
    return (n * (n + 1)) / 2
end

$sum = 0
def calcRoute(width, height)
    p "[%d : %d] => %d" % [width, height, $sum]
    if width >= 2 then
        tmpWidth = width - 1
        (height + 1).times do |n|
            calcRoute(tmpWidth, n)
        end
    elsif width == 1 then
        if height == 0 then
            $sum += 1
        else
            $sum += height + 1
        end
    end
end

calcRoute(3,3)
