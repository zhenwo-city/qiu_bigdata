'''
顺序查找
'''
def seq_search(items,key):
    for index,item in enumerate(items):
        if key==item:
            return index
    return -1
'''
折半查找
'''
def bin_search(items,key):
    start,end=0,len(items)-1
    while start<=end:
        mid=(start+end)//2
        if key>items[mid]:
            start=mid+1
        elif key<items[mid]:
            end=mid-1
        else:
            return mid
    return -1
