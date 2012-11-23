from Party import *
from GameplayVariables import *

class BattleEngine(object):

    """
     Class that stores and manages interactions between parties, characters and
     actions. Bridges Data and Logic layers.

    :author: James Heslin
    """

    """ ATTRIBUTES

     Holds all gameplay data

    vars  (private)

    """

    def setup_data(self):
        """
         Initialises all the Party, Character and Action instances

        @return  :
        @author
        """
        pass

    def perform_action(self, action):
        """
         Performs the action specified by the input

        @param string action : The action to be performed
        @return string :
        @author
        """
        pass

    def create_party(self, name):
        """
         Interface for the creation of new Party instances

        @param string name : Name of the party
        @return Party :
        @author
        """
        pass

    def get_char_choice(self, curr_action):
        """
         Returns a list of all the characters the current action can be performed on.

        @param int curr_action : Integer representing the current action
        @return string :
        @author
        """
        pass



