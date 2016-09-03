
class Player(object):

	def __init__(self, display):
		self.display = display 
		self.name = ""
		self.health = ""
		self.sanity = ""
		self.inventory = ""


	#set health	
	def health_adjustment(self):
		pass


	#set sanity	
	def sanity_adjustment(self):
		pass


	def inventory(self):
		pass


	def player_reset(self, name):
		self.name = name
		self.health = "Sound In Body"
		self.sanity = "Sound In Mind"


	def get_health(self):
		return self.health


	def get_sanity(self):
		return self.sanity





