till_twenty = \
['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', \
 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']

tens_places = \
['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def convert_num_to_string(num_, split_=' ', compliance_=False) :
    assert(num_ >= 0)
    if num_ <= 20 :
        return till_twenty[num_]
    elif num_ < 100 :
        tens_place, ones_place = divmod(num_, 10)
        assert(tens_place >= 1)
        if ones_place == 0 :
            return tens_places[tens_place]
        else :
            return tens_places[tens_place] + split_ + till_twenty[ones_place]
    elif num_ < 1000 :
        hundreds_place, tens_mod = divmod(num_, 100)
        tens_place, ones_mod = divmod(tens_mod, 10)
        and_ = ''
        assert(hundreds_place < 10 and hundreds_place >= 1)
        if compliance_ :
            and_ = split_ + 'and'

        if tens_mod == 0 :  # 100, 200, 300 ... 900
            return till_twenty[hundreds_place] + split_ + 'hundred'
        elif tens_mod <= 20 :  # 101, 209, 315 ... 920
            return till_twenty[hundreds_place] + split_ + 'hundred' + and_ + split_ + till_twenty[tens_mod]
        elif ones_mod == 0 :
            return till_twenty[hundreds_place] + split_ + 'hundred' + and_ + split_ + tens_places[tens_place]
        else :  # 121, 299, 321, 999
            return till_twenty[hundreds_place] + split_ + 'hundred' + and_ + split_ + tens_places[tens_place] + split_ + till_twenty[ones_mod]

    elif num_ == 1000 :
        thousands_place, hundreds_place = divmod(num_, 1000)
        if hundreds_place == 0 :
            return till_twenty[thousands_place] + split_ + 'thousand'

sum_ = 0
cnt_ = 1000
for i in range(1, cnt_ + 1) :
    str_ = convert_num_to_string(i, '', True)
    print(str_)
    sum_ += len(str_)

print(sum_)
