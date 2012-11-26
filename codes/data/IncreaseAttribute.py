from codes.data.Action import Action
from codes.data.Character import Character


class IncreaseAttribute (Action):

    """
     Increase an attribute of a Character

    :author: Max Vizard
    """

    """ ATTRIBUTES

     String to display during the action
     
    in_act_str  (private)

     The string to display after the action is finished

    done_act_str  (private)

     List of operations that make up the Action

    operations  (private)

    Name of the attribute in the Character attributes

    attr_str  (private)

     How much to increase the attribute by

    increase_by  (private)

     Name of action

    name  (private)
    
     Bool to indicate whether action expects target or not

    needs_target  (public)

    """

    def __init__(self,
                 name,
                 str_dict={'in': '', 'done': ''},
                 attr_str='',
                 incr_by=1,
                 needs_target=False):

        self.name = name
        self.in_act_str = str_dict.get('in', '')
        self.done_act_str = str_dict.get('done', '')
        self.operations = [Character.incr_attr, ]
        self.attr_str = attr_str
        self.increase_by = incr_by
        self.needs_target = needs_target
