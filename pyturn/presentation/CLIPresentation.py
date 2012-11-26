from GamePresentation import GamePresentation
from CLInterface import CLInterface

class CLIPresentation (GamePresentation):

    """
     Implementation of GamePresentation that has CLInterface as its interface

    :author: James Heslin (PROGRAM_IX)
    """
    
    def __init__(self):
        self.game_interface = CLInterface()

    def display(self, message):
        """
         Implementation of display that delegates to its CLInterface instance

        @param string message : Message to be passed to CLInterface
        @return  :
        @author
        """
        self.game_interface.display(message)

    def get_choice(self, options):
        """
         Implementaion of get_choice that delegates to its CLInterface instance

        @param string options : List of options to pass to the CLInterface 
        @return int :
        @author
        """
        return self.game_interface.get_choice(options)



