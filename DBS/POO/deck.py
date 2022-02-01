import random

class card(object):
	"""docstring for ClassName"""
	def __init__(self, suit, value):
		self.suit = suit
		self.val = value
	
	def show(self):
		print("{} of {}".format(self.val, self.suit))


class deck(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.cards = []
		self.build()

	def build(self):
		for fam in ['Spides', 'Cubs', 'Diamon', 'Heart']:
			for num in range(1, 15):
				self.cards.append(card(fam, num))
				# Here we send the card to card class!

	def show(self):
		for c in self.cards:
			c.show()



	def shuffle(self):
		for i in range(len(self.cards)-1, 0, -1):
			r = random.randint(0, i)
			self.cards[i], self.cards[r] = self.cards[r], self.cards[i]


	def draw(self):
		return self.cards.pop()


class player(object):
	"""docstring for ClassName"""
	def __init__(self, name):
		self.name = name
		self.hand = []

	def drawcard(self, deck):
		self.hand.append(deck.draw())
		return self

	def showhand(self):
		print('{} has:'.format(self.name))
		for card in self.hand:
			card.show()


deck = deck()
deck.shuffle()


play = player('Bob')
play.drawcard(deck).drawcard(deck)
play.showhand()

