def bubble_sort(items, comp=lambda x, y: x > y):
    """搅拌排序(冒泡排序升级版)"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items
'''
和冒泡排序的思路是一样的，区别在于冒泡排序是一个i排一次序，而搅拌排序是顺序排完再逆序排
'''

def example_bubble_sort(items, cop=lambda x, y: x > y):
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if cop(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if cop(items[j - 1], items[j]):
                    items[j - 1], items[j] = items[j], items[j - 1]
                    swapped = True
        if not swapped:
            break
    return items
