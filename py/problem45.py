from lib.math_utils import each_triangular, each_pentagonal, each_hexagonal

tris = each_triangular(286, 100000)
pens = each_pentagonal(166, 100000)
hexs = each_hexagonal(144, 100000)
print(set(tris) & set(pens) & set(hexs))
