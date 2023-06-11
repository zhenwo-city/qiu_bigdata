# 列表推导式：可以用来生成列表，集合，字典
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用股票价格大于100元的股票构造一个新的字典
prices2 = {key: value for key, value in prices.items() if value > 10}  # 生成的字典
print(prices2)
prices1 = {i for i in range(1, 20)}  # 生成的集合
print(prices1)
prices3 = [i for i in range(1, 30)]  # 生成的数组
print(prices3)
