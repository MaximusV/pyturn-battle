from pyturn.data.Action import Action
from pyturn.data.Character import Character


class ActionDecorator (Action):

    """
     Decorates an Action with additional functionality

    :author: Max Vizard
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

        @param Character performer : The Character who will be the semantic
                                     performer of the action
        @param Character target : The Chracter upon whom the action should be
                                  performed, if any
        @return list : A list of strings representing the information about
                        the action
        @author
        """
        pass
        #return self.act.execute(performer, target)

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

    def get_needs_target(self):
        """
         Accessor method for needs_target attribute.
         
        @return boolean : Whether the Action needs a target
        @author
        """
        pass