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




	def __init__(self):
		super(DisplayRoom, self).__init__()
		self.room_south = ""
		self.room_north = ""
		self.room_east = ""
		self.room_west = ""


	#print action options for various rooms	
	def print_action_options(self):
		MENU_ACTION_START = {
			"N" : "N = New Character",
		}
		MENU_ACTION_ATRIUM_CLOSET = {
			"1" : "1. = Slam The Closet Door",
			"2" : "2. = Crush The Serpent Head Beneath Your Heel",
		}

		if self.location == "start":
			for key, value in MENU_ACTION_START.items():
				if key == "N":
					print ("\t" + value)				

		elif self.location == "atrium_closet":
			for key, value in MENU_ACTION_ATRIUM_CLOSET.items():
				print ("\t" + value)



	#print movement options for various rooms	
	def print_movement_options(self):
		MENU_MOVEMENT_ATRIUM = {
			"W" : "W = Open The Door",
			"S" : "S = Turn And Flee The House",
			"D" : "D = Enter The Library",
			"A" : "A = Enter The Dining Hall",
		}

		if self.location == "atrium":
			for key, value in MENU_MOVEMENT_ATRIUM.items():
				print("\t" + value)
	


