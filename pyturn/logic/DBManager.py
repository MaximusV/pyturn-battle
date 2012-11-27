from pyturn.observer.IObserver import IObserver
import copy

class DBManager (IObserver):

    """
     Manages the saved state (in database or otherwise) of the game

    :author: James Heslin
    """

    def __init__(self, init_sub):
        self.last_sub = copy.deepcopy(init_sub)

    def update(self, sub):
        """
         Called by the IObserver's notify() method

        @param ISubject sub : Subject to check
        @return  :
        @author
        """
        self.last_sub = copy.deepcopy(sub)
        
        # print 'Update called on DB_Manager'
    
    def __str__(self):
        return str(self.__dict__)

    def __cmp__(self, other): 
        return self.__dict__ == other.__dict__


