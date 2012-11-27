from pyturn.observer.IObserver import IObserver

class DBManager (IObserver):

    """
     Manages the saved state (in database or otherwise) of the game

    :author: James Heslin
    """

    def __init__(self, init_sub):
        self.last_sub = init_sub

    def update(self, sub):
        """
         Called by the IObserver's notify() method

        @param ISubject sub : Subject to check
        @return  :
        @author
        """
        self.last_sub = sub
        
        # print 'Update called on DB_Manager'



