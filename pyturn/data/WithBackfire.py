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

    def execute(self, performer, target=None):
        """
         Perform the action. Semantically, performer performs the action on
         target.

        @param Character performer : The Character who will be the semantic
                                     performer of the action
        @param Character target : The Character upon whom the action should be
                                  performed, if any
        @return string : A list of strings representing the information about
                         the action
        @author
        """
        pre_results = self.act.execute(performer, target)
        format_dict = {'performer': performer.name,
                       'attr': self.act.attr_str,
                       'value': abs(self.act.value) / 2}
        
        if target:
            format_dict['target'] = target.name
        
        try:
            pre_results[1] += ' However, this backfires and negatively affects {performer}.'
            pre_results[2] += ' {performer}\'s {attr} also reduced by {value} points!'
            
            pre_results[1] = pre_results[1].format(**format_dict)
            pre_results[2] = pre_results[2].format(**format_dict)
            performer.decr_attr(self.act.attr_str, abs(self.act.value) / 2)

            return pre_results

        except IndexError:
            print 'Expected at least two result strings from Action'
            print self.act.name

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

    def get_needs_target(self):
        """
         Accessor method for needs_target attribute.
         
        @return boolean : Whether the Action needs a target
        @author
        """
        return self.act.get_needs_target()