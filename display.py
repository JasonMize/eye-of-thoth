import os
import sys
import random
import textwrap

from player import Player
from player_input import PlayerInput


class Display(object):

	MENU_CONSTANTS = (
		"X = Quit",
	)
	
	DESCRIPTIONS = {
		"error1" : ("That is an invalid option, please try again.",),
		"error2" : ("That name is too long. 10 characters or less, please.",),
		"error_insane" : ("Maybe a quiet cup of tea would help you regain a bit of sanity?",
			"GAME OVER",
			),
		"error_dead" : ("Being dead is the worst.", 
			"GAME OVER",
			),
		"monster_dead" : ("The monster is dead!",),
		"monster_insane" : ("You have banished the monster back to Neter-khertet!",
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
			"Straight ahead is a closed door. Behind you is the exit.",
			#" To the right appears to be a library. To the left an enormous dining hall.",
			),
		"atrium_closet" : ("Stepping forward across the winestained rug (blood?), you grasp the doorknob firmly and open the door.",
			"You are unsurprised to discover a closet full of moth eaten fur coats... and then movement pulls your eye to the shadowy floor.", 
			"The shadows are completely filled with the overlapping coils of the largest serpent you have ever seen."),
		"atrium_monster_flee" : ("You flinch from the undulating mound, slamming the door as you leap back.",
			"Before the door can latch, the serpent bursts forward!",
			"As the door smashes open the serpent rears upward and speaks...",
			"'Who dares disturb the rest of Apophis?! I shall sleep atop thy bones!'",
			),
		"atrium_monster_fight_win" : ("Your boot connects solidly with the serpents head.",
			"As you back up to administer another sample of your wrath, the serpent opens its mouth and begins to speak...",
			"'You dare to strike Apophis?! Prepare to die!'",
			),
		"atrium_monster_fight_lose" : ("The serpent dodges your kick and explodes out of the closet, knocking you flying.",
			"YOU TAKE DAMAGE!",
			"As you scramble to your feet, the serpent stares for a moment and then begins to speak...", 
			"'Foolish mortal. I am Apophis! Your body shall feed my young.'"),
		"atrium_fight_loop_physical_win" : ("You strike Apophis with your hands!",
			"That seems to have some effect so you do it some more.",
			),
		"atrium_fight_loop_physical_lose" : ("You attempt to strike Apophis but he strikes you first!",
			"YOU TAKE DAMAGE!",
			"Maybe if you'd taken Gym instead of Latin?",
			),
		"atrium_fight_loop_mystical_win" : ("Shouting a mystical phrase of banishment that your Professor of Egyptology taught you seems to have some effect.", 
			"The serpent is slightly transparent around the edges.", 
			"Keep it up!",
			),
		"atrium_fight_loop_mystical_lose" : ("Your attempt to banish Apophis to the astral plane gives you an unfortunate glimpse of the other side.",
			"YOU LOSE SANITY!",
			"I'm sure you'll feel better after a small lie down.",
			),
		"atrium_monster_dead" : ("You have killed Apophis! Well done, that.",
			),
		"atrium_monster_insane" : ("You have banished Apophis from the material plane! And Mother said you'd never amount to anything.",
			),
		
	}


	def __init__(self):
		self.player_input = PlayerInput(self)
		self.text_width = 80
		self.location = "start"
		self.player_hud = ""
		self.error = "no_error"


	def description(self):
		#description start
		for item in self.DESCRIPTIONS[self.location]:
			print("\t" + textwrap.fill(item, self.text_width))
			print("\n")
		

	#print HUD
	def hud (self):
		print(self.player_hud)


	#print title
	def title (self):
		print("\t╔╦╗┬ ┬┌─┐  ╔═╗┬ ┬┌─┐  ╔═╗┌─┐  ╔╦╗┬ ┬┌─┐┌┬┐┬ ┬")
		print("\t ║ ├─┤├┤   ║╣ └┬┘├┤   ║ ║├┤    ║ ├─┤│ │ │ ├─┤")
		print("\t ╩ ┴ ┴└─┘  ╚═╝ ┴ └─┘  ╚═╝└     ╩ ┴ ┴└─┘ ┴ ┴ ┴")
	

	def print_error_message(self):
		if self.error != "no_error": 
			print("\t*" * 5)

			for item in self.DESCRIPTIONS[self.error]:
				print("\t" + textwrap.fill(item, self.text_width))					

			print("\t*" * 5 + "\n")
			self.error = "no_error"


	def print_menu_constants(self):
		#player input
		if self.location != "create_player" and self.location != "exit": 
			if self.error != "error_insane" and self.error != "error_dead":	
				for item in self.MENU_CONSTANTS:
					print("\t" + item)

				print("\n\tWhat would you like to do?")


	#after every action, create new screen	
	def rebuild_display (self, display_room, player_input, player):

		#wipe screen
		os.system('clear')
		# print("*" * 10)
		# print("room = " + self.location)

		#title
		self.title()

		#HUD
		player.hud()
		print("\n")

		#description
		self.description()
		print("\n")

		#error messages
		self.print_error_message()

		if player.is_alive:
			#room specific menu actions
			display_room.print_action_options()

			#room specific menu movements
			display_room.print_movement_options()

			#standard menu options
			self.print_menu_constants()



