

class InputHandler (object):

	def __init__(self, display, player_input, player):
		self.display = display
		self.player_input = player_input
		self.player = player

	def input_start(self):			
		if self.player_input.player_selection == "n":
			self.display.location = "create_player"


	def input_create_player(self):
		self.player.player_reset(self.player_input.player_selection)
		self.display.location = "atrium"
		self.player_input.player_selection = ""


	def input_atrium(self):			
		#open the door
		if self.player_input.player_selection == "w":
			self.display.location = "atrium_closet"

		#turn and flee the house
		elif self.player_input.player_selection == "s":
			self.display.location = "exit"
			self.error = "error_insane"
			self.player.sanity_adjustment(-3)

		#room on right
		elif self.player_input.player_selection == "d":
			pass
			#TODO

		#room on left
		elif self.player_input.player_selection == "a":
			pass
			#TODO

	def input_atrium_closet(self):
		#slam the door
		if self.player_input.player_selection == "1":
			self.display.location == "atrium_monster_flee"
		
		#fight the serpent	
		elif self.player_input.player_selection == "2":
			if self.monster.physical_combat() == "win":
				self.display.location == "atrium_monster_fight_win"
			else:
				self.display.location == "atrium_monster_fight_lose"

	def input_menu_constants(self):		
		#quit
		if self.player_input.player_selection == "x":
			self.player.is_alive = False
	

	def input_validity_checker(self):
		#don't check player name
		if self.display.location == "create_player" or self.player_input.player_selection == "":
			self.player_input.list_of_possible_player_selections = []
			return self.player_input.player_selection
		else: 		
			#take all possible selections and compare them to input, if no match then return error
			list_of_matches = []
			for item in self.player_input.list_of_possible_player_selections:
				if self.player_input.player_selection == item:
					list_of_matches.append(item)

			if list_of_matches == []:
				self.error = "error1"				

		self.player_input.list_of_possible_player_selections = []


	#action based on player input		
	def menu_input_handler(self):

		if self.display.location == "start":
			self.input_start()

		elif self.display.location == "create_player":
			self.input_create_player()

		elif self.display.location == "atrium":
			self.input_atrium()			

		elif self.display.location == "atrium_closet":
			self.input_atrium_closet()

		self.input_menu_constants()	

		self.input_validity_checker()
