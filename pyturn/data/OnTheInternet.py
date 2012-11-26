from pyturn.data.ActionDecorator import ActionDecorator


class OnTheInternet (ActionDecorator):

    """
     Changes an Action to happen in the context of the Internet

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
        ActionDecorator.__init__(self, action)

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
            pre_results[0] = pre_results[0][0, -1] + 'on the internet!'
            pre_results[1] = pre_results[1][0, -1] + '. %s\'s popularity has\
                                    risen, especially with the younger vote!'

            performer.incr_attr('pop', 5)
        except IndexError:
            print 'Expected at least two result strings from Action %s' %
            (self.act.name)
