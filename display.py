import os
import textwrap
from player import Player


class Display(object):
	
	def __init__(self):
		pass

	def menu_options (self):
		print ("1. save game")
		print ("2. load game")	

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
			print(textwrap.fill("Obsessed with the occult, a rumor has reached you that the fabled Eye Of Thoth can be found in the dilapidated mansion of arcane explorer Archibald Hammer.", text_width))
			print("\n")
			print(textwrap.fill("Ignoring the fact that Archibald hasn't been seen in 20 years and his mansion is supposedly 'haunted', you decide to pay Archie a little visit..."))



		print("\n")
