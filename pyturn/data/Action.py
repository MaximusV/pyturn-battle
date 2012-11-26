from pyturn.data.Character import Character

class Action(object):

    """
     Represents an action performed by a Character on a Character

    :author: Max Vizard
    """

    """ ATTRIBUTES

     The string to display during the action

    in_act_str  (private)

     The string to display after the action

    done_act_str  (private)

     List of function pointers to functions that make up the action

    operations  (private)

     Name of action

    name  (private)

    """

    def execute(self, performer, target):
        """
         Perform the action. Semantically, performer performs the action on target.

        @param Character performer : The Character who will be the semantic performer of the action
        @param Character target : The Chracter upon whom the action should be performed, if any
        @return string : A list of strings representing the information about the action
        @author
        """
        pass

    def get_operations(self):
        """
         Accessor method for operations attribute.
         
        @return list : The list of operations
        @author
        """
        pass

    def get_in_act(self):
        """
         Accessor method for in_act_str attribute.
         
        @return string : The in_act_str attribute
        @author
        """
        pass

    def get_done_act(self):
        """
         Accessor method for done_act_str attribute.
         
        @return string : The done_act_str attribute
        @author
        """
        pass
