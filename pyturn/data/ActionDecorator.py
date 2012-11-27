from pyturn.data.Action import Action
from pyturn.data.Character import Character


class ActionDecorator (Action):

    """
     Decorates an Action with additional functionality

    @author: Max Vizard
    """

    """ ATTRIBUTES

     The Action being decorated

    act  (private)

     The string to display after the action

    done_act_string  (private)

     The string to display during the action

    in_act_string  (private)

    """

    #def __init__(self, action):
    #    self.act = action

    def execute(self, performer, target=None):
        """
         Perform the action. Semantically, performer performs the action on
         target.

         @type performer: Character
         @param performer: The Character who will be the semantic
                                performer of the action
         @type target: Character
         @param target: The Character upon whom the action should be
                                performed, if any
         @rtype: list
         @return: A list of strings representing the information about
                        the action
         @author: Max Vizard
        """
        pass
        #return self.act.execute(performer, target)

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