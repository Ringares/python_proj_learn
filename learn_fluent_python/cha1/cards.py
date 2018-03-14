"""
1. collections.namedtuple 用于构建只有属性,没有方法的 简单对象
2. 实现了__len__, __getitem__ 后, 就可以利用标准库的 random.choice 操作自定义对象
3. 因为 __getitem__ 交给了 [] 操作, 所以 deck 类自动支持切片操作
4. 迭代通常是隐式的, 如果没有实现 __contains__, 那么 in 操作就会按顺序执行迭代搜索

"""
import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [Card(rank, suit)
                      for rank in self.ranks
                      for suit in self.suits]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, item):
        return self.cards[item]


deck = FrenchDeck()

print(str(len(deck)))
print(deck[2:10])
print('choice: ', choice(deck))

'''
排序
'''
suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * 4 + suit_value[card.suit]


for c in sorted(deck, key=spades_high):
    print(c)
