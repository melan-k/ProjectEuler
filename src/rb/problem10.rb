require 'prime'
a = []
Prime.each do |n|
  if n >= 2000000 then
    break
    end
  a << n
end

p a.reduce(0) {|sum, n| sum += n}
