from Action import *
from Character import *
from Function_pointer import *

class ReduceAttribute (Action):

    """
     Reduce an attribute of a Character

    :version:
    :author:
    """

    """ ATTRIBUTES

     String to display during the action
     

    in_act_string  (private)

     

    done_act_string  (private)

     List of operations that make up the Action

    operations  (private)

     The attribute to increase

    attribute  (private)

     How much to reduce the attribute by

    reduce_by  (private)

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



