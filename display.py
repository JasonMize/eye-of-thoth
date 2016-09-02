import os
import sys
import textwrap
from player import Player

class Display(object):

	MENU_NO_PLAYER = (
		"N = New Character",
		"L = Load Game",
		"Q = Quit",
	)

	MENU = (
		"S = Save Game",
		"L = Load Game",
		"Q = Quit",
	)
	
	DESCRIPTIONS = {
		"error1" : "'{}' is an invalid option, please try again.",
		"start1" : "Obsessed with the occult, a rumor has reached you that the fabled Eye Of Thoth can be found in the dilapidated mansion of arcane explorer Archibald Hammer.",
		"start2" : "Ignoring the fact that Archibald hasn't been seen in 20 years and his mansion is supposedly 'haunted', you decide to pay Archie a little visit...",
		"atrium1" : "Lightning flashes as you kick in the front door. Clicking on your flashlight, you step across the threshold.",
		"atrium2" : "Playing your flashlight around the room you see...TODO",
	}


	def __init__(self):
		self.player = Player(self)
		self.text_width = 80
		self.player_selection = ""


	def description(self, location):
		#player doesn't exist (dead or new game)	
		if location == "start":
			print("\t" + textwrap.fill(self.DESCRIPTIONS["start1"], self.text_width))
			print("\n")
			print("\t" + textwrap.fill(self.DESCRIPTIONS["start2"], self.text_width))

		elif location == "error1":
			print("\n" + textwrap.fill(self.DESCRIPTIONS["error1"], self.text_width)
				.format(self.player_selection))
		
		elif location =="create_player":
			self.player.player_creation()

		elif location =="atrium":
			print("\t" + textwrap.fill(self.DESCRIPTIONS["atrium1"], self.text_width))	
			print("\n")
			print("\t" + textwrap.fill(self.DESCRIPTIONS["atrium2"], self.text_width))	


	def menu (self):
		pass

	def menu_options_no_player(self):
		#new character
		if self.player_selection == "n" or self.player_selection == "N":
			self.rebuild_display(location="create_player")
		#load game	
		elif self.player_selection == "l" or self.player_selection == "L":
			pass
		#quit
		elif self.player_selection == "q" or self.player_selection == "Q":
			sys.exit
		#invalid input	
		else:
			self.display_selection_error()


	def display_selection_error(self):
		self.rebuild_display(location="error1")
		

	#get player input
	def player_input(self):
		print("\n\tWhat would you like to do?")
		self.player_selection = input("\t> ")		
		return self.player_selection


	def HUD (self):		
		print("\tSANITY: {}\t\t{}\t\tHEALTH: {}"
			.format(self.player.sanity, self.player.name, self.player.health ))


	#after every action, create new screen	
	def rebuild_display (self, location="start"):

		#wipe screen
		os.system('clear')
	
		#title
		print("\t╔╦╗┬ ┬┌─┐  ╔═╗┬ ┬┌─┐  ╔═╗┌─┐  ╔╦╗┬ ┬┌─┐┌┬┐┬ ┬")
		print("\t ║ ├─┤├┤   ║╣ └┬┘├┤   ║ ║├┤    ║ ├─┤│ │ │ ├─┤")
		print("\t ╩ ┴ ┴└─┘  ╚═╝ ┴ └─┘  ╚═╝└     ╩ ┴ ┴└─┘ ┴ ┴ ┴")

		#HUD
		self.HUD()
		print("\n")

		#description
		self.description(location)
		print("\n")

		#print menu options
		#if player name exists 
		if self.player.name:
			for option in self.MENU:
				print("\t" + option)
		#no player created	
		else: 	
			for option in self.MENU_NO_PLAYER:
				print("\t" + option)

		#player input	
		self.player_selection = self.player_input()	

		#action to take
		self.menu_options_no_player()

		print("\n")





