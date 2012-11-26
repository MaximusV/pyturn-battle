from State import State
from BattleEngine import BattleEngine
from ElectionEngine import ElectionEngine
from DBManager import DBManager


class GameState (State):

    """
     State representing the 'play'-specific processes

    :author: James Heslin
    """

    """ ATTRIBUTES

     Instance of BattleEngine specific to this GameState

    engine  (private)

     The data manager for this game state
     

    db_manager  (private)

    """
    
    def __init__(self):
        self.engine = self.create_engine()
        self.db_manager = DBManager()

    def get_options(self):
        """
         Return the names of the currently available actions as a list of strings

        @return list : List of possible actions, first element is a flag 
        @author
        """
        return self.engine.get_options()

    def get_state_desc(self):
        """
         Returns a description of the current game state

        @return string :
        @author
        """
        return self.engine.get_desc()

    def create_engine(self):
        """
         Interface for the creation of new BattleEngine instances

        @return BattleEngine : A subclass of BattleEngine for this GameState
        @author
        """
        return ElectionEngine()

    def process_input(self, curr_action):
        """
         Performs the current action and returns the result

        @param int curr_action : An integer representing the current action
        @return string : 
        @author
        """
        return self.engine.perform_action(curr_action)

    def end_turn(self):
        """
         Finish the current turn.
        @author
        """
        return self.engine.end_turn()


