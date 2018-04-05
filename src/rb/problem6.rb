numbers = 1..100
result1 = numbers.reduce(0) do |sum, n|
    sum += n**2
end

result2 = numbers.reduce(0) do |sum, n|
    sum += n
end

p result2**2 - result1
