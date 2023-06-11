def merge(items1, items2, cop=lambda x, y: x > y):
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if cop(items1[index1], items2[index2]):
            items.append(items2[index2])
            index2 += 1
        else:
            items.append(items1[index1])
            index1 += 1
    items += items1[index1:]#如果不添加这个的话会出现无法完全合并的情况
    '''
    merge([1, 3, 5, 8], [2, 4, 7, 9, 10])
    [1, 2, 3, 4, 5, 7, 8]
    '''
    items += items2[index2:]
    return items



