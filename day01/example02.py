names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# 录入五个学生三门课程的成绩
# 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# scores = [[None] * len(courses)] * len(names)
'''
请输入关羽的语文成绩: 12
[[12.0, None, None], [12.0, None, None], [12.0, None, None], [12.0, None, None], [12.0, None, None]]
请输入关羽的数学成绩: 
'''
scores = [[None] * len(courses) for _ in range(len(names))]
'''
请输入关羽的语文成绩: 12
[[12.0, None, None], [None, None, None], [None, None, None], [None, None, None], [None, None, None]]
请输入关羽的数学成绩: 23
[[12.0, 23.0, None], [None, None, None], [None, None, None], [None, None, None], [None, None, None]]
请输入关羽的英语成绩: 
'''
for row, name in enumerate(names):
    '''
    Return an enumerate object.
    
      iterable
        an object supporting iteration
    
    The enumerate object yields pairs containing a count (from start, which
    defaults to zero) and a value yielded by the iterable argument.
    
    enumerate is useful for obtaining an indexed list:
        (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
    '''
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
        print(scores)
print(scores)
