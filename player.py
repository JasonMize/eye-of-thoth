
class Player(object):

	HEALTH = {
		4 : "Sound In Body",
		3 : "Battered",
		2 : "On Death's Doorstep",
		1 : "Dead",
	}
  
	SANITY = {
		4 : "Sound In Mind",
		3 : "Unhinged", 
		2 : "Dangerously Bizarre",
		1 : "Insane",
	}


	def __init__(self):
		self.is_alive = True
		self.name = ""
		self.health = 4
		self.sanity = 4
		self.inventory = ""


	#set health	
	def health_adjustment(self, adjustment):
		self.health += adjustment
		if self.healh <= 1:
			self.health = 1
			self.display.rebuild_display()
			self.display.is_alive = False


	#set sanity	
	def sanity_adjustment(self, adjustment):
		self.sanity += adjustment
		print (self.sanity)
		if self.sanity <= 1:
			self.sanity = 1
			self.display.rebuild_display()
			self.display.is_alive = False


	def inventory(self):
		pass


	def player_reset(self, name):
		self.name = name
		self.health = 4
		self.sanity = 4


	def get_health(self):
		return self.HEALTH[self.health]


	def get_sanity(self):
		return self.SANITY[self.sanity]





