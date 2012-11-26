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
        #return self.act.execute(performer, target)


