from GamePresentation import *

class CLIPresentation (GamePresentation):

    """
     Implementation of GamePresentation that has GameCLI as its interface

    :version:
    :author:
    """

    def display(self, message):
        """
         Implementation of display that delegates to its GameCLI instance

        @param string message : Message to be passed to GameCLI
        @return  :
        @author
        """
        pass

    def get_choice(self, options):
        """
         Implementaion of get_choice that delegates to its GameCLI instance

        @param string options : List of options to pass to the GameCLI 
        @return int :
        @author
        """
        pass



