import random
import unittest

VERSION = 0.01
 
class Card:
    '''a standard playing card
    cards will have a suit and a rank
    Class Attributes
    ----------------
    suit_names: list
        the four suit names in order 
        0:Diamonds, 1:Clubs, 2: Hearts, 3: Spades
    
    faces: dict
        maps face cards' rank name
        1:Ace, 11:Jack, 12:Queen,  13:King
    Instance Attributes
    -------------------
    suit: int
        the numerical index into the suit_names list
    suit_name: string
        the name of the card's suit
    rank: int
        the numerical rank of the card
    rank_name: string
        the name of the card's rank (e.g., "King" or "3")
    '''
    suit_names = ["Diamonds","Clubs","Hearts","Spades"]
    faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}
 

    def __init__(self, suit=0,rank=2):
        self.suit = suit
        self.suit_name = Card.suit_names[self.suit]

        self.rank = rank
        if self.rank in Card.faces:
            self.rank_name = Card.faces[self.rank]
        else:
            self.rank_name = str(self.rank)
 
    def __str__(self):
        return f"{self.rank_name} of {self.suit_name}"
 

class Deck:
    '''a deck of Cards
    Instance Attributes
    -------------------
    cards: list
        the list of Cards currently in the Deck. Initialized to contain
        all 52 cards in a standard deck
    '''

    def __init__(self): 

        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card) # appends in a sorted order
 
    def deal_card(self, i=-1):
        '''remove a card from the Deck
        Parameters  
        -------------------
        i: int (optional)
            the index of the ard to remove. Default (-1) will remove the "top" card
        Returns
        -------
        Card
            the Card that was removed
        '''
        return self.cards.pop(i) 
 
    def shuffle(self):
        '''shuffles (randomizes the order) of the Cards
        self.cards is modified in place
        Parameters  
        ----------
        None
        Returns
        -------
        None
        '''
        random.shuffle(self.cards)
 
    def replace_card(self, card):
        card_strs = [] # forming an empty list
        for c in self.cards: # each card in self.cards (the initial list)
            card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs: # if the string representing this card is not in the list already
            self.cards.append(card) # append it to the list

    def sort_cards(self):
        '''returns the Deck to its original order

        Cards will be in the same order as when Deck was constructed.
        self.cards is modified in place.
        Parameters
        ----------
        None
        Returns
        -------
        None
        '''
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)
 
    def deal_hand(self, hand_size):
        '''removes and returns hand_size cards from the Deck
        
        self.cards is modified in place. Deck size will be reduced
        by hand_size
        Parameters  
        -------------------
        hand_size: int
            the number of cards to deal
        Returns
        -------
        list
            the top hand_size cards from the Deck
        '''
        hand_cards = []
        for i in range(hand_size):
            hand_cards.append(self.deal_card())
        return hand_cards

    def deal(self,num_hands,num_cards):
        ''' Deal the deck cards and return a list of Hands (Hand object).

        if the num_cards is -1, all the cards should be dealt, then the deck
        should be empty; else, the list of hand objects will be returned.
        Parameters
        ----------
        num_hands: int
            the number of hands involved in the game
        num_cards: int
            the number of cards per hand
        Returns
        -------
        list
            a list in which every element is an instance of Hand
        '''
        self.shuffle()
        hand_list = []

        if num_hands*num_cards < len(self.cards) and num_hands > 0 and num_cards > 0:
            for i in range(num_hands):
                hand_cards = self.deal_hand(num_cards)
                hand_list.append(Hand(hand_cards))
        elif num_hands*num_cards > len(self.cards) or num_cards == -1:
            new_num_cards = len(self.cards)//num_hands
            hand_cards_list = []
            ## Same amount of the cards are distributed to everyone
            for i in range(num_hands):
                hand_cards = self.deal_hand(new_num_cards)
                hand_cards_list.append(hand_cards)
            ## Distribute the rest of the cards
            for j in range(len(self.cards)):
                left_card = self.deal_card()
                hand_cards_list[j].append(left_card)
            for k in hand_cards_list:
                hand_list.append(Hand(k))

        return hand_list




# create the Hand with an initial set of cards
class Hand:
    '''a hand for playing card
    Class Attributes
    ----------------
    None
    Instance Attributes
    -------------------
    init_card: lista list of cards
    '''
    def __init__(self, init_cards):
        self.cards = []
        for card in init_cards:
            self.cards.append(card)
    

    def add_card(self, card):
        '''add a card
        add a card to the hand
        silently fails if the card is already in the hand
        Parameters
        -------------------
        card: instance
        a card to add
        Returns
        -------
        None
        '''
        card_str = []
        for i in self.cards:
            card_str.append(i.__str__())

        if card.__str__() not in card_str:
            self.cards.append(card)



    def remove_card(self, card):
        '''remove a card from the hand
        Parameters
        -------------------
        card: instance
        a card to remove
        Returns
        -------
        the card, or None if the card was not in the Hand
        '''
        card_str = []
        for i in self.cards:
            card_str.append(i.__str__())
        
        if card.__str__() in card_str:
            card_to_remove_idx = card_str.index(card.__str__())
            card_to_remove = self.cards.pop(card_to_remove_idx)
            return card_to_remove
        else:
            return None


    def draw(self, deck):
        '''draw a card
        draw a card from a deck and add it to the hand
        side effect: the deck will be depleted by one card
        Parameters
        -------------------
        deck: instance
        a deck from which to draw
        Returns
        -------
        None
        '''
        card = deck.deal_card()
        self.cards.append(card)

    def remove_pairs(self):
        '''remove all the pairs from the hand
        if there are three of a kind, only two will be removed
        Parameters
        -------------------
        None
        Returns
        -------
        None
        '''
        ## organize the pairs in ranks
        order_cards = {}
        keys = [i for i in range(1,14)]
        order_cards = {k:[] for k in keys}
        for card in self.cards:
            for key in order_cards.keys():
                if card.rank == key:
                    order_cards[key].append(card)

        ## pop the pairs out
        for l in order_cards.values():
            if len(l) == 2:
                l.clear()
            elif len(l) == 3:
                l.pop(l.index(random.choice(l)))
                l.pop(l.index(random.choice(l)))
            elif len(l) == 4:
                l.clear()

        ##reconstruct the cards in hand
        new_cards = []
        for l in order_cards.values():
            new_cards.extend(l)

        self.cards = new_cards


def print_hand(hand):
    '''prints a hand in a compact form
    
    Parameters  
    -------------------
    hand: list
        list of Cards to print
    Returns
    -------
    none
    '''
    hand_str = '/ '
    for c in hand:
        s = c.suit_name[0]
        r = c.rank_name[0]
        hand_str += r + "of" + s + ' / '
    print(hand_str)



# init_cards = [Card(3,12),Card(0,13),Card(2,6),Card(1,5),Card(3,3),Card(2,3),Card(2,5)]
# hand = Hand(init_cards)
# for card in hand.cards:
#     print(card)

# hand.remove_pairs()
# print("-"*60)
# for card in hand.cards:
#     print(card)
deck = Deck()
list1 = deck.deal(8,-1)
print(list1)
for i in list1:
   print(len(i.cards))
# for i in list1:
#     print(len(i))