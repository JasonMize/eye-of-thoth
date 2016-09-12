from display import Display


class DisplayRoom (Display):
	
	ROOM = (
		"Library", 
		"Dungeon",
		"Dining Room",
		"Master Bedroom",
		"Music Library",
		"Observatory",
		"Torture Chamber",
		"Conservatory",
		"Furnace Room",
	)


	def __init__(self, display):
		self.display = display


	#print action options for various rooms	
	def print_action_options(self):
		MENU_ACTION_START = {
			"N" : "N = New Character",
		}
		MENU_ACTION_ATRIUM_CLOSET = {
			"1" : "1 = Slam The Closet Door",
			"2" : "2 = Crush The Serpent Head Beneath Your Booted Heel",
		}
		MENU_ACTION_ATRIUM_MONSTER_FIGHT = {
			"1" : "1 = Punch That Snake!",
			"2" : "2 = Exorcism!",
		}

		if self.display.error != "error_dead" and self.display.error != "error_insane":
			if self.display.location == "start":
				for key, value in sorted(MENU_ACTION_START.items()):
					if key == "N":
						print ("\t" + value)	
			
			elif self.display.location == "atrium_closet":
				for key, value in sorted(MENU_ACTION_ATRIUM_CLOSET.items()):
					print ("\t" + value)

			elif (self.display.location == "atrium_monster_fight_win" 
				or self.display.location == "atrium_monster_flee" 
				or self.display.location == "atrium_monster_fight_lose"
				or self.display.location == "atrium_fight_loop_physical_win"
				or self.display.location == "atrium_fight_loop_physical_lose"
				or self.display.location == "atrium_fight_loop_mystical_win"
				or self.display.location == "atrium_fight_loop_mystical_lose"):

				for key, value in sorted(MENU_ACTION_ATRIUM_MONSTER_FIGHT.items()):
					print ("\t" + value)			

			elif (self.display.location == "atrium_monster_dead" 
				or self.display.location == "atrium_monster_insane"):
				pass

	#print movement options for various rooms	
	def print_movement_options(self):
		MENU_MOVEMENT_ATRIUM = {
			"W" : "W = Open The Door",
			"S" : "S = Turn And Flee The House",
		}

		if self.display.location == "atrium":
			for key, value in sorted(MENU_MOVEMENT_ATRIUM.items()):
				print("\t" + value)
	


