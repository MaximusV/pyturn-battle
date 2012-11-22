from Party import *
from Character import *

class PoliticalParty (Party):

    """
     A Party of politicians

    :version:
    :author:
    """

    def create_character(self, attributes_dict):
        """
         Factory Method to create a new Character

        @param dict attributes_dict : Dictionary holding all the attributes of the new Character
        @return  :
        @author
        """
        pass

    def add_member(self, politician):
        """
         Add a politician to the PoliticalParty

        @param Character politician : The Character to add to the PoliticalParty
        @return  :
        @author
        """
        pass

    def remove_member(self, id):
        """
         Remove a member from the PoliticalParty

        @param int id : Integer representing the Character to remove
        @return  :
        @author
        """
        pass

    def get_active_member(self):
        """
         Get the active member of the PoliticalParty

        @return Character :
        @author
        """
        pass

    def get_member(self, id):
        """
         Return a Character with the ID specified

        @param int id : Integer representing the Character
        @return Character :
        @author
        """
        pass



