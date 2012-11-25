from GameInterface import GameInterface

class GameCLI (GameInterface):

    """
     Command Line Interface to game

    :author: James Heslin (PROGRAM_IX)
    """

    def display(self, message):
        """
         Prints the message to the command line

        @param string message : Message to be displayed
        @return  :
        @author
        """
        for i in message:
            print i

    def get_choice(self, options):
        """
         Lists the options in the CLI and returns  the user input

        @param string options : List of options to present to the user
        @return int :
        @author
        """
        n = 1
        for o in options:
            print n, "-", o
            n = n+1
        res = int(raw_input("Select an option: "))-1
        #print "Selected", res
        return res



