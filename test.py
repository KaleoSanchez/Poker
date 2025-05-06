import unittest
import Poker

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
    
if __name__ == "__main__":
    unittest.main()