import os
import sys
import textwrap
from player import Player


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

	def menu_options_no_player(self):
		player_selection = ""

		#print menu options
		for option in self.MENU_NO_PLAYER:
			print("\t" + option)

		print("\n\tWhat would you like to do?")
		player_selection = input("\t> ")

		if player_selection == "0":
			sys.exit
		elif player_selection == "1":
			print ("choice 1")
			self.rebuild_display()	
		elif player_selection == "2":
			print ("choice 2")
			self.rebuild_display()
		else:
			self.display_selection_error(player_selection)



	def display_selection_error(self, player_selection):
		if player_selection.isdigit():
			print("\n{} is an invalid option, please try again".format(player_selection))
			self.rebuild_display()
		else:
			print("\n{} is not a number. Please select a number from the options above.".format(player_selection))
			self.rebuild_display()



	#after every action, create new screen	
	def rebuild_display (self):
		text_width = 80

		#wipe screen
		os.system('clear')
		#title
		print("\t╔╦╗┬ ┬┌─┐  ╔═╗┬ ┬┌─┐  ╔═╗┌─┐  ╔╦╗┬ ┬┌─┐┌┬┐┬ ┬")
		print("\t ║ ├─┤├┤   ║╣ └┬┘├┤   ║ ║├┤    ║ ├─┤│ │ │ ├─┤")
		print("\t ╩ ┴ ┴└─┘  ╚═╝ ┴ └─┘  ╚═╝└     ╩ ┴ ┴└─┘ ┴ ┴ ┴")
		print("\n")

		#if player doesn't exist, opening scene / load game option	
		if Player.player["name"] == "":
			print(textwrap.fill(self.DESCRIPTIONS["start1"], text_width))
			print("\n")
			print(textwrap.fill(self.DESCRIPTIONS["start2"], text_width))
			print("\n")

			self.menu_options_no_player()


		print("\n")
