"""
快速排序 - 选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大
"""


def quick_sort(items, comp=lambda x, y: x <= y):
    "将set，tuple等类型的数据转换成list"
    items = list(items)[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items


def _quick_sort(items, start, end, cop):
    if start < end:
        print(items)
        pos = _partition(items, start, end, cop)
        print("左分区排序", items)
        _quick_sort(items, start, pos - 1, cop)
        print('又分区排序', items)
        _quick_sort(items, pos + 1, end, cop)


def _partition(items, start, end, cop):
    # 以最后一个数值为基准数
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        if cop(items[j], pivot):
            i += 1
            print(items[j], items[i])
            items[i], items[j] = items[j], items[i]
    # 排序完成，开始交换基准数
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1


items = [168, 158, 98, 100, 148, 567, 55, 198, 156, 178]
print(quick_sort(items))
