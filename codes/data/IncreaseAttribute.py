from Action import *
from Character import *
from Function_pointer import *

class IncreaseAttribute (Action):

    """
     Increase an attribute of a Character

    :version:
    :author:
    """

    """ ATTRIBUTES

     String to display during the action
     

    in_act_string  (private)

     The string to display after the action is finished

    done_act_string  (private)

     List of operations that make up the Action

    operations  (private)

     

    attribute  (private)

     How much to increase the attribute by

    increase_by  (private)

     Name of action
     

    name  (private)

    """

    def execute(self, performer, target):
        """
         Do the action: Semantically, the performer is performing the action on the
         target

        @param Character performer : The Character performing the action
        @param Character target : The target of the action
        @return string :
        @author
        """
        pass



