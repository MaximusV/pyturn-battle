from codes.data.ActionDecorator import ActionDecorator
from codes.data.Character import Character 
from codes.data.Action import Action

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
        
    def execute(self, performer, target):
        """
         Perform the action. Semantically, performer performs the action on target.

        @param Character performer : The Character who will be the semantic performer of the action
        @param Character target : 
        @return string :
        @author
        """
        pre_results = self.act.execute()
        try:
            pre_results[0] = pre_results[0][0,-1] + 'on the internet!'
            pre_results[1] = pre_results[1][0,-1] + '. %s\'s popularity has risen, especially with the younger vote!'
            
            performer.incr_attr('pop', 5)
        except IndexError:
            print 'Expected at least two result strings from Action %s' % self.act.name


