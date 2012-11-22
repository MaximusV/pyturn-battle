from codes.observer import ISubject
import operator as operate

class Character (ISubject):

    """
     Stores and manages data relating to an individual character and their attributes

     :author: Max Vizard
    """

    """ ATTRIBUTES

     A dict of all the character's attributes

    attributes_dict  (protected)

     Unique identifier of the character

    id  (public)

     Static counter to keep track of how many characters have been created - used to
     assign IDs

    CHARACTER_COUNT  (private)

     The Character's name

    name  (private)

    """
    
    CHARACTER_COUNT = 0
    
    def __init__(self, name, attr_dict={'HP': 10, 'DF': 3, 'AD': 1}):
        self.name = name
        self.attributes_dict = attr_dict
        self.id = Character.CHARACTER_COUNT
        Character.CHARACTER_COUNT += 1

    def remove_attr(self, name):
        """
         Remove an attribute from the character's dict

        @param string name : Name of attribute to remove
        @return void :
        @author 
        """
        del self.attributes_dict[name]

    def incr_attr(self, name, value = 1):
        """
         Increase value of an attribute in the character's dict

        @param string name : Name of attribute
        @param int value : Value to increase the attribute by
        @return void :
        @author
        """
        try:
            self.attributes_dict[name] += value
        except ValueError:
            print 'Expected a numerical value'

    def decr_attr(self, name, value = 1):
        """
         Decrease value of an attribute in the character's dict

        @param string name : Name of attribute to decrease
        @param int value : Value to decrease attribute by
        @return void :
        @author
        """
        try:
            self.attributes_dict[name] -= value
        except ValueError:
            print 'Expected a numerical value'
            

    def mod_attr(self, name, value = 1, operator):
        """
         Change value of an attribute in the character's dict using an operator

        @param string name : Name of attribute to modify
        @param int value : Value to modify the attribute by
        @param char operator : Operator to modify the attribute by
        @return void :
        @author
        """
        op_dict = {'+': operate.add,'-': operate.sub, '*': operate.mul, '/': operate.div }
        try:
            self.attributes_dict[name] = op_dict[operator](self.attributes_dict, value)
        except ValueError:
            print 'Expected a numerical value' 

    def add_attr(self, value, name):
        """
         Add an attribute to the character's dict

        @param int value : Value of attribute
        @param string name : Name of attribute
        @return void :
        @author
        """
        if not self.attributes_dict[name]:
            self.attributes_dict[name] = value
        else:
            print 'Attribute already exists'
        
