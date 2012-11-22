from State import *

class MenuState (State):

    """
     Menu-specific behaviour

    :version:
    :author:
    """

    def get_options(self):
        """
         Get the currently available menu options

        @return string :
        @author
        """
        pass

    def get_state_desc(self):
        """
         Returns a string describing the current state of the menu

        @return string :
        @author
        """
        pass

    def process_input(self, curr_action):
        """
         Process the input to the menu

        @param int curr_action : 
        @return string :
        @author
        """
        pass



