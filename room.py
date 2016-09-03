
class Room (object):
	
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
		self.room_south = ""
		self.room_north = ""
		self.room_east = ""
		self.room_west = ""


	#print movement options for various rooms	
	def movement_options(self):
		MENU_ATRIUM = {
			"W" : "W = Open The Door",
			"S" : "S = Turn And Flee The House",
			"D" : "D = Enter The {}",
			"A" : "A = Enter The {}",
		}

		if self.display.location == "atrium":
			for key, value in MENU_ATRIUM.items():
				if key == "W":
					print("\t" + value)
				elif key == "S":
					print("\t" + value)	
				elif key == "D":	
					print("\t" + value.format(self.room_east))
				elif key == "A":
					print("\t" + value.format(self.room_west))	
		

	def monster(self):
		pass	

 


