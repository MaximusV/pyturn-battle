from codes.data.ActionDecorator import ActionDecorator


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
        try:
            pre_results[1] += ' However, this also backfires and negatively \
affects %s.' % performer.name
            pre_results[2] += ' %s\'s %s attribute also reduced by %i points!'
            pre_results[2] = pre_results[2] % (performer.name,
                            self.act.attr_str, self.act.increase_by / 2)

            performer.decr_attr(self.act.attr_str, self.act.increase_by / 2)

            return pre_results

        except IndexError:
            print 'Expected at least two result strings from Action'
            print self.act.name
