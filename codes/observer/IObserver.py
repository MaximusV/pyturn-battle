from ISubject import *

class IObserver(object):

    """
     Defines observer interface

    :version:
    :author:
    """

    def update(self, sub):
        """
         Action taken when a subject notifies observer of change

        @param ISubject sub : Instance of the subject that changed
        @return  :
        @author
        """
        pass



