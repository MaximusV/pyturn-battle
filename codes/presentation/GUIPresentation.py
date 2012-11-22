from GamePresentation import *

class GUIPresentation (GamePresentation):

    """
     Implementation of GamePresentation that has GameGUI as its interface

    :version:
    :author: James Heslin (PROGRAM_IX)
    """
    
    def __init__(self, game_interface):
        self.game_interface = game_interface

    def display(self, message):
        """
         Implementation of display that delegates to its GameGUI instance

        @param string message : Message to be passed to GameGUI
        @return  :
        @author
        """
        self.game_interface.display(message)

    def get_choice(self, options):
        """
         Implementaion of get_choice that delegates to its GameGUI instance

        @param string options : List of options to pass to the GameGUI 
        @return int :
        @author
        """
        return self.game_interface.get_choice(options)



