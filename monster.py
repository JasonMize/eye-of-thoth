import random


class Monster(object):

	def __init__(self, display):
		self.player_physical_attack = 4
		self.monster_physical_attack = 6
		self.player_dispel_ability = 4
		self.monster_dispel_resistance = 6


	def physical_combat (self):
		if random.randint(1, self.player_physical_attack) < random.randint(1, self.monster_physical_attack):
			display.player.health_adjustment(-1)
			return "lose"	
		else:
			return "win"	