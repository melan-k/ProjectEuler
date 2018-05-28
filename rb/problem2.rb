f1 = 0
f2 = 1
a = []
lim = 4000000

while true do
    buf = f2
    f2 += f1
    f1 = buf
    if  f2 > lim then
        break
    end
    if f2.even? then
        a << f2
    end
end
sum = a.reduce(0) do |sum, element|
    sum += element
end;

p sum
