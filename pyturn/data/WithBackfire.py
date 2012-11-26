from pyturn.data.ActionDecorator import ActionDecorator
from pyturn.data.Character import Character

class WithBackfire(ActionDecorator):
    """
     Changes an Action to also have a negative effect on the performer,
     for half the value of the action itself on the same attribute.

    :author: Max Vizard
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

    def __init__(self, action):
        #ActionDecorator.__init__(action)
        self.act = action

    def get_operations(self):
        """
         Accessor method for operations attribute.
         
        @return list : The list of operations
        @author
        """
        op = self.act.get_operations()
        op.extend(Character.decr_attr)
        return op

    def get_in_act(self):
        """
         Accessor method for in_act_str attribute.
         
        @return string : The in_act_str attribute
        @author
        """
        in_act = self.act.get_in_act()
        in_act += ' This backfires and negatively affects {performer}.'
        return in_act
        

    def get_done_act(self):
        """
         Accessor method for done_act_str attribute.
         
        @return string : The done_act_str attribute
        @author
        """
        done_act = self.act.get_done_act()
        done_act += ' {performer}\'s {attr} fell {value} points.'
        return done_act
