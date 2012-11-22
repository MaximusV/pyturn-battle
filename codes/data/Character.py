from ISubject import *

class Character (ISubject):

    """
     Stores and manages data relating to an individual character and their attributes

    :version:
    :author:
    """

    """ ATTRIBUTES

     A dict of all the character's attributes

    attributes_dict  (protected)

     Unique identifier of the character

    id  (protected)

     Static counter to keep track of how many characters have been created - used to
     assign IDs

    CHARACTER_COUNT  (private)

     The Character's name

    name  (private)

    """

    def remove_attr(self, name):
        """
         Remove an attribute from the character's dict

        @param string name : Name of attribute to remove
        @return  :
        @author
        """
        pass

    def incr_attr(self, name, value = 1):
        """
         Increase value of an attribute in the character's dict

        @param string name : Name of attribute
        @param int value : Value to increase the attribute by
        @return  :
        @author
        """
        pass

    def decr_attr(self, name, value = 1):
        """
         Decrease value of an attribute in the character's dict

        @param string name : Name of attribute to decrease
        @param int value : Value to decrease attribute by
        @return  :
        @author
        """
        pass

    def mod_attr(self, name, value = 1, operator):
        """
         Change value of an attribute in the character's dict using an operator

        @param string name : Name of attribute to modify
        @param int value : Value to modify the attribute by
        @param char operator : Operator to modify the attribute by
        @return  :
        @author
        """
        pass

    def _add_attr(self, value, name):
        """
         Add an attribute to the character's dict

        @param int value : Value of attribute
        @param string name : Name of attribute
        @return  :
        @author
        """
        pass



