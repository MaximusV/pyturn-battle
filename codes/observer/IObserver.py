from codes.observer import ISubject

class IObserver(object):

    """
     Defines Observer interface

    :author: Max Vizard
    """

    def update(self, sub):
        """
         Action taken when a subject notifies observer of change

        @param ISubject sub : Instance of the subject that changed
        @return void :
        @author
        """
        pass



