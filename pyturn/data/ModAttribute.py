from pyturn.data.Action import Action
from pyturn.data.Character import Character


class ModAttribute (Action):

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

     How much to change the attribute by

    value  (private)

     Name of action

    name  (private)
    
     Bool to indicate whether action expects target or not

    needs_target  (public)

    """

    def __init__(self,
                 name,
                 str_dict={'in': '', 'done': ''},
                 attr_str='',
                 value=0,
                 needs_target=False):

        self.name = name
        self.in_act_str = str_dict.get('in', '')
        self.done_act_str = str_dict.get('done', '')
        self.operations = [Character.incr_attr]
        self.attr_str = attr_str
        self.value = value
        self.needs_target = needs_target

    def execute(self, performer, target=None):
        """
         Do the action: Semantically, the performer is performing the action on
         the target

        @param Character performer : The Character performing the action
        @param Character target : The target of the action
        @return list : List of strings containing output about the action
        @author
        """
        results = ["display"]
        
        format_dict = {'performer': performer.name,
                       'attr': self.attr_str,
                       'value': abs(self.value)}

        if target:
            format_dict['target'] = target.name
            self.operations[0](target, self.attr_str, self.value)
            results.append(self.in_act_str.format(**format_dict))
            results.append(self.done_act_str.format(**format_dict))
        else:
            self.operations[0](performer, self.attr_str, self.value)
            results.append(self.in_act_str.format(**format_dict))
            results.append(self.done_act_str.format(**format_dict))

        return results

    def get_operations(self):
        """
         Accessor method for operations attribute.
         
        @return list : The list of operations
        @author
        """
        return self.operations[:] # Returns a copy instead of actual attribute

    def get_in_act(self):
        """
         Accessor method for in_act_str attribute.
         
        @return string : The in_act_str attribute
        @author
        """
        return self.in_act_str[:] # Returns a copy instead of actual attribute

    def get_done_act(self):
        """
         Accessor method for done_act_str attribute.
         
        @return string : The done_act_str attribute
        @author
        """
        return self.done_act_str[:] # Returns a copy instead of actual attribute
    
    def get_needs_target(self):
        """
         Accessor method for needs_target attribute.
         
        @return boolean : Whether the Action needs a target
        @author
        """
        return self.needs_target
