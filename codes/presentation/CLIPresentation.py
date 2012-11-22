from GamePresentation import *

class CLIPresentation (GamePresentation):

    """
     Implementation of GamePresentation that has GameCLI as its interface

    :author: James Heslin (PROGRAM_IX)
    """
    
    def __init__(self, game_interface):
        self.game_interface = game_interface

    def display(self, message):
        """
         Implementation of display that delegates to its GameCLI instance

        @param string message : Message to be passed to GameCLI
        @return  :
        @author
        """
        self.game_interface.display(message)

    def get_choice(self, options):
        """
         Implementaion of get_choice that delegates to its GameCLI instance

        @param string options : List of options to pass to the GameCLI 
        @return int :
        @author
        """
        return self.game_interface.get_choice(options)



