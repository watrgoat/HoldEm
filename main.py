import random

# Card class representing a single playing card
class Card:
    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# Deck class representing a deck of 52 playing cards
class Deck:
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    def __init__(self) -> None:
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.cards)
        random.shuffle(self.cards)
    
    def probability(self, card):
        if card in self.cards:
            return 1/len(self.cards)
        else:
            return 0

    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self, cards) -> None:
        self.cards = cards

    def add_card(self, card):
        self.cards.append(card)
        return

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)
    

def game():
    pot = 0

    # generate shuffled deck
    game_deck = Deck()

    # player antes 1$
    ante = int(input("Input the initial bet amount: "))
    pot += ante

    # player is dealt 2 cards, so is dealer
    player_cards = (game_deck.deal_card(), game_deck.deal_card())
    player_hand = Hand(player_cards)
    dealer_cards = (game_deck.deal_card(), game_deck.deal_card())
    dealer_hand = Hand(dealer_cards)

    # player checks cards
    print(f'Your hand is: {player_hand}')
    
    # player decides to fold losing the ante or double their initial ante
    while True:
        response = input(f"Do you bet double your ante ({ante*2}$) or fold (d or f): ")
        if response == 'd':
            break
        elif response == 'f':
            return
        else:
            print('Invalid input. Try again.')
            print()





    # 3 cards are dealt to the board (will become 5)
    # player chooses to bet ante (1$) again or check risking no more money
    pass

game()


# pop the top two
# check probability of opponent having better cards (define better cards)
# if hand is in top 70% continue
# pop 3 for flop

'''
# Function to determine the winner based on hand rankings
def determine_winner(hands):
    ranks = ["High Card", "One Pair", "Two Pair", "Three of a Kind", "Straight",
             "Flush", "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]

    scores = []
    for hand in hands:
        score = 0
        for card in hand.cards:
            score += Deck.ranks.index(card.rank) + 2
        scores.append(score)

    max_score = max(scores)
    winners = [i for i, score in enumerate(scores) if score == max_score]

    if len(winners) == 1:
        return f"Player {winners[0] + 1} wins with {ranks[max_score - 2]}"

    winner_str = ", ".join(str(winner + 1) for winner in winners)
    return f"Players {winner_str} tie with {ranks[max_score - 2]}"


# Main game function
def play_game(num_players):
    deck = Deck()
    deck.shuffle()

    players = [Hand() for _ in range(num_players)]
    for _ in range(2):
        for player in players:
            player.add_card(deck.deal_card())

    community_cards = Hand()
    for _ in range(5):
        community_cards.add_card(deck.deal_card())

    print("Community Cards: ", community_cards)
    for i, player in enumerate(players):
        print(f"Player {i + 1} Cards: ", player)

    print(determine_winner(players))


# Play the game with 2 players
play_game(2)
'''