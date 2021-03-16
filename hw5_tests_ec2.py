#########################################
#####        Name: Hang Song        #####
#####      Uniqname: hangsong       #####
#########################################
import unittest
import hw5_cards_ec2
import random

class TestHand(unittest.TestCase):
    def test_remove_pairs(self):
        # Queen of Spades, King of Diamonds, 6 of Hearts, 5 of Clubs, 3 of Spades, 3 of Hearts, 5 of Hearts
        # Card is not
        init_cards = [hw5_cards_ec2.Card(3,12),hw5_cards_ec2.Card(0,13),hw5_cards_ec2.Card(2,6),hw5_cards_ec2.Card(1,5),hw5_cards_ec2.Card(3,3),hw5_cards_ec2.Card(2,3),hw5_cards_ec2.Card(2,5)]
        hand = hw5_cards_ec2.Hand(init_cards)
        length0 = len(hand.cards)
        card_str_0 = [card.__str__() for card in hand.cards]
        hand.remove_pairs()
        length1 = len(hand.cards)
        card_str_1 = [card.__str__() for card in hand.cards]
        # card length is shortened
        self.assertEqual(length0-4,length1,msg="Test if the pairs are removed")
        self.assertIn("5 of Clubs",card_str_0)
        self.assertIn("5 of Hearts",card_str_0)
        self.assertIn("3 of Spades",card_str_0)
        self.assertIn("3 of Hearts",card_str_0)
        # remove the correct card
        self.assertTrue("5 of Clubs" not in card_str_1)
        self.assertTrue("5 of Hearts" not in card_str_1)
        self.assertTrue("3 of Spades" not in card_str_1)
        self.assertTrue("3 of Hearts" not in card_str_1)
        # nothing to remove when there are no pairs
        hand.remove_pairs()
        length2 = len(hand.cards)
        self.assertEqual(length1,length2,msg="Test if the length is equal when there is no pairs to be removed")

class TestDeck(unittest.TestCase):
    def test_deal(self):
        #Test when there are enough cards to deal
        num_hands = 5
        num_cards = 8
        deck = hw5_cards_ec2.Deck()
        handlist = deck.deal(num_hands,num_cards)
        self.assertEqual(len(handlist),5)
        self.assertIsInstance(handlist[0],hw5_cards_ec2.Hand)
        self.assertEqual(len(handlist[-1].cards),8)

        #Test when there are not enough cards to distribute everyone
        num_hands_2 = 8
        num_cards_2 = 7
        deck2 = hw5_cards_ec2.Deck()
        handlist2 = deck2.deal(num_hands_2,num_cards_2)
        self.assertEqual(len(handlist2),8)
        self.assertIsInstance(handlist2[-1],hw5_cards_ec2.Hand)
        self.assertEqual(len(handlist2[0].cards),7)
        self.assertEqual(len(handlist2[-1].cards),6)
        self.assertEqual(len(handlist2[4].cards),6)






if __name__=="__main__":
    unittest.main()