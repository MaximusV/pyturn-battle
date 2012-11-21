from Character import *
from I_observer import *

class Party(object):

    """
     Stores a list of members and manages member creation and retrieval

    :version:
    :author:
    """

    """ ATTRIBUTES

     

    members_list  (protected)

     

    active_member  (protected)

     

    observer_list  (private)

    """

    def create_character(self, attributes_dict):
        """
         

        @param dict attributes_dict : 
        @return Character :
        @author
        """
        pass

    def add_member(self, character):
        """
         

        @param Character character : 
        @return  :
        @author
        """
        pass

    def remove_member(self, id):
        """
         

        @param int id : 
        @return  :
        @author
        """
        pass

    def get_active_member(self, id):
        """
         

        @param int id : 
        @return Character :
        @author
        """
        pass

    def get_member(self, id):
        """
         

        @param int id : 
        @return Character :
        @author
        """
        pass

    def attach(self, ob):
        """
         

        @param i_observer ob : 
        @return  :
        @author
        """
        pass

    def detach(self, ob):
        """
         

        @param i_observer ob : 
        @return  :
        @author
        """
        pass



