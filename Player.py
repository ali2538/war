class Player:
    HELD_CARDS_NUMBER = 1

    def __init__(self, name) -> None:
        self.name = name
        self._hand = []
        self.heldCards = []

    def playCard(self):
        return self._hand.pop(0)

    def receiveCard(self, card):
        self._hand.append(card)

    def hand(self):
        return len(self._hand)

    def putCardsOnHold(self, numberOfCardsToBeHeld=HELD_CARDS_NUMBER):
        tempCard = self._hand[0]
        self._hand.pop(0)
        return tempCard

    def receiveHeldCards(self, hd):
        self._hand.extend(hd)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def continuePlay(self):
        return len(self._hand) > 0

    def cardCount(self):
        return len(self.hand)
