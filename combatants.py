class Combatants(object):

	def __init__(self):
		pass


	def physical_combat (self):
		if random.randint(1, self.player_physical_attack) < random.randint(1, self.monster_physical_attack):
			display.player.health_adjustment(-1)
			return "lose"	
		else:
			return "win"			