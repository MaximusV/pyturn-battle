from GameInterface import *

class GamePresentation:

    """
     Defines interface for presenting the game to the user

    :author: James Heslin (PROGRAM_IX)
    """

    """ ATTRIBUTES

     The instance of GameInterface to delegate to

    game_interface  (private)

    """


    def display(self, message):
        """
         Sends a message to the interface to be displayed

        @param string message : The message string to pass to the interface to be displayed
        @return  :
        @author
        """
        pass

    def get_choice(self, options):
        """
         Send a list of options to the game interface to display them to the user. The
         interface gets the user choice and this method returns it

        @param string options : List of options to pass to the interface to be presented to the user
        @return int :
        @author
        """
        pass



