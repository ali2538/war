from random import shuffle

from Card import Card


class Deck:
    SUITES = ["Clubs", "Diamonds", "Hearts", "Spades"]
    RANKS = ["Ace", "Two", "Three", "Four", "Five", "Six",
             "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

    def __init__(self):
        self.deck = []
        for j in range(0, 4):
            for i in range(0, 13):
                if i == 0:
                    self.deck.append([self.SUITES[j], self.RANKS[i], 14])
                else:
                    self.deck.append([self.SUITES[j], self.RANKS[i], i + 1])

    def shuffle(self):
        shuffle(self.deck)

    def deal(self, player1, player2):
        for i in range(0, 52):
            if i % 2 == 0:
                player1.receiveCard(self.deck[i])
            else:
                player2.receiveCard(self.deck[i])

    def print(self):
        for card in self.deck:
            print(f'{card[0]} -- {card[1]} -- {card[2]}\n')
