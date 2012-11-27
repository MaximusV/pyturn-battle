import operator as operate

class Character:

    """
     Stores and manages data relating to an individual character and their attributes

     @author: Max Vizard
    """

    """ ATTRIBUTES

     A dict of all the character's attributes

    attributes_dict  (protected)
    
    A list of strings representing Actions this Character can perform
    
    actions_list (private)

     Unique identifier of the character

    id  (public)

     Static counter to keep track of how many characters have been created - used to
     assign IDs

    CHARACTER_COUNT  (private)

     The Character's name

    name  (private)

    """
    
    CHARACTER_COUNT = 0
    
    def __init__(self, name, attr_dict={'HP': 10, 'DF': 3, 'AD': 1}, actions=[]):
        self.name = name
        self.attributes_dict = attr_dict
        self.id = Character.CHARACTER_COUNT
        self.actions_list = actions
        Character.CHARACTER_COUNT += 1

    def get_action(self, a_int):
        """
         Gets the action represented by the input
         
         @type a_int: int
         @param a_int: An integer representing an Action
         @rtype: Action
         @return: The Action represented by the input
         @author: Max Vizard
        """
        return self.actions_list[a_int]
    
    def get_state(self):
        """
         Gets the current state of the Character
         
         @rtype: list
         @return: A list of strings representing the Character's
                     current state
         @author: Max Vizard
        """
        a = []
        for i in self.attributes_dict:
            a.append(i+" "+str(self.attributes_dict[i]))
        return a

    def remove_attr(self, name):
        """
         Remove an attribute from the character's dict

         @type name: string
         @param name: Name of attribute to remove
         @author: Max Vizard 
        """
        del self.attributes_dict[name]

    def incr_attr(self, name, value = 1):
        """
         Increase value of an attribute in the character's dict

         @type name: string
         @param name: Name of attribute
         @type value: int
         @param value: Value to increase the attribute by
         @author: Max Vizard
        """
        try:
            self.attributes_dict[name] += value
        except ValueError:
            print 'Expected a numerical value'

    def decr_attr(self, name, value = 1):
        """
         Decrease value of an attribute in the character's dict

         @type name: string
         @param name: Name of attribute to decrease
         @type value: int
         @param value: Value to decrease attribute by
         @author: Max Vizard
        """
        try:
            self.attributes_dict[name] -= value
        except ValueError:
            print 'Expected a numerical value'
            

    def mod_attr(self, name, value = 1, operator='+'):
        """
         Change value of an attribute in the character's dict using an operator

         @type name: string
         @param name: Name of attribute to modify
         @type value: int
         @param value: Value to modify the attribute by
         @type operator: char
         @param operator: Operator to modify the attribute by
         @author: Max Vizard
        """
        op_dict = {'+': operate.add,'-': operate.sub, '*': operate.mul, '/': operate.div }
        try:
            self.attributes_dict[name] = op_dict[operator](self.attributes_dict, value)
        except ValueError:
            print 'Expected a numerical value' 

    def add_attr(self, value, name):
        """
         Add an attribute to the character's dict

         @type value: int
         @param value: Value of attribute
         @type name: string
         @param name: Name of attribute
         @author: Max Vizard
        """
        if not self.attributes_dict[name]:
            self.attributes_dict[name] = value
        else:
            print 'Attribute already exists'
        
    def dead(self):
        if self.attributes_dict.get('popularity') < 25:
            return True