## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import random

def check_win(p_cards, c_cards):
    if p_cards > c_cards:
        print("You Won!")
    if c_cards > p_cards:
        print("You lose 😤")
    if p_cards == c_cards:
        print("DRAW!")

def deal_card():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10 ,10]
    return random.choice(cards)

another_game = "y"

another_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while another_game == 'y':
    player_cards = []
    dealer_cards = []
    another_card = "y"
    player_cards = [deal_card() for x in range(2)]
    dealer_cards = [deal_card() for x in range(2)]
    reveal_dealer_cards = 1
    while another_card == 'y' and sum(player_cards) < 21 and sum(dealer_cards) < 21:
        print(f"Your cards: {player_cards}, current score: " + str(sum(player_cards)))
        print("Computer\'s first card: " + str(dealer_cards[:reveal_dealer_cards]))

        another_card = input("Type 'y' to get another card, type 'n' to pass:")
        
        
        if another_card == 'y':
            player_cards.append(deal_card())
            dealer_cards.append(deal_card())
            
        elif another_card == 'n':
            while sum(dealer_cards) < 21:
                dealer_cards.append(deal_card())
            
            another_card = 'n'
        reveal_dealer_cards += 1
            
    print(f"Your final hand: {player_cards}, final score: " + str(sum(player_cards)))
    print(f"Computer\'s final hand: {dealer_cards}, final score: " + str(sum(dealer_cards)))        
    check_win(player_cards, dealer_cards)
    another_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if another_game == 'n':
        another_game = 'n'