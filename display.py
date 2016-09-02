import os
import sys
import textwrap
from player import Player

text_width = 80
player_selection = ""

class Display(object):

	MENU_NO_PLAYER = (
		"1. New Character",
		"2. Load Game",
		"0. Quit",
	)
	
	DESCRIPTIONS = {
		"start1" : "Obsessed with the occult, a rumor has reached you that the fabled Eye Of Thoth can be found in the dilapidated mansion of arcane explorer Archibald Hammer.",
		"start2" : "Ignoring the fact that Archibald hasn't been seen in 20 years and his mansion is supposedly 'haunted', you decide to pay Archie a little visit...",
	}



	def __init__(self):
		pass

	def menu_options (self):
		print ("1. save game")
		print ("2. load game")	

	def menu_options_no_player(self, player_selection):
		if player_selection == "0":
			sys.exit
		elif player_selection == "1":
			self.rebuild_display("create_player", player_selection)
		elif player_selection == "2":
			pass
		else:
			self.display_selection_error(player_selection)

	#get player input
	def player_input(self):
		print("\n\tWhat would you like to do?")
		player_selection = input("\t> ")
		return player_selection		


	def display_selection_error(self, player_selection):
		if player_selection.isdigit():
			self.rebuild_display(location="error1", player_selection=player_selection)
		else:
			self.rebuild_display(location="error2", player_selection=player_selection)
	
	def description(self, location, player_selection):
		#player doesn't exist (dead or new game)	
		if location == "start":
			print("\t" + textwrap.fill(self.DESCRIPTIONS["start1"], text_width))
			print("\n")
			print("\t" + textwrap.fill(self.DESCRIPTIONS["start2"], text_width))

		elif location == "error1":
			print("\n'{}' is an invalid option, please try again"
				.format(player_selection))
		
		elif location == "error2":
			print("\n'{}' is not a number. Please select a number from the options below."
				.format(player_selection))
		
		elif location =="create_player":
			Player.player_creation(self)
	


	#after every action, create new screen	
	def rebuild_display (self, location="start", player_selection=player_selection):

		#wipe screen
		os.system('clear')
	
		#title
		print("\t╔╦╗┬ ┬┌─┐  ╔═╗┬ ┬┌─┐  ╔═╗┌─┐  ╔╦╗┬ ┬┌─┐┌┬┐┬ ┬")
		print("\t ║ ├─┤├┤   ║╣ └┬┘├┤   ║ ║├┤    ║ ├─┤│ │ │ ├─┤")
		print("\t ╩ ┴ ┴└─┘  ╚═╝ ┴ └─┘  ╚═╝└     ╩ ┴ ┴└─┘ ┴ ┴ ┴")
		print("\n")

		#description
		self.description(location, player_selection)
		print("\n")

		#print menu options
		for option in self.MENU_NO_PLAYER:
			print("\t" + option)

		player_selection = self.player_input()	

		self.menu_options_no_player(player_selection)

		print("\n")





