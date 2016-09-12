

# class InputHandler (object):

# 	def __init__(self, display, player_input, player, combatants):
# 		self.display = display
# 		self.player_input = player_input
# 		self.player = player
# 		self.combatants = combatants
	


# 	def input_start(self):			
# 		self.player_input.list_of_possible_player_selections.append("n")
# 		if self.player_input.player_selection == "n":
# 			self.display.location = "create_player"


# 	def input_create_player(self):
# 		self.player.player_reset(self.player_input.player_selection)
# 		self.display.location = "atrium"
# 		self.player_input.player_selection = ""


# 	def input_atrium(self):			
# 		self.player_input.list_of_possible_player_selections.append("w")
# 		self.player_input.list_of_possible_player_selections.append("s")
# 		#turn and flee the house
# 		if self.player_input.player_selection == "s":
# 			self.display.location = "exit"
# 			self.player.sanity_adjustment(-3)
# 		#open the door
# 		elif self.player_input.player_selection == "w":
# 			self.display.location = "atrium_closet"



# 	def input_atrium_closet(self):
# 		self.player_input.list_of_possible_player_selections.append("1")
# 		self.player_input.list_of_possible_player_selections.append("2")

# 		#slam the door
# 		if self.player_input.player_selection == "1":
# 			self.display.location = "atrium_monster_flee"

# 		#fight the serpent	
# 		elif self.player_input.player_selection == "2":
# 			self.combatants.physical_combat()
			
			

# 	def input_atrium_fight_loop(self):
# 		self.player_input.list_of_possible_player_selections.append("1")
# 		self.player_input.list_of_possible_player_selections.append("2")
# 		#punch the snake		
# 		if self.player_input.player_selection == "1":
# 			self.combatants.physical_combat() 
# 		#exorcism
# 		elif self.player_input.player_selection == "2":
# 			self.combatants.mystical_combat()	
			

# 	def input_atrium_monster_dead(self):			
# 		pass

# 	def input_atrium_monster_insane(self):
# 		pass

# 	def input_menu_constants(self):		
# 		self.player_input.list_of_possible_player_selections.append("x")

# 		#quit
# 		if self.player_input.player_selection == "x":
# 			self.player.is_alive = False
	


# 	#action based on player input		
# 	def menu_input_handler(self):

# 		if self.display.location == "start":
# 			self.input_start()

# 		elif self.display.location == "create_player":
# 			self.input_create_player()

# 		elif self.display.location == "atrium":
# 			self.input_atrium()			

# 		elif self.display.location == "atrium_closet":
# 			self.input_atrium_closet()

# 		elif (self.display.location == "atrium_monster_fight_win" 
# 			or self.display.location == "atrium_monster_fight_lose" 
# 			or self.display.location == "atrium_monster_flee"
# 			or self.display.location == "atrium_fight_loop_physical_win"
# 			or self.display.location == "atrium_fight_loop_physical_lose"
# 			or self.display.location == "atrium_fight_loop_mystical_win"
# 			or self.display.location == "atrium_fight_loop_mystical_lose"):

# 			self.input_atrium_fight_loop()	

# 		elif self.display.location == "atrium_monster_dead":
# 			self.input_atrium_monster_dead()

# 		elif self.display.location == "atrium_monster_insane":
# 			self.input_atrium_monster_insane()	

# 		self.input_menu_constants()	

# 		self.player_input.input_validity_checker()
