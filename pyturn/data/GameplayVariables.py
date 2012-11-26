from pyturn.observer.ISubject import ISubject


class GameplayVariables (ISubject):

    """
     Holds all the Party instances in the current game, and various gameplay
     constants

    :author: Max Vizard
    """

    """ ATTRIBUTES

     Dict of all possible Actions

    actions_dict  (public)

     List of Party instances in the current game

    parties  (public)

     Integer representing the currently active Party

    active_party  (public)

     List of IObserver instances to notify when something changes

    observers  (public)

    """
    
    def __init__(self):
        self.actions_dict = {}
        self.parties = []
        self.active_party = -1
        self.observers = []
        
    def get_action(self, a_int):
        party = self.parties[self.active_party]
        char = party.get_active_member()
        a_string = char.get_action(a_int)
        #print a_string
        return self.actions_dict.get(a_string)

    def attach(self, ob):
        """
         Add an IObserver to the observer list

        @param IObserver ob : IObserver to add to the observer list
        @return void :
        @author
        """
        self.observers.append(ob)

    def detach(self, ob):
        """
         Remove an IObserver from the observer list

        @param IObserver ob : IObserver to remove from the observer list
        @return void :
        @author
        """
        self.observers.remove(ob)

    def notify(self):
        """
         Call update() on all observers

        @return void :
        @author
        """
        for observer in self.observers:
            observer.update(self)




