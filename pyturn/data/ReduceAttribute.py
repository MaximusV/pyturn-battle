from pyturn.data.Action import Action
from pyturn.data.Character import Character

class ReduceAttribute (Action):

    """
     Reduce an attribute of a Character

    :author: Max Vizard
    """

    """ ATTRIBUTES

     String to display during the action
     
    in_act_string  (private)

     The string to display after the action is finished
    
    done_act_string  (private)

     List of operations that make up the Action

    operations  (private)

     Name of the attribute in the Character attributes

    attr_str  (private)

     How much to reduce the attribute by

    reduce_by  (private)

     Name of action

    name  (private)

    """
    
    def __init__(self, name, str_dict={'in':'', 'done':''}, attr_str='', reduce_by=1,):
            self.name = name
            self.in_act_str = str_dict.get('in', '')
            self.done_act_str = str_dict.get('done', '')
            self.operations = [Character.decr_attr,]
            self.attr_str = attr_str
            self.increase_by = reduce_by


