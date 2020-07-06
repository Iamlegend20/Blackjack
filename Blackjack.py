import random

suits = ('Hearts', 'Spades', 'Clubs', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]                                                                                                                                                                                                                     
		
	def __str__(self):
		return f'{self.rank} of {self.suit}'

class Deck:
	def __init__(self):
		self.cards = []
		for suit in suits:
			for rank in ranks:
				self.cards.append(Card(suit,rank))
	def __str__(self):
		x = 'The deck contains:\n'
		for num,card in enumerate(self.cards,1):
			x += f'  {num}. {card}\n'
		return x
	def deal_card(self):
		return self.cards.pop(0)
		
		
class Hand:		
	def __init__(self):
		self.cards = []
		self.value_total = 0
	def show_hand(self):
		for card in self.cards:
			print(card)
	def add_card(self,card):
		self.cards.append(card)
		self.value_total += card.value

class Chips:
	def __init__(self):
		self.value = 100


			
deck = Deck()
random.shuffle(deck.cards)
player_hand = Hand()
dealer_hand = Hand()

player_hand.add_card(deck.deal_card())
player_hand.add_card(deck.deal_card())
dealer_hand.add_card(deck.deal_card())
dealer_hand.add_card(deck.deal_card())

player_hand.show_hand()
dealer_hand.show_hand()
print(player_hand.value_total)
