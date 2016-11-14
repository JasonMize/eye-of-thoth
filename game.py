from game_state import GameState
from player_input import PlayerInput
from display import Display 

class Game (object):

    def __init__ (self):
        self.game_state = GameState()
        self.display = Display()
        self.player_input = PlayerInput()

    #game loop  
    def run (self): 
        while self.game_state.get_state() is not "quit":
            self.draw_screen()
            self.get_input ()



    def draw_screen(self):
        self.title()
        self.game_state.draw (self.display)

    def title (self):
        self.display.draw_text("\t╔╦╗┬ ┬┌─┐  ╔═╗┬ ┬┌─┐  ╔═╗┌─┐  ╔╦╗┬ ┬┌─┐┌┬┐┬ ┬")
        self.display.draw_text("\t ║ ├─┤├┤   ║╣ └┬┘├┤   ║ ║├┤    ║ ├─┤│ │ │ ├─┤")
        self.display.draw_text("\t ╩ ┴ ┴└─┘  ╚═╝ ┴ └─┘  ╚═╝└     ╩ ┴ ┴└─┘ ┴ ┴ ┴")
        
    def get_input (self):
        self.game_state.get_input(self.player_input)

