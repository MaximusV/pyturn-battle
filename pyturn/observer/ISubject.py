class ISubject:

    """
     Defines Subject interface

    :author: Max Vizard
    """

    def notify(self):
        """
         Calls update() on all the observers.

        @return void :
        @author
        """
        pass

    def attach(self, ob):
        """
         Add an observer to the list

        @param IObserver ob : The IObserver instance to add to the list
        @return void :
        @author
        """
        pass

    def detach(self, ob):
        """
         Remove an observer from the list

        @param IObserver ob : The IObserver instance to remove from the list
        @return void :
        @author
        """
        pass



