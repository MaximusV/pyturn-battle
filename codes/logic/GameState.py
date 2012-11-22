from State import *
from BattleEngine import *
from DBManager import *

class GameState (State):

    """
     State representing the 'play'-specific processes

    :version:
    :author:
    """

    """ ATTRIBUTES

     Instance of BattleEngine specific to this GameState

    engine  (private)

     The data manager for this game state
     

    db_manager  (private)

    """

    def get_options(self):
        """
         Return the names of the currently available actions as a list of strings

        @return string :
        @author
        """
        pass

    def get_state_desc(self):
        """
         Returns a description of the current game state

        @return string :
        @author
        """
        pass

    def create_engine(self):
        """
         Interface for the creation of new BattleEngine instances

        @return BattleEngine :
        @author
        """
        pass

    def _process_input(self, curr_action):
        """
         Performs the current action and returns the result

        @param int curr_action : An integer representing the current actionp
        @return string :
        @author
        """
        pass



