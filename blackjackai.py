import random

class Card:


	def __init__(self, suit, rank, value, value2):

		self.suit = suit

		self.rank = rank

		self.value = value

		self.value2 = value2


	def printCard(self):

		print(self.suit)
		print(self.rank)
		print(self.value) 




class Player:

	def __init__(self, total, hand):

		self.total = total

		self.hand = hand



def shuffle(self):




		


sample = Card('Hearts', 'Queen', 10, 0)
sample.printCard()	

deck = []
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
val = 0
val2 = 0
startingHand = []




for i in range(4):

	

	for j in range(13):

		if(j == 0):

			val = 1
			val2 = 11
		elif(j == 11 or j == 12 or j == 13):

			val = 10
			val2 = 0
		else:

			val = j+1
			val2 = 0
			
			



		temp = Card(suits[i], ranks[j], val, val2)
		deck.append(temp)



#while loop here
random.shuffle(deck)










