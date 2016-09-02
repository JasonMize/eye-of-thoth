
class Player(object):

	def __init__(self, display):
		self.display = display 
		self.name = ""
		self.health = "Sound In Body"
		self.sanity = "Sound In Mind"
		self.inventory = ""

	def health(self):
		pass

	def sanity(self):
		pass

	def inventory(self):
		pass

	def player_creation(self):
		print ("\tWhat is your name?")
		self.name = input("\t> ")
		self.display.rebuild_display(location="atrium")

		







