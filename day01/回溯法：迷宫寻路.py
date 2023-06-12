# 定义数组,创建一个迷宫
# 用数组创建出一个迷宫，0为可以通过的路径，1为墙壁。
l = [[0, 0, 0, 1, 0, 0, 1],
     [1, 1, 0, 0, 0, 1, 1],
     [0, 0, 0, 1, 0, 1, 1],
     [0, 1, 0, 1, 1, 1, 1],
     [0, 1, 0, 1, 1, 1, 1],
     [0, 0, 1, 0, 0, 0, 0],
     [1, 0, 1, 0, 1, 0, 1],
     [1, 0, 0, 0, 0, 0, 1]
     ]
for i in l:
    print(i)

stack = [[0, 0]]  # 开始位置
history = [[0, 0]]  # 已走过的位置


def up(location):
    # 判断是否到迷宫的最上侧
    if location[0] == 0:
        return False
    else:
        new_location = [location[0] - 1, location[1]]
    # 判断是否走过这个路
    if new_location in history:
        return False
    # 判断下个路径是否为墙
    elif l[new_location[0]][new_location[1]] == 1:
        return False
    # 进入到下个路径，把下个路径添加到位置和历史路径中
    else:

        stack.append(new_location)
        history.append(new_location)
        return True


def down(location):
    # 判断是否到迷宫的最下侧
    if location[0] == l.__len__() - 1:
        return False
    else:
        new_location = [location[0] + 1, location[1]]
    if new_location in history:
        return False
    elif l[new_location[0]][new_location[1]] == 1:
        return False
    else:
        stack.append(new_location)
        history.append(new_location)
        return True


def left(location):
    # 判断是否到迷宫的最左侧
    if location[1] == 0:
        return False
    else:
        new_location = [location[0], location[1] - 1]
    if new_location in history:
        return False
    elif l[new_location[0]][new_location[1]] == 1:
        return False
    else:
        stack.append(new_location)
        history.append(new_location)
        return True


def right(location):
    # 判断是否到迷宫的最右侧
    if location[1] == l[0].__len__() - 1:
        return False
    else:
        new_location = [location[0], location[1] + 1]
    if new_location in history:
        return False
    elif l[new_location[0]][new_location[1]] == 1:
        return False
    else:
        stack.append(new_location)
        history.append(new_location)
        return True


while stack[-1] != [5, 6]:
    location = stack[-1]  # 将当前位置传入参数location中
    print(location)
    if down(location):
        print('down')
        location = stack[-1]
        continue
    if right(location):
        print('right')
        location = stack[-1]
        continue
    if up(location):
        print('up')
        location = stack[-1]
        continue
    if left(location):
        print('left')
        location = stack[-1]
        continue
    # 这个代码实现的是回溯功能,如果跑错路的话回退到上一级
    stack.pop()
print("所有路径")
print(history)
print('迷宫路径为:')
print(stack)
