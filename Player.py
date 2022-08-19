class Player:
    def __init__(self, name) -> None:
        self.name = name
        self._hand = []

    def playCard(self):
        print(f'{self._hand[0][1]} of {self._hand[0][0]}')

    def receiveCard(self, card):
        self._hand.append(card)

    def hand(self):
        return self._hand

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
