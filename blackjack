import random

suits = [u"\u2666", u"\u2665", u"\u2663", u"\u2660"]
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
def shuffle_deck(suits, cards):
    deck = []
    for suit in suits:
        for card in cards:
            deck.append(card + ' ' + suit)
    random.shuffle(deck)
    return deck

def deal_card(deck):
    card = deck.pop()
    return card

def count_score(hand):
    score_ace_one = 0
    score_ace_eleven = 0
    for card in hand:
        if card.split()[0] not in ['A', 'K', 'Q', 'J']:
            score_ace_one += int(card.split()[0])
            score_ace_eleven += int(card.split()[0])
        elif card.split()[0] != 'A':
            score_ace_one += 10
            score_ace_eleven += 10
    for card in hand:
        if card.split()[0] == 'A':
            score_ace_one += 1
            score_ace_eleven += 11
    
    selected_score = 0
    if max(score_ace_one, score_ace_eleven) > 21:
        selected_score += score_ace_one
    else:
        selected_score += score_ace_eleven
    return selected_score
            
def play_game():
    
    deck = shuffle_deck(suits, cards)
    dealer_cards = []
    player_cards = []
    dealer_score = 0
    player_score = 0
    player_cards.append(deal_card(deck))
    dealer_cards.append(deal_card(deck))
    player_cards.append(deal_card(deck))
    dealer_score += count_score(dealer_cards)
    player_score += count_score(player_cards)
    print(f'Dealer cards are: {dealer_cards}')
    print(f'Dealer score is: {dealer_score}')
    print(f'Player cards are: {player_cards}')
    print(f'Player score is: {player_score}')
    print()
    print()
    
    while player_score < 21: 
        action = input('Stand (s) or Hit(h)?')
        if action == 's':
            print(f'You stood with a score of {player_score}')
            break
        if action == 'h':
            player_cards.append(deal_card(deck))
            player_score = count_score(player_cards)
            print(f'Player cards are: {player_cards}')
            print(f'Player score is: {player_score}')
    
    while dealer_score <= 16:
        dealer_cards.append(deal_card(deck))
        dealer_score = count_score(dealer_cards)
    
    while True:
        if player_score == 21 and len(player_cards) == 2:
            print(f'You got a blackjack!')
            break
        if player_score > 21:
            print(f'You busted with a score of {player_score}')
            break
        elif dealer_score > 21:
            print(f'Dealer cards are: {dealer_cards}')
            print(f'Dealer has busted with a score of {dealer_score}')
            break
        elif player_score > dealer_score:
            print(f'Dealer cards are: {dealer_cards}')
            print(f'Dealer score is {dealer_score}. Player wins with a score of {player_score}.')
            break
        elif dealer_score > player_score:
            print(f'Dealer cards are: {dealer_cards}')
            print(f'Dealer score is {dealer_score}. Dealer wins.')
            break
        elif dealer_score == player_score:
            print(f'Dealer cards are: {dealer_cards}')
            print(f'Dealer score is {dealer_score}. You tie.')
            break
        
play_game()