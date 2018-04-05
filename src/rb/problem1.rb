a = 1...1000
result = a.inject do |sum, n|
    add = ((n%3==0) or (n%5)==0) ? n : 0
    sum += add
end
p result
