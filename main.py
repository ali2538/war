from Deck import Deck
from Player import Player

deckOfCards = Deck()

deckOfCards.shuffle()

player1 = Player("Player1")
player2 = Player("Player2")

deckOfCards.deal(player1, player2)

cardsOnTable = []

while (player1.hand() > 0) and (player2.hand() > 0):
    player1Card = player1.playCard()
    player2Card = player2.playCard()
    print(f'{player1.name} has {player1Card[1]} of {player1Card[0]}')
    print(f'{player2.name} has {player2Card[1]} of {player2Card[0]}')
    if player1Card[2] > player2Card[2]:
        print(f'{player1.name} get the cards')
        player1.receiveCard(player1Card)
        player1.receiveCard(player2Card)
        if len(cardsOnTable) > 0:
            player1.receiveHeldCards(cardsOnTable)
            cardsOnTable.clear()
    elif player1Card[2] < player2Card[2]:
        print(f'{player2.name} get the cards')
        player2.receiveCard(player2Card)
        player2.receiveCard(player1Card)
        if len(cardsOnTable) > 0:
            player2.receiveHeldCards(cardsOnTable)
            cardsOnTable.clear()
    elif player1Card[2] == player2Card[2]:
        if (player2.hand() > 0) and (player1.hand() > 0):
            print(f'cards are equal. Set aside the cards')
            cardsOnTable.append(player1.putCardsOnHold())
            print(f'after 1 ====== {cardsOnTable}')
            cardsOnTable.append(player2.putCardsOnHold())
            print(f'after 2 ====== {cardsOnTable}')
            cardsOnTable.append(player1Card)
            cardsOnTable.append(player2Card)
        elif (player1.hand() == 0) or (player2.hand() == 0):
            if player2.hand() == 0:
                print(f'{player1.name} has won the game')
                print(f'{player1.name} Card Count: {player1.hand()}')
                print(f'{player2.name} Card Count: {player2.hand()}')
            else:
                print(f'{player2.name} has won the game')
                print(f'{player1.name} Card Count: {player1.hand()}')
                print(f'{player2.name} Card Count: {player2.hand()}')
    input('Press enter to continue: ')
print(f'{player1.name} Card Count: {player1.hand()}')
print(f'{player2.name} Card Count: {player2.hand()}')
if player1.hand() == 52:
    print(f'{player1.name} has won the game')
if player2.hand() == 52:
    print(f'{player2.name} has won the game')
