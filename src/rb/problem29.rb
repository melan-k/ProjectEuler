range = 2..100
value = 0
array = []
range.each do |a|
    range.each do |b|
        value = a ** b
        unless array.include?(value) then
            array << value
        end
    end
end

p array.count
