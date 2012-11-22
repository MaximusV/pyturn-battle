from ISubject import *
from Action import *
from IObserver import *
from Party import *

class GameplayVariables (ISubject):

    """
     Holds all the Party instances in the current game, and various gameplay
     constants

    :version:
    :author:
    """

    """ ATTRIBUTES

     Dict of all possible Actions

    actions_dict  (private)

     List of Party instances in the current game

    parties  (private)

     Integer representing the currently active Party

    active_party  (private)

     List of IObserver instances to notify when something changes

    observers  (private)

    """

    def attach(self, ob):
        """
         Add an IObserver to the observer list

        @param IObserver ob : IObserver to add to the observer list
        @return  :
        @author
        """
        pass

    def detach(self, ob):
        """
         Remove an IObserver from the observer list

        @param IObserver ob : IObserver to remove from the observer list
        @return  :
        @author
        """
        pass

    def notify(self):
        """
         Call update() on all observers

        @return  :
        @author
        """
        pass



