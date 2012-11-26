from GamePresentation import *
from GUInterface import GUInterface

class GUIPresentation (GamePresentation):

    """
     Implementation of GamePresentation that has GUInterface as its interface

    :version:
    :author: James Heslin (PROGRAM_IX)
    """
    
    def __init__(self):
        self.game_interface = GUInterface()

    def display(self, message):
        """
         Implementation of display that delegates to its GUInterface instance

        @param string message : Message to be passed to GUInterface
        @return  :
        @author
        """
        self.game_interface.display(message)

    def get_choice(self, options):
        """
         Implementaion of get_choice that delegates to its GUInterface instance

        @param string options : List of options to pass to the GUInterface 
        @return int :
        @author
        """
        return self.game_interface.get_choice(options)



