from IObserver import *
from ISubject import *

class DBManager (IObserver):

    """
     Manages the saved state (in database or otherwise) of the game

    :version:
    :author:
    """

    def update(self, sub):
        """
         Called by the IObserver's notify() method

        @param ISubject sub : Subject to check
        @return  :
        @author
        """
        pass



