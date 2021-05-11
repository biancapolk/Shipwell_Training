# WAR.PY
# CARD
# SUIT, RANK, VALUE
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = {'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'}
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        # All 52 card objects
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the Card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    def remove_one(self):
        pass
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # List of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

if __name__ == "__main__":
    # Creating a new instance of the Deck class
    new_deck = Deck()
    # first_card = new_deck.all_cards[-1]
    # print(first_card)



    # try:
    #
    #     five_of_hearts = Card("Hearts", 'Five')
    # except:
    #     print("Sorry, something went wrong. Check that the title of the suit and rank are capitalized")
    # else:
    #     print(five_of_hearts.value)



    # Loop through all of the cards in and new deck and print each card object
    # for card_object in new_deck.all_cards:
    #   print(card_object)

    #
    new_deck.shuffle()
    mycard = new_deck.deal_one()
    print(mycard)
    print(new_deck.all_cards[0])
    new_player = Player("Jose")
    print(new_player)