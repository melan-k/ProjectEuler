factors = 3..10000
def getDividors(n)
    a = []
    cnt = 1
    while cnt < n do
        if (n % cnt == 0) then
            a << cnt
        end
        cnt += 1
    end
    if a.length == 0 then
        a << 'nothing'
    end
    a
end

d_array = []
factors.each do |f|
    a1 = getDividors(f)
    unless a1[0] == 'nothing' then
        a2 = a1.reduce(0) { |sum, n| sum += n }
        a3 = getDividors(a2).reduce(0) do |sum, n|
            unless n == 'nothing' then
                sum += n
            end
        end

        if a3 == f && a2 != f then
            # p "%s : %d => %d" % [a1.to_s, a2, f]
            d_array << f
        end
    end
end

p d_array.reduce(0) { |sum, n| sum += n }
