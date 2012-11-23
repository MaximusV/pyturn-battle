from codes.observer.IObserver import IObserver

class DBManager (IObserver):

    """
     Manages the saved state (in database or otherwise) of the game

    :author: James Heslin
    """

    def update(self, sub):
        """
         Called by the IObserver's notify() method

        @param ISubject sub : Subject to check
        @return  :
        @author
        """
        pass



