import random

card_list = [
    'Ace of Hearts',
    'Ace of Diamonds',
    'Ace of Spades',
    'Ace of Clubs',
    'King of Hearts',
    'King of Diamonds',
    'King of Spades',
    'King of Clubs',
    'Queen of Hearts',
    'Queen of Diamonds',
    'Queen of Spades',
    'Queen of Clubs',
    'Jack of Hearts',
    'Jack of Diamonds',
    'Jack of Spades',
    'Jack of Clubs',
    '10 of Hearts',
    '10 of Diamonds',
    '10 of Spades',
    '10 of Clubs',
    '9 of Hearts',
    '9 of Diamonds',
    '9 of Spades',
    '9 of Clubs',
    '8 of Hearts',
    '8 of Diamonds',
    '8 of Spades',
    '8 of Clubs',
    '7 of Hearts',
    '7 of Diamonds',
    '7 of Spades',
    '7 of Clubs',
    '6 of Hearts',
    '6 of Diamonds',
    '6 of Spades',
    '6 of Clubs',
    '5 of Hearts',
    '5 of Diamonds',
    '5 of Spades',
    '5 of Clubs',
    '4 of Hearts',
    '4 of Diamonds',
    '4 of Spades',
    '4 of Clubs',
    '3 of Hearts',
    '3 of Diamonds',
    '3 of Spades',
    '3 of Clubs',
    '2 of Hearts',
    '2 of Diamonds',
    '2 of Spades',
    '2 of Clubs'   
]

# variables that will hold certain statistics (i.e. how often a player got a 
# pocket pair, and how often they did not)
pocket_pairs = 0
no_pocket_pairs = 0
flop_pair_low = 0
flop_pair_high = 0
pair_low = 0
pair_high = 0

face_counts = {}
suit_counts = {}

def random_card():
    return playing_cards.pop(random.randint(0,(len(playing_cards)-1)))

def deal_hand():
    hand.append(random_card())
    hand.append(random_card())
    print(hand)

def deal_table():
    table.append(random_card())
    table.append(random_card())
    table.append(random_card())
    table.append(random_card())
    table.append(random_card())
    print(table)

def increment_card_count(my_string):
    of_place = my_string.find('of')
    card_name = my_string[0:of_place-1]
    suit = my_string[of_place+3:]

    if face_counts.get(card_name):
        face_counts[card_name] = face_counts.get(card_name) + 1
    else:
        face_counts[card_name] = 1
    
    if suit_counts.get(suit):
        suit_counts[suit] = suit_counts.get(suit) + 1
    else:
        suit_counts[suit] = 1

def check_for_pocket_pair():
    global pocket_pairs
    global no_pocket_pairs
    # if both cards are the same face, there will be only 1 key:value pair in the dictionary - face_counts
    if 1 == len(face_counts):
        pocket_pairs += 1
    else:
        no_pocket_pairs += 1

for x in range(1,10001):

    # make a copy of the deck of cards for each round of the game
    playing_cards = card_list[:]

    hand = []
    table = []
    deal_hand()
    deal_table()
    print('\n\n')

    face_counts = {}
    suit_counts = {}

    for card in hand:
        increment_card_count(card)

    # print("Face counts:")
    # print(face_counts)

    # print("Suit counts:")
    # print(suit_counts)

    check_for_pocket_pair()

    print('\n\n')

print('Stats - ')
print('pocket pairs: ', pocket_pairs)
print('no pocket pairs: ', no_pocket_pairs)
print('% that were pocket pairs: ', str(round((pocket_pairs / no_pocket_pairs) * 100, 2)) + '%')

