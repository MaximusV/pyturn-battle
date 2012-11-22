from IObserver import *

class ISubject(object):

    """
     Defines Subject interface

    :version:
    :author:
    """

    def notify(self):
        """
         Calls update() on all the observers.

        @return  :
        @author
        """
        pass

    def attach(self, ob):
        """
         Add an observer to the list

        @param IObserver ob : 
        @return  :
        @author
        """
        pass

    def detach(self, ob):
        """
         Remove an observer from the list

        @param IObserver ob : 
        @return  :
        @author
        """
        pass



