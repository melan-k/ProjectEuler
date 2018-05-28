require 'prime'
p Prime.each_with_index.find {|e, index| index == 100 - 1 }[0]
