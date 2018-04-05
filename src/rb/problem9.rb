a = 1
b = a + 1
c = 1000 - (a + b)

loop do
  unless (a**2) + (b**2) == (c**2) then
    b += 1
    c -= 1
    if b >= c then
      a += 1
      b = a + 1
      c = 1000 - (a + b)
    end
  else
    break
  end
end

puts a * b * c
