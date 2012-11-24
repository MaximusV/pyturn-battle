from Party import Party
from Character import Character

class PoliticalParty (Party):

    """
     A Party of politicians

    :author: Max Vizard
    """
    """ ATTRIBUTES
    
     Name of the party
    name  (public)

     List of members

    members_list  (private)

     The currently active member

    active_member  (private)

    """
    
    def __init__(self, name):
        self.name = name
        self.members_list = []
        self.active_member = None
        
    def create_character(self, name, attributes_dict, actions_list):
        """
         Factory Method to create a new Character
        
        @param string name : String representing the name of the Character to be created
        @param dict attributes_dict : Dictionary holding all the attributes of the new Character
        @return Character :
        @author
        """
        return Character(name, attributes_dict, actions_list)

    def add_member(self, politician):
        """
         Add a politician to the PoliticalParty

        @param Character politician : The Character to add to the PoliticalParty
        @return void :
        @author
        """
        self.members_list.append(politician)

    def remove_member(self, id_num):
        """
         Remove a member from the PoliticalParty

        @param int id_num : Integer representing the Character to remove
        @return void :
        @author
        """
        member = self.get_member(id_num)
        if member:
            self.members_list.remove(member)
        else:
            print 'Member with ID: %i not in party %s' % (id, self.name)

    def get_active_member(self):
        """
         Get the active member of the PoliticalParty

        @return Character : The active member of the party to be returned
        @author
        """
        return self.active_member

    def set_active_member(self, active):
        """
         Set the active member of the PoliticalParty
         
        @param Character active : The Character to set as active
        @return void :
        @author: 
        """
        self.active_member = active

    def get_member(self, id_num):
        """
         Return a Character with the ID specified

        @param int id_num : Integer representing the Character
        @return Character : The Character with the ID value specified or None if not found
        @author
        """
        for mem in self.members_list:
            if mem.id == id_num:
                return mem
            
        print 'Member with ID: %i not found' % id_num
        return None
        



