from codes.data import Action
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

    """
    
    def __init__(self, name, str_dict={'in':'', 'done':''}, attr_str='', incr_by=1,):
        self.name = name
        self.in_act_str = str_dict.get('in', '')
        self.done_act_str = str_dict.get('done', '')
        self.operations = [Character.incr_attr,]
        self.attr_str = attr_str
        self.increase_by = incr_by

    def execute(self, performer, target=None):
        """
         Do the action: Semantically, the performer is performing the action on the
         target

        @param Character performer : The Character performing the action
        @param Character target : The target of the action
        @return list : List of strings containing output about the action
        @author
        """
        results = []
        
        if target:
            self.operations[0](target, self.attr_str, self.increase_by)
            results.append(self.in_act_str % (performer.name, target.name))
            results.append(self.done_act_str % (target.name))
        else:
            self.operations[0](performer, self.attr_str, self.increase_by)
            results.append(self.in_act_str % (performer.name, 'himself'))
            results.append(self.done_act_str % (performer.name))
            
        return results
        



