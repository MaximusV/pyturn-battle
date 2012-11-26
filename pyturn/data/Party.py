from codes.observer.ISubject import ISubject
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

    def create_character(self, name, attributes_dict):
        """
         Factory method to create Character instances
         
        @param string name : String representing the name of the Character to be created
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

    def remove_member(self, id_num):
        """
         Remove a Character from the member list

        @param int id_num : ID of member to remove
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

    def get_member(self, id_num):
        """
         Get the Character instance that has the given ID if it is a member of this Party

        @param int id : The ID of the Character to get
        @return Character :
        @author
        """
        pass
    
    def get_state(self):
        """
         Get information about the state of this Party
         
         @return list : A list of strings representing the state of the Party
         @author
        """
        pass 

