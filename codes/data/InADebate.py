from ActionDecorator import *
from Character import *
from Action import *

class InADebate (ActionDecorator):

    """
     Changes Action so that it happens in the context of a debate

    :version:
    :author:
    """

    """ ATTRIBUTES

     The Action being decorated

    act  (private)

     The string to display after the action

    done_act_string  (private)

     The string to display during the action

    in_act_string  (private)

     Name of action
     

    name  (private)

    """

    def execute(self, performer, target):
        """
         Perform the action. Semantically, performer performs the action on target.

        @param Character performer : The Character who will be the semantic performer of the action
        @param Character target : 
        @return string :
        @author
        """
        pass



