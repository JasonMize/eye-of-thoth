import random

class Combatants(object):

	def __init__(self, player, monster, display):
		self.player = player
		self.monster = monster
		self.display = display


	def physical_combat (self):
		player_attack = random.randint(1, self.player.player_physical_attack)
		print("player physical attack: " + str(player_attack))

		monster_attack = random.randint(1, self.monster.monster_physical_attack)
		print("monster physical attack: " + str(monster_attack))

		if self.player.is_alive and self.monster.is_alive:
			if self.display.location == "atrium_closet":
				if player_attack <= monster_attack:		
					self.player.health_adjustment(-1)
					self.display.location = "atrium_monster_fight_lose"	

				elif player_attack > monster_attack:
					self.monster.monster_health_adjustment(-1)
					return "win"
					self.display.location = "atrium_monster_fight_win"	
			
			elif (self.display.location == "atrium_fight_loop_physical_win"
				or self.display.location == "atrium_fight_loop_physical_lose"):
				
				if player_attack <= monster_attack:
					self.player.health_adjustment(-1)
					self.display.location = "atrium_fight_loop_physical_lose"

				elif player_attack > monster_attack:
					self.monster.monster_health_adjustment(-1)
					return "win"
					self.display.location = "atrium_fight_loop_physical_win"		

					

	def mystical_combat (self):
		print ("I'm in mystical COMBAT!")
		player_attack = random.randint(1, self.player.player_mystical_attack)
		print("player mystical attack: " + str(player_attack))

		monster_attack = random.randint(1, self.monster.monster_mystical_attack)
		print("monster mystical attack: " + str(monster_attack))
		
		if self.player.is_alive and self.monster.is_alive:
			if (self.display.location == "atrium_fight_loop_mystical_win"
				or self.display.location == "atrium_fight_loop_mystical_lose"):

				if player_attack <= monster_attack:
					self.player.sanity_adjustment(-1)
					self.display.location = "atrium_fight_loop_mystical_lose"

				elif player_attack > monster_attack:
					self.monster.monster_sanity_adjustment(-1)
					return "win"
					self.display.location = "atrium_fight_loop_mystical_win"		










