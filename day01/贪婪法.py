"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
"""


class Thing(object):
    """定义物品类"""

    def __init__(self, names, price, weight):
        self.names = names
        self.price = price
        self.weight = weight

    # 需要借助装饰器，使value函数成为Thing类的一个属性
    @property
    def value(self):
        return self.price / self.weight


def input_thing():
    """编写输入函数，规定输入的格式"""
    names_str, price_str, weight_str = input("输入(\"电脑 200 20\"").split()
    return names_str, int(price_str), int(weight_str)


def main():
    max_weight, num_thing = map(int, input("输入最大重量和房间物品数量").split())
    all_thing = []
    for _ in range(num_thing):
        all_thing.append(Thing(*input_thing()))
    all_thing.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_thing:
        if thing.weight + total_weight <= max_weight:
            print(f"小偷偷走了{thing.names}")
            total_weight += thing.weight
            total_price += thing.price
    print(f"总价值{total_price}")


if __name__ == '__main__':
    main()
