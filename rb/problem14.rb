begin_num = 2
chain_length = 0
max_begin_num = 0
while begin_num < 1000000 do
    tmp = begin_num
    tmp_chain_length = 0
    while tmp != 1 do
        if tmp.even? then
            tmp = tmp / 2
        else
            tmp = tmp * 3 + 1
        tmp_chain_length += 1
        end
    end
    if tmp_chain_length > chain_length then
        chain_length = tmp_chain_length
        max_begin_num = begin_num
        end
    begin_num += 1
end
p "%d:%d" % [max_begin_num, chain_length]
