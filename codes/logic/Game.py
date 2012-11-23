from State import *
from GameState import *
from GamePresentation import *

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



