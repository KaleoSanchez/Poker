import unittest
import Poker
from unittest.mock import patch

class TestPokerGame(unittest.TestCase):
    def test_HandRank(self):
        self.assertEqual(Poker.HandRank([1, 2, 3, 4, 13]), 6)  #Straight
        self.assertEqual(Poker.HandRank([0, 13, 26, 8, 1]), 7)  #3 of Kind
        self.assertEqual(Poker.HandRank([0, 2, 12, 39, 1]), 9)  #Pair
        self.assertEqual(Poker.HandRank([0, 1, 2, 3, 4]), 5) #Flush
        self.assertEqual(Poker.HandRank([0, 13, 26, 39, 14]), 3)  #4 of a Kind

    def test_DidPlayerWin(self):
        #the array on the left is player, the array on the right is dealer
        self.assertEqual(Poker.DidPlayerWinner([1,2,3,4,13],[5,6,7,8,9]),2)#Player win
        self.assertEqual(Poker.DidPlayerWinner([5,6,7,8,9],[1,2,3,4,13]),1)#Dealer Win
        self.assertEqual(Poker.DidPlayerWinner([5,6,7,8,9],[5,6,7,8,9]),3)#Tie

    def test_MoneyLeft(self):
        x = 0
        z = 100
        y = 200
        self.assertEqual(Poker.MoneyLeft(x,y),"n")
        self.assertEqual(Poker.MoneyLeft(y,x),"n")
        self.assertEqual(Poker.MoneyLeft(z,y),"y")
    
    def test_validBet(self):
        playerMoney = 100
        bet = 20 
        self.assertTrue(Poker.ValidBet(playerMoney,bet))
    
    def test_InvalidBet(self):
        playerMoney = 100
        bet = 200
        self.assertFalse(Poker.ValidBet(playerMoney,bet))

    def test_cardValues(self):
        duece = 1
        five = 5
        jack = 11
        Queen = 12
        King = 13
        Ace = 14
        self.assertEqual(Poker.GetCardValue(duece),"Deuce")
        self.assertEqual(Poker.GetCardValue(five),"5")
        self.assertEqual(Poker.GetCardValue(jack),"Jack")
        self.assertEqual(Poker.GetCardValue(Queen),"Queen")
        self.assertEqual(Poker.GetCardValue(King),"King")
        self.assertEqual(Poker.GetCardValue(Ace),"Ace")

    def test_GameResult_PlayerWin(self):
        result = 1
        PlayerMoney = 100
        DealerMoney = 100
        totalBet = 25
        self.assertEqual(Poker.GameResult(result,PlayerMoney,DealerMoney,totalBet), (75,125))
    
    def test_GameResult_DealerWin(self):
        result = 2
        PlayerMoney = 100
        DealerMoney = 100
        totalBet = 25
        self.assertEqual(Poker.GameResult(result,PlayerMoney,DealerMoney,totalBet), (125,75))
    
    def test_GameResult_Tie(self):
        result = 3
        PlayerMoney = 100
        DealerMoney = 100
        totalBet = 25
        self.assertEqual(Poker.GameResult(result,PlayerMoney,DealerMoney,totalBet), (100,100))
    
    def test_GetCardSuit(self):
        Spade = 0
        clubs = 1
        diamonds = 2
        hearts = 3
        self.assertEqual(Poker.GetCardSuit(Spade), 'Spades')
        self.assertEqual(Poker.GetCardSuit(clubs), 'Clubs')
        self.assertEqual(Poker.GetCardSuit(diamonds), 'Diamonds')
        self.assertEqual(Poker.GetCardSuit(hearts), 'Hearts')
    
    def test_ShowHand(self):
        Hand = [1,2,3,4,5]
        self.assertEqual(Poker.ShowHand(Hand),None)

    def test_deck(self):
        cards = Poker.deck()
        self.assertEqual(len(cards), 52)
        self.assertEqual(len(set(cards)), 52)
        self.assertTrue(all(isinstance(card, int) for card in cards))
    
    def test_ValidBet_zero(self):
        self.assertTrue(Poker.ValidBet(100, 0))

    @patch('builtins.print')
    def test_CardName_allSuits(self, mock_print):
        for card in [0, 13, 26, 39]:
            Poker.CardName(card)
        self.assertGreaterEqual(mock_print.call_count, 4)
    
    def test_GetCardValue_Two(self):
        self.assertEqual(Poker.GetCardValue(2), "2")
    
    def test_ValidBet_ExactlyPlayerMoney(self):
        self.assertTrue(Poker.ValidBet(100,100))

    def test_deck_card_range(self):
        deck = Poker.deck()
        self.assertTrue(all(0 <= card < 52 for card in deck))
    
    def test_ValidBet_negative(self):
        self.assertTrue(Poker.ValidBet(100, -5))
    
    @patch('builtins.print')
    def test_CardName_print(self, mock_print):
        Poker.CardName(0)
        mock_print.assert_called()
    
    @patch('builtins.print')
    def test_ShowHand_print(self, mock_print):
        Poker.ShowHand([0, 13, 26])
        self.assertGreaterEqual(mock_print.call_count, 3)

    @patch('builtins.print')
    def test_GameResult_prints_and_money_update(self, mock_print):
        dealer, player = Poker.GameResult(1, 150, 50, 25)
        self.assertEqual((dealer, player), (25, 175))
        mock_print.assert_called_with('\nPlayer Wins!, You win', 25, 'dollars!')

    @patch('builtins.print')
    def test_GameResult_tie_print(self, mock_print):
        dealer, player = Poker.GameResult(3, 100, 100, 25)
        self.assertEqual((dealer, player), (100, 100))
        mock_print.assert_called_with('\nTie, All parties push')



if __name__ == "__main__":
    unittest.main()