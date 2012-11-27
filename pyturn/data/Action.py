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

         @type performer: Character
         @param performer: The Character who will be the semantic performer of the action
         @type target: Character
         @param target: The Character upon whom the action should be performed, if any
         @rtype: list
         @return: A list of strings representing the information about the action
         @author: Max Vizard
        """
        pass

    def get_operations(self):
        """
         Accessor method for operations attribute.
         @rtype: list
         @return: The list of operations
         @author: Max Vizard
        """
        pass

    def get_in_act(self):
        """
         Accessor method for in_act_str attribute.
         
         @rtype: string
         @return: The in_act_str attribute
         @author: Max Vizard
        """
        pass

    def get_done_act(self):
        """
         Accessor method for done_act_str attribute.
         
         @rtype: string
         @return: The done_act_str attribute
         @author: Max Vizard
        """
        pass
    
    def get_needs_target(self):
        """
         Accessor method for needs_target attribute.
         
         @rtype: boolean
         @return: Whether the Action needs a target
         @author: Max Vizard
        """
        pass
