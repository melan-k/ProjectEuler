result = 0
def calcRoute(width, height)
    if width == 0 or height == 0 then
        p width, height
        result += 1
    elsif width < 2 or height < 2 then
        if width == 1 then
            result += height + 1
        elsif height == 1 then
            result += width + 1
        end
    else
        height.times do |n|
            calcRoute(width-1, n + 1)
        end
    end
end

p calcRoute(0, 0)
