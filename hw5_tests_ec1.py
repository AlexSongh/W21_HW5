#########################################
#####        Name: Hang Song        #####
#####      Uniqname: hangsong       #####
#########################################
import unittest
import hw5_cards_ec1
import random

class TestHand(unittest.TestCase):
    def test_init(self):
        init_cards = [hw5_cards_ec1.Card(3,12),hw5_cards_ec1.Card(0,13),hw5_cards_ec1.Card(2,6),hw5_cards_ec1.Card(1,5),hw5_cards_ec1.Card(3,3)]
        hand = hw5_cards_ec1.Hand(init_cards)
        self.assertIsInstance(hand,hw5_cards_ec1.Hand)
        self.assertIsInstance(hand.cards,list)
        self.assertEqual(hand.cards[0].__str__(),"Queen of Spades")
        self.assertEqual(hand.cards[1].__str__(),"King of Diamonds")
        self.assertEqual(hand.cards[2].__str__(),"6 of Hearts")
        self.assertEqual(hand.cards[3].__str__(),"5 of Clubs")
        self.assertEqual(hand.cards[4].__str__(),"3 of Spades")


    def testAddAndRemove(self):
        init_cards = [hw5_cards_ec1.Card(3,12),hw5_cards_ec1.Card(0,13),hw5_cards_ec1.Card(2,6),hw5_cards_ec1.Card(1,5),hw5_cards_ec1.Card(3,3)]
        hand = hw5_cards_ec1.Hand(init_cards) #create a Hand object for convenience
        handlength_0 = len(hand.cards)
        #Add a card (invalid card, not adding anything)
        hand.add_card(hw5_cards_ec1.Card(3,12))
        handlength_1 = len(hand.cards)
        self.assertEqual(handlength_0,handlength_1,msg="Test adding a card when the card is in hand.")
        #Add a card (valid card)
        hand.add_card(hw5_cards_ec1.Card(0,1))
        handlength_2 = len(hand.cards)
        self.assertEqual(handlength_1+1,handlength_2,msg="Test adding a card when the card is not in hand.")

        #Remove a card (valid card)
        card_to_remove = hand.remove_card(hw5_cards_ec1.Card(0,1))
        handlength_3 = len(hand.cards)
        self.assertEqual(handlength_2,handlength_3+1, msg="Test removing a card that is in hand")
        self.assertEqual(card_to_remove.__str__(),"Ace of Diamonds", msg = "Test the card that is removed is as specified")

        #Remove a card (invalid card, not really removing anything)
        card_to_remove2 = hand.remove_card(hw5_cards_ec1.Card(3,8))
        handlength_4 = len(hand.cards)
        self.assertEqual(handlength_3,handlength_4,msg="Test removing a card that is not in hand.")
        self.assertEqual(card_to_remove2,None)



    def test_draw(self):
        deck = hw5_cards_ec1.Deck()
        init_cards = [hw5_cards_ec1.Card(3,12),hw5_cards_ec1.Card(0,13),hw5_cards_ec1.Card(2,6),hw5_cards_ec1.Card(1,5),hw5_cards_ec1.Card(3,3)]
        hand = hw5_cards_ec1.Hand(init_cards)

        # Remove the cards that are in hand from the deck
        deck_str = []
        for i in deck.cards:
            deck_str.append(i.__str__())

        hand_str = []
        for i in hand.cards:
            hand_str.append(i.__str__())

        for i in hand_str:
            for j in deck_str:
                if j == i:
                    idx = deck_str.index(j)
                    deck.cards.pop(idx)
        # Make sure the cards in hand and the deck cards are compensate with each other.
        initial_deck_length = len(deck.cards)
        initial_hand_length = len(hand.cards)
        self.assertEqual(initial_deck_length+initial_hand_length,52,msg="Compensate pair")

        # Make sure the draw function works
        hand.draw(deck)
        after_deck_length = len(deck.cards)
        after_hand_length = len(hand.cards)
        self.assertEqual(after_deck_length+after_hand_length,52,msg="Compensate pair")
        self.assertEqual(after_deck_length,initial_deck_length-1,msg="Remove one from deck")
        self.assertEqual(after_hand_length,initial_hand_length+1,msg="Add one to the hand")



if __name__=="__main__":
    unittest.main(verbosity=2)