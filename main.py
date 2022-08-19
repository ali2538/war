from Deck import Deck
from Player import Player

deckOfCards = Deck()

deckOfCards.shuffle()

player1 = Player("Player1")
player2 = Player("Player2")

deckOfCards.deal(player1, player2)

player1.playCard()
player2.playCard()
