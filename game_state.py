
from player import Player
from display import Display


class GameState(object):

    DESCRIPTIONS = {
        "start" : ("Obsessed with the occult, a rumor has reached you that the fabled Eye Of Thoth can be found in the dilapidated mansion of arcane explorer Archibald Hammer.",
            "Ignoring the fact that Archibald hasn't been seen in 20 years and his mansion is supposedly 'haunted', you decide to pay Archie a little visit...",
        ),
        "create_player" : ("What is your name?",),
    }

    def __init__ (self):
       self.state = "start"
       self.player = Player()
       self.display = Display()


    def get_state(self):
        return self.state

    def get_menu_options(self):
        return []

   #starting state - welcome screen

   #create character
    def create_character(self):
        self.state = "create"

   #exploring rooms - fights, etc. 
    def exploring (self):
        pass

    def draw (self, display):
        self.player.draw(display)
        if self.state == "start":
            self.draw_start(display)
        elif self.state == "create":
            self.draw_create(display)
        elif self.state == "explore":
            pass
        elif self.state == "save":
            pass
        elif self.state == "load":
            pass
        elif self.state == "quit":
            pass
        else:
            self.state = "start"

        self.draw_menu(display)


    def draw_menu (self, display):
        if self.state == "start":
            #N for create player
            pass
        elif self.state == "create":
            #always pass
            return
        elif self.state == "explore":
            #room menu + action menu 
            pass
        elif self.state == "save":
            return
        elif self.state == "load":
            return
        elif self.state == "quit":
            return
        else:
            pass
        # for line in self.MENU["standard"]:
        #      self.display.draw_text ()
        #      #TODO: display standard menu choices

        # 3 types of menu: 

        #     actions: (numbers)
        #         1 = Fight
        #         2 = Exorcism

        #     movements: (wasd)
        #         W = North
        #         A = West
        #         S = South
        #         D = East

        #     standard:
        #         C = Save
        #         V = Load
        #         X = Exit



    def draw_start (self, display):       
        for line in self.DESCRIPTIONS["start"]:
            self.display.draw_text (line)


    def draw_create(self, display):
        pass



    def get_input(self, player_input):
        if self.state == "create":
            abc = player_input.get_text_input()
        else:
            abc = player_input.get_menu_input()
        self.process_input(abc)




   #saving game

   #loading game


   #terminal state
    def quit (self):
        self.state = "quit"


    def process_input(self, abc):  
        if self.state == "start":
            self.process_input_start(abc)
        elif self.state == "create":
            self.process_input_create(abc)
        elif self.state == "explore":
            pass
        elif self.state == "save":
            pass
        elif self.state == "load":
            pass
        elif self.state == "quit":
            pass
        else:
            self.state = "start"


    def process_input_start(self, abc):
        if abc == "n":
            self.state = "create"
        elif abc == "l":
            self.state = "load"
        elif abc == "q":
            self.state = "quit"


    def process_input_create(self, abc):
        self.player.player_reset(abc)
        self.state = "explore"





