import random
import time

bet = 0

def main():
    PlayerMoney = 100
    DealerMoney = 100
    again = 'y'
    while again == 'y':
        Deck = deck()
        DeckPosition = 0
        print("Welcome to Reno Poker!, I'll shuffle the deck!\n")
        random.shuffle(Deck)
        time.sleep(1)
        print("Deck has been shuffled, here is your hand!\n")
        time.sleep(0.5)
        PlayerHand = []
        for _ in range(5):
            PlayerHand.append(Deck[DeckPosition])
            CardName(PlayerHand[-1])
            DeckPosition += 1
            time.sleep(0.5)

        DealerHand = []
        for _ in range(5):
            DealerHand.append(Deck[DeckPosition])
            DeckPosition += 1

        BetIsValid = False
        while not BetIsValid:
            print('\nYou have', PlayerMoney, 'Dollars')
            bet = int(input('\nWould you like to place a bet? If so, how much?\n'))
            BetIsValid = ValidBet(PlayerMoney,bet)
        print('Would you like a redeal? use numbers 1-5 to select your card, press 0 to submit')
        Menu = True
        Select = [0, 0, 0, 0, 0]

        while Menu:
            for i in range(5):
                if Select[i] == 1:
                    print('Swapping out your ', end='')
                else:
                    print('Keeping your ', end='')
                CardName(PlayerHand[i])
            choice = input('\n')
            if choice.isdigit() and 0 <= int(choice) <= 5:
                choice = int(choice)
                if choice == 0:
                    Menu = False
                else:
                    Select[choice - 1] = 1 - Select[choice - 1]

        print("Redealing... here is your hand!\n")
        for i in range(5):
            if Select[i] == 1:
                PlayerHand[i] = Deck[DeckPosition]
                DeckPosition += 1
            CardName(PlayerHand[i])
            time.sleep(0.5)

        totalbet = bet + int(input('\nBet more?? If so how much'))
        while totalbet > PlayerMoney:
            print('Bet is not valid, returning to bet input')
            totalbet = 0
            totalbet = bet + int(input('\nBet more? If so, how much?\n'))

        print('Total bet is', totalbet, 'dollars\n')
        time.sleep(2)

        print('Dealer\'s Hand:\n')
        ShowHand(DealerHand)
        result = DidPlayerWinner(PlayerHand, DealerHand)
        GameResult(result,PlayerMoney,DealerMoney,totalbet)
        print('\nYour Money:', PlayerMoney)
        print('Dealer Money:', DealerMoney)
        again = MoneyLeft(PlayerMoney, DealerMoney)
        
    print('\nThanks for Playing!')

def HandRank(x):
    eval = sorted([(card % 13) + 1 for card in x])
    suit = [card // 13 for card in x]

    if len(set(suit)) == 1:  # Flush
        return 5

    straight = all(eval[i] == eval[0] + i for i in range(1, 5))
    straight_ace_low = eval == [1, 2, 3, 4, 13]

    if straight or straight_ace_low:
        return 6 if straight else 1

    counts = [eval.count(card) for card in set(eval)]
    max_count = max(counts)

    if max_count == 4:  # Four of a Kind
        return 3
    if max_count == 3 and 2 in counts:  # Full House
        return 4
    if max_count == 3:  # Three of a Kind
        return 7
    if max_count == 2 and counts.count(2) == 2:  # Two Pair
        return 8
    if max_count == 2:  # Pair
        return 9
    return 10  # High Card

def DidPlayerWinner(x, y):
    rank_x = HandRank(x)
    rank_y = HandRank(y)
    if rank_x < rank_y:
        return 1
    elif rank_x > rank_y:
        return 2
    else:
        return 3

def CardName(card):
    value = (card % 13) + 1
    suit = card // 13
    print(f"{GetCardValue(value)} of {GetCardSuit(suit)}")

def GetCardValue(value):
    if value == 1:
        return "Deuce"
    elif 2 <= value <= 10:
        return str(value)
    elif value == 11:
        return "Jack"
    elif value == 12:
        return "Queen"
    elif value == 13:
        return "King"
    else:
        return "Ace"

def GetCardSuit(suit):
    suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
    return suits[suit]

def deck():
    Deck = list(range(52))
    return Deck

def ShowHand(hand):
    for card in hand:
        CardName(card)

def MoneyLeft(playerMoney, dealerMoney):
    returnvalue = 'NULL'
    if dealerMoney == 0:
        print('You beat the Dealer!!')
        returnvalue = 'n'
        return returnvalue
    if playerMoney == 0:
        print('You went broke, Too Bad.')
        returnvalue = 'n'
        return returnvalue
    else: 
        returnvalue = 'y'
        return returnvalue 

def ValidBet(PlayerMoney,bet):
    if bet <= PlayerMoney:
        print('Betting', bet, 'dollars')
        return True
    else:
        print('Bet is not valid, returning to bet input')
        bet = 0
        return False

def GameResult(result, PlayerMoney,DealerMoney,totalbet):
    if result == 1:
        print('\nPlayer Wins!, You win', totalbet, 'dollars!')
        PlayerMoney += totalbet
        DealerMoney -= totalbet
        return DealerMoney, PlayerMoney
    elif result == 2:
        print('\nDealer Wins!, You Lose', totalbet, 'dollars!')
        PlayerMoney -= totalbet
        DealerMoney += totalbet
        return DealerMoney, PlayerMoney
    else:
        print('\nTie, All parties push')
        return DealerMoney, PlayerMoney


if __name__ == "__main__": 
    main()