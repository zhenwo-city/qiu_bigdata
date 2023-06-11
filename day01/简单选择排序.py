def select_sort(items,cop=lambda x,y:x<y):
    ''' 简单选择排序'''
    items=items[:]
    for i in range(len(items)-1):
        min_index=i
        for j in range(i+1,len(items)):
            if cop(items[i],items[j]):
                min_index=j
        #这个地方需要注意，大值与小值互换
        items[i],items[min_index]=items[min_index],items[j]
    return items