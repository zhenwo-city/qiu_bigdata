import itertools
# 产生ABCD的全排列
iter1=itertools.permutations('ABCD')
for i in iter1:
    print(i)

# 产生ABCDE的五选三组合
iter2=itertools.combinations('ABCDE', 3)
print('产生ABCDE的五选三组合')
for i in iter2:
    print(i)
# 产生ABCD和123的笛卡尔积
iter3=itertools.product('ABCD', '123')
print('产生ABCD和123的笛卡尔积')
for i in iter3:
    print(i)
# 产生ABC的无限循环序列
iter4=itertools.cycle(('A', 'B', 'C'))
itertools.groupby
iter5=itertools.accumulate('dwdhakwh')
for u in iter5:
    print(u)
