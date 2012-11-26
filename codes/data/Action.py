from codes.data.Character import Character


class Action(object):

    """
     Represents an action performed by a Character on a Character

    :author: Max Vizard
    """

    """ ATTRIBUTES

     The string to display during the action

    in_act_string  (private)

     The string to display after the action

    done_act_string  (private)

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
