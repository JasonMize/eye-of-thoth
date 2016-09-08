
class Monster(object):

	def __init__(self, display, display_room, player_input):
		self.display = display
		self.display_room = display_room
		self.player_input = player_input
		self.monster_physical_attack = 100
		self.monster_mystical_attack = 100
		self.monster_health = 3
		self.monster_sanity = 3
		self.is_alive = True


	#set health	
	def monster_health_adjustment(self, adjustment):
		self.monster_health += adjustment
		print ("monster health: " + str(self.monster_health))
		if self.monster_health <= 1:
			self.monster_health = 1
			self.display.location = "atrium_monster_dead"
			self.display.error = "monster_dead"
			


	#set sanity	
	def monster_sanity_adjustment(self, adjustment):
		self.monster_sanity += adjustment
		print ("monster sanity: " + str(self.monster_sanity))
		if self.monster_sanity <= 1:
			self.monster_sanity = 1
			self.display.location = "atrium_monster_insane"
			self.display.error = "monster_insane"
			