import os
import sys
import random
import textwrap

from player import Player

class Display(object):

	MENU_CONSTANTS = (
		"X = Quit",
	)
	
	DESCRIPTIONS = {
		"error1" : ("'{}' is an invalid option, please try again.",),
		"error2" : ("That name is too long. 10 characters or less, please.",),
		"error_insane" : ("Maybe a quiet cup of tea would help you regain a bit of sanity?",
			"GAME OVER",
			),
		"start" : ("Obsessed with the occult, a rumor has reached you that the fabled Eye Of Thoth can be found in the dilapidated mansion of arcane explorer Archibald Hammer.",
			"Ignoring the fact that Archibald hasn't been seen in 20 years and his mansion is supposedly 'haunted', you decide to pay Archie a little visit...",
			),
		"create_player" : ("What is your name?",),
		"exit" : ("That rug is far too ominous. You turn tail and flee into the night.", 
			"As the weeks pass, thoughts about your missed opportunity turn into an obsession. Then into a mania.",
			"Insanity insues.",
			),
		"atrium" : ("Lightning flashes as you kick in the front door. Clicking on your flashlight, you step across the threshold.", 
			"Playing your flashlight around the room you see an enormous chandelier glittering above a plush floor rug. In the dimness, it is hard to tell if the rugstain is wine or blood.",
			"Straight ahead is a closed door. Behind you is the exit. To the right appears to be a library. To the left an enormous dining hall.",
			),
		"atrium_closet" : ("Stepping forward across the winestained rug (blood?), you grasp the doorknob firmly and open the door.",
			"You are unsurprised to discover a closet full of moth eaten fur coats... and then a small movement pulls your eye to the shadowy floor.", 
			"The shadows are completely filled with the overlapping coils of the largest serpent you have ever seen."),
		"atrium_monster_flee" : ("Atrium Monster Flee Text",),
		"atrium_monster_fight_win" : ("Atrium Monster Fight Win Text",),
		"atrium_monster_fight_lose" : ("Atrium Monster Fight Lose Text",),

	}


	def __init__(self):
		self.text_width = 80
		self.player_selection = ""
		self.location = "start"
		self.error = "no_error"
		self.list_of_possible_player_selections = []



	def description(self):
		#description start
		for item in self.DESCRIPTIONS[self.location]:
			print("\t" + textwrap.fill(item, self.text_width))
			print("\n")
		


	def input_start(self):			
		if self.player_selection == "n":
			self.location = "create_player"


	def input_create_player(self):
		self.player.player_reset(self.player_selection)
		self.location = "atrium"
		self.player_selection = ""


	def input_atrium(self):			
		#open the door
		if self.player_selection == "w":
			self.location = "atrium_closet"

		#turn and flee the house
		elif self.player_selection == "s":
			self.location = "exit"
			self.error = "error_insane"
			self.player.sanity_adjustment(-3)

		#room on right
		elif self.player_selection == "d":
			pass
			#TODO

		#room on left
		elif self.player_selection == "a":
			pass
			#TODO

	def input_atrium_closet(self):
		#slam the door
		if self.player_selection == "1":
			self.location == "atrium_monster_flee"
		
		#fight the serpent	
		elif self.player_selection == "2":
			if self.monster.physical_combat() == "win":
				self.location == "atrium_monster_fight_win"
			else:
				self.location == "atrium_monster_fight_lose"

	def input_menu_constants(self):		
		#quit
		if self.player_selection == "x":
			self.player.is_alive = False
	

	def input_validity_checker(self):
		#don't check player name
		if self.location == "create_player" or self.player_selection == "":
			self.list_of_possible_player_selections = []
			return self.player_selection
		else: 		
			#take all possible selections and compare them to input, if no match then return error
			list_of_matches = []
			for item in self.list_of_possible_player_selections:
				if self.player_selection == item:
					list_of_matches.append(item)

			if list_of_matches == []:
				self.error = "error1"				

		self.list_of_possible_player_selections = []

	


	#print HUD
	def HUD (self, player):
		if player.name:		
			print("\tSANITY: {}\t\t{}\t\tHEALTH: {}".format(player.get_sanity(), player.name, player.get_health() ))


	#print title
	def title (self):
		print("\t╔╦╗┬ ┬┌─┐  ╔═╗┬ ┬┌─┐  ╔═╗┌─┐  ╔╦╗┬ ┬┌─┐┌┬┐┬ ┬")
		print("\t ║ ├─┤├┤   ║╣ └┬┘├┤   ║ ║├┤    ║ ├─┤│ │ │ ├─┤")
		print("\t ╩ ┴ ┴└─┘  ╚═╝ ┴ └─┘  ╚═╝└     ╩ ┴ ┴└─┘ ┴ ┴ ┴")
	

	#identify and print error type	
	def error_message (self):
		if self.error != "no_error": 
			print("\t*" * 5)

			if self.error == "error1":
				print("\t" + textwrap.fill(self.DESCRIPTIONS["error1"], self.text_width).format(self.player_selection))

			else:
				for item in self.DESCRIPTIONS[self.error]:
					print("\t" + textwrap.fill(item, self.text_width))
			
			print("\t*" * 5 + "\n")
			self.error = "no_error"


	def print_menu_constants(self):
		#player input
		if self.location != "create_player" and self.location != "exit":	
			for option in self.MENU_CONSTANTS:
				print("\t" + option)

			print("\n\tWhat would you like to do?")


	#after every action, create new screen	
	def rebuild_display (self):

		#wipe screen
		os.system('clear')
		# print("*" * 10)
		# print("room = " + self.location)

		#title
		self.title()

		#HUD
		self.HUD(Player())
		print("\n")

		#description

		self.description()
		print("\n")

		#error messages
		self.error_message()

		#room specific menu actions
		self.room.print_action_options()

		#room specific menu movements
		self.room.print_movement_options()

		#standard menu options
		self.print_menu_constants()


	#get player input
	def player_gives_input(self):
		if self.location == "create_player":
			self.player_selection = input("\tEnter Your Name > ")
		else:	
			self.player_selection = input("\t> ").lower()
			self.list_of_possible_player_selections.append(self.player_selection)


	#action based on player input		
	def menu_input_handler(self):

		if self.location == "start":
			self.input_start()

		elif self.location == "create_player":
			self.input_create_player()

		elif self.location == "atrium":
			self.input_atrium()			

		elif self.location == "atrium_closet":
			self.input_atrium_closet()

		self.input_menu_constants()	

		self.input_validity_checker()
