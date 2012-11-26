from State import State
from GameState import *
from pyturn.presentation.GamePresentation import GamePresentation

SWITCH_FLAG = "switch"
QUIT_FLAG = "quit"
CHOOSE_FLAG = "choose"
DISPLAY_FLAG = "display"

class Game:

    """
     Main class for the application

    :author: James Heslin
    """

    """ ATTRIBUTES

     Holds the current state of the application

    state  (private)

     Holds a reference to the current GamePresentation instance

    presentation  (private)

    """

    def turn(self):
        """
         Method that is called every iteration of the run loop, returns 0 to change
         state, -1 to quit

        @return int :
        @author
        """
        pass

    def run(self):
        """
         Main game loop, calls turn until turn returns quit value

        @return  :
        @author
        """
        pass

    def create_state(self):
        """
         Factory method providing an interface for creating State instances

        @return GameState :
        @author
        """
        pass



