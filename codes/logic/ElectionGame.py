from Game import Game
from GameState import GameState
from MenuState import MenuState
from codes.presentation.CLIPresentation import CLIPresentation
from codes.presentation.GUIPresentation import GUIPresentation
from sys import exit

class ElectionGame (Game):

    """
     Main Class for the Election game

    :author: James Heslin
    """

    """ ATTRIBUTES

     Holds the current state of the application

    states  (private)

     Holds a reference to the current GamePresentation instance

    presentation  (private)

    """

    def __init__(self):
        self.states = [self.create_state('game'), self.create_state('menu')]
        self.presentation = CLIPresentation()

    def turn(self):
        """
         Method to call each turn in the Election game

        @return int: flag to tell the run method what to do next
        @author
        """
        opt = self.states[0].get_options()
        inp = self.presentation.get_choice(opt)
        result = self.states[0].process_input(inp)
        while (result[0] == "choice"):
            inp = self.presentation.get_choice(result[1:])
            result = self.states[0].process_input(inp)
        if(result[0] == "quit"):
            self.presentation.display(result[1:])
            return -1
        elif(result[0] == "switch"):
            self.presentation.display(result[1:])
            return 1
        elif(result[0] == "display"):
            self.presentation.display(result[1:])
            return 0
        

    def run(self):
        """
         Main loop for the Election game

        @author
        """
        turn_flag = 0
        while not(turn_flag == -1):
            turn_flag = self.turn()
            if turn_flag == 1:
                # Switch state
                tmp = self.states[0]
                self.states[0] = self.states[1]
                self.states[1] = tmp
            elif turn_flag == -1:
                # Quit
                exit(0)                
            

    def create_state(self, s_type):
        """
         Create a state

        @return State : an instance of a subclass of State
        @author
        """
        
        if s_type == 'game':
            return GameState()
        elif s_type == 'menu':
            return MenuState()
        



