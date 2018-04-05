def palindrome?(n)
    d = Math.log10(n).floor + 1
    cd = d / 2
    str = n.to_s
    s1 = str[0..cd-1]
    if d.odd? then
        s2 = str[cd+1..str.length].reverse
    else
        s2 = str[cd..str.length].reverse
    end

    s1 == s2
end

inc = 0
cnt = 100
limit = 999
max = 0
f0 = 0
f1 = 0

while cnt <= limit do
    value = cnt * (cnt + inc)
    if palindrome?(value) & (value > max) then
        max = value
        f0 = cnt
        f1 = cnt + inc
    end

    if inc == limit - cnt then
        cnt += 1
        inc = 0
    else
        inc += 1
    end
end

p max, f0, f1