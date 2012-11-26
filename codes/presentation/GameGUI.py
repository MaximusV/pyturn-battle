from GameInterface import GameInterface
import easygui as eg

class GameGUI (GameInterface):

    """
     Graphical interface to game

    :author: James Heslin
    """

    def display(self, message):
        """
         Prints the message to the command line

        @param string message : Message to be displayed
        @return  :
        @author
        """
        for i in message:
            eg.msgbox(i, "Message")

    def get_choice(self, options):
        """
         Lists the options in the CLI and returns  the user input

        @param string options : List of options to present to the user
        @return int :
        @author
        """
        return options.index(eg.choicebox("Select an action", "Choice", 
                                          options))


