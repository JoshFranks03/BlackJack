# Blackjack Project

import random
from art import logo
from replit import clear

 
user_hand = []
dealer_hand = []

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calc_score(hand):

  found_ace = 0
  for i in hand:
    if i == 11:
      found_ace = 1

  score = sum(hand)

  if score > 21 and found_ace == 1:
    hand.append(1)
    hand.remove(11) 

  return score

def compare_scores(dealer, user):
  if dealer>user:
    return 1
  elif user>dealer:
    return 0
  else:
    return 2
def blackjack(newGame):
  if newGame == 1:
    user_hand.clear()
    dealer_hand.clear()
    
    user_hand.append(deal_card())
    user_hand.append(deal_card())
    
    dealer_hand.append(deal_card())
    dealer_hand.append(deal_card())

  print(f"Your cards are {user_hand}")
  print(f"dealer has a {dealer_hand[0]}")
  
  user_score = calc_score(user_hand)
  dealer_score = calc_score(dealer_hand)

  end_game = 0
  if user_score == 21:
    print("You have 21, you win!")
    end_game = 1
  elif user_score>21:
    print("Bust, you lose!")
    end_game = 1
  
  if dealer_score == 21:
    print("Dealer has 21, you lose!")
    end_game = 1
  elif dealer_score>21:
    print("Dealer Bust, you win!")
    end_game = 1
  

  if end_game == 0:
    cont_deal = input("Would you like another card? Type 'y' or 'n': ")
    if cont_deal == "y":
      user_hand.append(deal_card())
      blackjack(0)
    elif cont_deal == "n":
      while calc_score(dealer_hand) < 17:
        dealer_hand.append(deal_card())
        dealer_score = calc_score(dealer_hand)
        print(dealer_hand)
      if dealer_score == 21:
        print("Dealer has 21, you lose!")
        end_game = 1
      elif dealer_score>21:
        print("Dealer Bust, you win!")
        end_game = 1  
      elif dealer_score < 21 and dealer_score >= 17:
        winner = compare_scores(dealer_score, user_score)
        if winner == 0:
          end_game = 1
          print(f"Dealer has {dealer_hand}, your hand is {user_hand}. You win!!!")
        elif winner == 1:
          end_game = 1
          print(f"Dealer has {dealer_hand}, your hand is {user_hand}. You lose!!!")
        else:
          end_game = 1
          print(f"Dealer has {dealer_hand}, your hand is {user_hand}. It's a draw!!!")
      
  
    

    
    
def run_game():
  play = input("Would you like to play a game of blackjack? Type 'y' or 'n': ")
  if play == 'y':
    clear()
    print(logo)
    blackjack(1)
    run_game()
  clear()

run_game()
    









