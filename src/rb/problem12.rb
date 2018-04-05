require 'prime'

cnt = 1
while true do
    tnum =  (cnt * (cnt + 1)) / 2   # calculate the triangle number : n(n+1) / 2
    factors = tnum.prime_division   # [[prime1, cnt], [prime2, cnt]]
    dividor_cnt = 1
    factors.each do |n|             # { tnum = a^p * b^q * c^r  } =>
        dividor_cnt *= n[1] + 1     # dividors count : (p+1)(q+1)(r+1)
    end
    if dividor_cnt < 500 then
        cnt += 1
    else
        break
    end
end
p tnum