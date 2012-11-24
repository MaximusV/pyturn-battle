from State import *
from codes.logic.Game import SWITCH_FLAG, CHOOSE_FLAG, DISPLAY_FLAG, QUIT_FLAG

class MenuState (State):

    """
     Menu-specific behaviour
    
    :author: James Heslin
    """

    def get_options(self):
        """
         Get the currently available menu options

        @return string :
        @author
        """
        return [CHOOSE_FLAG, "Start game", "Quit"]

    def get_state_desc(self):
        """
         Returns a string describing the current state of the menu

        @return string :
        @author
        """
        return [DISPLAY_FLAG, "Menu"]

    def process_input(self, curr_action):
        """
         Process the input to the menu

        @param int curr_action : 
        @return string :
        @author
        """
        if curr_action == 0:
            return [SWITCH_FLAG, "Starting game..."]
        elif curr_action == 1:
            return [QUIT_FLAG, "Quitting..."]



