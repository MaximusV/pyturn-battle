from codes.observer import ISubject
import Character

class Party (ISubject, ISubject):

    """
     Stores a list of members and manages member creation and retrieval

    :author: Max Vizard
    """

    """ ATTRIBUTES

     List of members

    members_list  (protected)

     The currently active member

    active_member  (protected)

    """

    def create_character(self, attributes_dict):
        """
         Factory method to create Character instances

        @param dict attributes_dict : Dict of attributes for the new Character
        @return Character :
        @author
        """
        pass

    def add_member(self, character):
        """
         Add a Character to the list of members

        @param Character character : Character instance to add to the member list
        @return  :
        @author
        """
        pass

    def remove_member(self, id):
        """
         Remove a Character from the member list

        @param int id : ID of member to remove
        @return  :
        @author
        """
        pass

    def get_active_member(self):
        """
         Get the active member of this Party

        @return Character :
        @author
        """
        pass

    def get_member(self, id):
        """
         Get the Character instance that has the given ID if it is a member of this Party

        @param int id : The ID of the Character to get
        @return Character :
        @author
        """
        pass


