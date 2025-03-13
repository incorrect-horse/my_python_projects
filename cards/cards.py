import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def present(self):
        return f'{self.value} of {self.suit}'

class Hand:
    def __init__(self, hand=[]):
        self.hand = hand
        self.discard_pile = DiscardPile()

    def discard(self):
        if len(self.hand) == 0:
            print('nothing to discard')
            return None
        remove_a_card = self.hand.pop()
        print(remove_a_card.present())
        self.discard_pile.make_discard_pile(remove_a_card)
        return remove_a_card.present()

    def show_hand(self):
        print(len(self.hand), '- cards in hand')
        return [x.present() for x in self.hand]

    def fold(self):
        if len(self.hand) == 0:
            print('nothing to fold')
            return None
        return [self.discard() for card in range(len(self.hand))]

class DiscardPile:
    def __init__(self):
        self.discarded_cards = []
    
    def make_discard_pile(self, add_to_discard):
        self.discarded_cards.append(add_to_discard)
        return [x.present() for x in self.discarded_cards]

    def show_discard(self):
        if len(self.discarded_cards) == 0:
            print('nothing to show')
            return None
        return [x.present() for x in self.discarded_cards]

    def return_discard_pile_to_deck(self):
        if len(self.discarded_cards) == 0:
            print('nothing to return')
            return None
        return [my_cards.cards.append(self.discarded_cards.pop()) for card in range(len(self.discarded_cards))]

class Deck:
    def __init__(self):
        # suits = ['hearts', 'diamonds', 'clubs', 'spades']
        suits = [chr(0x2665), chr(0x2666), chr(0x2663), chr(0x2660)]
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

        self.cards = [Card(suit, value) for suit in suits for value in values]

    def show_deck(self):
        print('card deck:', self.cards)
        return self.cards

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self, cards=1):
        self.hand = Hand().hand
        self.shuffle()
        for i in range(cards):
            self.hand.append(self.cards.pop())
        return self.hand

    def deal_hand(self):
        if len(self.cards) == 0:
            return None
        return self.deal_card(5)

    def count_remaining(self):
        return len(self.cards)

    def get_remaining(self):
        return [x.present() for x in self.cards]

def run():
    menu = "\nWhat Do Now?\n\n\
Card Deck\t\t\tHand\n\
  1) shuffle deck\t\t  4) deal hand\n\
  2) show deck\t\t\t  5) deal one card from deck\n\
  3) # cards in deck\t\t  6) show hand\n\
  \t\t\t\t  7) discard one from hand\n\
Discard\t\t\t\t  8) fold\n\
  9) show discard pile\n\
  10) discard pile to deck\tOther Actions\n\
  \t\t\t\t  0) quit\n\
  >>  "

    try:
        while True:
            usr_input = input(menu)
            if usr_input == '1':
                print('\nshuffling deck')
                my_cards.shuffle()
            elif usr_input == '2':
                print('\nshow deck')
                print(my_cards.get_remaining())
            elif usr_input == '3':
                print('\ncards in deck')
                print(my_cards.count_remaining())

            elif usr_input == '4':
                print('\ndealing n new cards')
                my_cards.deal_hand()
            elif usr_input == '5':
                print('\ndealing one card')
                my_cards.deal_card()
            elif usr_input == '6':
                print('\nshowing hand')
                print(my_hand.show_hand())
            elif usr_input == '7':
                print('\ndiscarding one card')
                my_hand.discard()
            elif usr_input == '8':
                print('\nfolding hand - cards placed in discard pile')
                my_hand.fold()
            elif usr_input == '9':
                print('\ndiscard pile')
                print(my_hand.discard_pile.show_discard())
            elif usr_input == '10':
                print('\nreturn discard pile to deck')
                my_hand.discard_pile.return_discard_pile_to_deck()

            elif usr_input == '99':
                print('\nshow deck objs')
                my_cards.show_deck() # shows raw objects...
            elif usr_input == '0':
                print('\nexit game')
                break
            else:
                print('\ncommand not recognized')
    except KeyboardInterrupt:
        print('\nctrl+c')

if __name__ == '__main__':
    my_cards = Deck()
    my_hand = Hand()
    run()

print('\nGoodbye!')
