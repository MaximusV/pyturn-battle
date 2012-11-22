from GamePresentation import *

class GameInterface(object):

    """
     Specifies the interface for user interaction with the game

    :author: James Heslin (PROGRAM_IX)
    """

    def display(self, message):
        """
         Displays the message to the user

        @param string message : Message to display
        @return  :
        @author
        """
        pass

    def get_choice(self, options):
        """
         Presents a list of choices to the user and returns their choice

        @param string options : List of options to present to the user
        @return int :
        @author
        """
        pass



