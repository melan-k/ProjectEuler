factors = 3...10000
a = []
n = 600851475143
while true do
    factors.each do |f|
        if n % f == 0 then
            a << f
            n /= f
            break
        end
    end
    if n == 1 then
        break
    end
end

p a.max
