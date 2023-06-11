def bubble_sort(items, comp=lambda x, y: x > y):
    """冒泡排序"""
    #items=items#此方法和下边的赋值方法的区别在于，此方法是直接创建一个链接，指向同一个内存地址
    '''
    print(bubble_sort(a))[1, 4, 4, 7, 7, 7, 36]
    print(a)[1, 4, 4, 7, 7, 7, 36]
    '''
    # 下一个方法是创建一个不同内存区域的变量
    items = items[:]
    '''
    print(bubble_sort(a))[1, 4, 4, 7, 7, 7, 36]
    print(a)[4, 7, 1, 4, 7, 36, 7]
    '''
    for i in range(len(items) - 1):
        # swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        # if not swapped:
        #     break
    return items
def example_bubble_sort(items,cop=lambda x,y:x>y):
    items=items[:]#不改变传递参数
    # items=items#改变传递参数
    for i in range(len(items)-1):
        swapped=False#判断排序是否完成
        for j in range(len(items)-1-i):
            if cop(items[j],items[j+1]):
                items[j],items[j+1]=items[j+1],items[j]
                swapped=True#表示发生过一次排序，整体排序没有完成
        if not swapped:#表示没有经过swapped=True这个步骤，说明此刻已经排序完成，可以跳出循环
            break
    return items#返回排序之后的结果#如果使用items=items则不需要返回结果

a=[4, 7, 1, 4, 7, 36, 7]
print(example_bubble_sort(a))
print(a)

