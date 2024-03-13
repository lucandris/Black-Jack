import random

# Define card suits and ranks
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Player class
class Player:
		def __init__(self, name, money):
				self.name = name
				self.money = money
				self.hand = []

# Card class
class Card:
		def __init__(self, suit, rank):
				self.suit = suit
				self.rank = rank

		def get_value(self):
				# Assign values to face cards and Ace
				if self.rank in ['Jack', 'Queen', 'King']:
						return 10
				elif self.rank == 'Ace':
						return 11
				else:
						return int(self.rank)

# Deck class
class Deck:
		def __init__(self):
				self.cards = []
				# Create a deck with all combinations of suits and ranks
				for suit in suits:
						for rank in ranks:
								self.cards.append(Card(suit, rank))

		def shuffle(self):
				random.shuffle(self.cards)

		def deal_card(self):
				# Check if deck is empty, otherwise deal a card
				if len(self.cards) == 0:
						print("Deck is empty!")
						return None
				return self.cards.pop()

# Dealer class
class Dealer:
		def __init__(self):
				self.name = "Anastasia"
				self.money = 1000000
				self.hand = []

# Function to calculate hand value
def calculate_hand_value(hand):
		value = 0
		has_ace = False
		# Iterate through cards in hand
		for card in hand:
				card_value = card.get_value()
				value += card_value
				# Check for Ace and adjust value if necessary
				if card_value == 11:
						has_ace = True
		if has_ace and value > 21:
				value -= 10
		return value

# Deal cards to player and dealer
def deal_cards(deck, player, dealer):
		# Clear player and dealer hands
		player.hand.clear()
		dealer.hand.clear()
		# Deal two cards each to player and dealer
		for _ in range(2):
				player.hand.append(deck.deal_card())
				dealer.hand.append(deck.deal_card())

# Play the game
def play():
		print("Welcome to Blackjack!")
		name = input("Enter your name: ")
		money = int(input("Enter your starting money: "))
		player = Player(name, money)

		# Create dealer
		dealer = Dealer()

		while True:
				# Create deck and shuffle
				deck = Deck()
				deck.shuffle()

				# Get player's bet
				while True:
						bet = int(input(f"Enter your bet (enter 0 to quit): "))
						if bet == 0:
								print(f"Thanks for playing, {player.name}! Your remaining money is ${player.money}.")
								return
						elif bet > player.money:
								print(f"Insufficient funds. You have ${player.money} remaining.")
						else:
								break

				# Deal cards
				deal_cards(deck, player, dealer)

				# Player's turn
				print(f"\n{player.name}'s turn")
				player_value = calculate_hand_value(player.hand)
				print(f"Your cards: {[card.rank + ' of ' + card.suit for card in player.hand]}")
				print(f"Dealer's upcard: {dealer.hand[0].rank} of {dealer.hand[0].suit}")  # Display dealer's upcard
				print(f"Your hand value: {player_value}")

				while player_value < 21:
						choice = input("Do you want to hit or stand? (h/s) ")
						if choice.lower() == 'h':
								player.hand.append(deck.deal_card())
								player_value = calculate_hand_value(player.hand)
								print(f"Your cards: {[card.rank + ' of ' + card.suit for card in player.hand]}")
								print(f"Dealer's upcard: {dealer.hand[0].rank} of {dealer.hand[0].suit}")  # Display dealer's upcard
								print(f"Your hand value: {player_value}")
						else:
								break

				# Dealer's turn
				print("\nDealer's turn")
				dealer_value = calculate_hand_value(dealer.hand)
				print(f"Dealer's cards: {[card.rank + ' of ' + card.suit for card in dealer.hand]}")
				print(f"Dealer's hand value: {dealer_value}")

				while dealer_value < 17:
						dealer.hand.append(deck.deal_card())
						dealer_value = calculate_hand_value(dealer.hand)
						print(f"Dealer's cards: {[card.rank + ' of ' + card.suit for card in dealer.hand]}")
						print(f"Dealer's hand value: {dealer_value}")

				# Determine winner
				if player_value > 21:
						print(f"{player.name} busts! You lose ${bet}.")
						player.money -= bet
				elif dealer_value > 21 or player_value > dealer_value:
						print(f"{player.name} wins! You win ${bet}.")
						player.money += bet
				elif player_value == dealer_value:
						print(f"{player.name} pushes. No money won or lost.")
				else:
						print(f"{player.name} loses. You lose ${bet}.")
						player.money -= bet

				print(f"\nRemaining money: ${player.money}")

				# Check if player is out of money
				if player.money == 0:
						print("You're out of money! Game over.")
						return

play()