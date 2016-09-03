import os
import sys
import random
import textwrap
from player import Player
from room import Room


class Display(object):

	MENU_NO_PLAYER = (
		"N = New Character",
		"V = Load Game",
		"X = Quit",
	)

	MENU = (
		"C = Save Game",
		"V = Load Game",
		"X = Quit",
	)
	
	DESCRIPTIONS = {
		"error1" : "'{}' is an invalid option, please try again.",
		"start1" : "Obsessed with the occult, a rumor has reached you that the fabled Eye Of Thoth can be found in the dilapidated mansion of arcane explorer Archibald Hammer.",
		"start2" : "Ignoring the fact that Archibald hasn't been seen in 20 years and his mansion is supposedly 'haunted', you decide to pay Archie a little visit...",
		"atrium1" : "Lightning flashes as you kick in the front door. Clicking on your flashlight, you step across the threshold.",
		"atrium2" : "Playing your flashlight around the room you see an enormous chandelier glittering above a plush floor rug. In the dimness, it is hard to tell if the rugstain is wine or blood.",
		"atrium3" : "Straight ahead is a {}. Behind you is the is {}. To the right appears to be a {}. To the left an enormous {}.",
	}


	def __init__(self):

		self.player = Player(self)
		self.room = Room(self)
		self.text_width = 80
		self.player_selection = ""
		self.location = "start"
		self.error = False
		self.error_type = ""
		self.is_alive = True

	#overall game keeps running	
	def alive (self):
		return self.is_alive	


	def description(self):
		#player doesn't exist (dead or new game)	
		if self.location == "start":
			print("\t" + textwrap.fill(self.DESCRIPTIONS["start1"], self.text_width))
			print("\n")
			print("\t" + textwrap.fill(self.DESCRIPTIONS["start2"], self.text_width))
		
		elif self.location =="atrium":
			self.room.room_north = "closed door"
			self.room.room_south = "exit"
			self.room.room_east = random.choice(self.room.ROOM)
			self.room.room_west = random.choice(self.room.ROOM)
			print("\t" + textwrap.fill(self.DESCRIPTIONS["atrium1"], self.text_width))	
			print("\n")
			print("\t" + textwrap.fill(self.DESCRIPTIONS["atrium2"], self.text_width))	
			print("\n")
			print("\t" + textwrap.fill(self.DESCRIPTIONS["atrium3"], self.text_width)
				.format(self.room.room_north, self.room.room_south, self.room.room_east, self.room.room_west))	


	#action to take when player_selection made		
	def menu_input_handler(self):
		#options if you are in the atrium		
		if self.location == "atrium":
			#open the door
			if self.player_selection == "w":
				pass
			#turn and flee the house
			elif self.player_selection == "s":
				pass
			#room on right
			elif self.player_selection == "d":
				pass
			#room on left
			elif self.player_selection == "a":
				pass
			else: 
				pass
		if self.location == "create_player":
			self.player.player_reset(self.player_selection)
			self.location = "atrium"

		#create new player		
		elif self.player_selection == "n":
			self.location="create_player"
			
		#save game
		elif self.player_selection == "c":
			pass
		
		#load game	
		elif self.player_selection == "v":
			pass

		#quit
		elif self.player_selection == "x":
			self.is_alive = False
	
		#invalid input	
		else:
			self.display_selection_error("error1")	


	def display_selection_error(self, error_type):
		self.error = True
		self.error_type = "error1"


	#get player input and send it to the action function
	def player_input(self):
		if self.location == "create_player":
			self.player_selection = input("\t> ")
		else:	
			self.player_selection = input("\t> ").lower()
			

	def HUD (self):		
		print("\tSANITY: {}\t\t{}\t\tHEALTH: {}"
			.format(self.player.get_sanity(), self.player.name, self.player.get_health() ))


	def title (self):
		print("\t╔╦╗┬ ┬┌─┐  ╔═╗┬ ┬┌─┐  ╔═╗┌─┐  ╔╦╗┬ ┬┌─┐┌┬┐┬ ┬")
		print("\t ║ ├─┤├┤   ║╣ └┬┘├┤   ║ ║├┤    ║ ├─┤│ │ │ ├─┤")
		print("\t ╩ ┴ ┴└─┘  ╚═╝ ┴ └─┘  ╚═╝└     ╩ ┴ ┴└─┘ ┴ ┴ ┴")
	

	def error_message (self):
		if self.error: 
			print("\t*" * 5)
			print("\t" + textwrap.fill(self.DESCRIPTIONS["error1"], self.text_width)
				.format(self.player_selection))
			print("\t*" * 5 + "\n")

			self.error = False


	def print_standard_menu(self):
		#if player name exists 
		if self.player.name:		
			for option in self.MENU:
				print("\t" + option)
		#no player exists	
		else: 	
			for option in self.MENU_NO_PLAYER:
				print("\t" + option)

		#player input	
		print("\n\tWhat would you like to do?")


	#after every action, create new screen	
	def rebuild_display (self):

		#wipe screen
		os.system('clear')

		#title
		self.title()

		#HUD
		self.HUD()
		print("\n")

		#description
		self.description()
		print("\n")

		#error messages
		self.error_message()

		#create a player - otherwise print menus
		if self.location == "create_player":
			print ("\tWhat is your name?")
		else:		
			#room specific menu options
			self.room.movement_options()

			#standard menu options
			self.print_standard_menu()

		print("\n")





