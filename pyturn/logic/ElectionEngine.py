from BattleEngine import BattleEngine
from pyturn.data.PoliticalParty import PoliticalParty
from pyturn.data.GameplayVariables import GameplayVariables
from pyturn.data.ModAttribute import ModAttribute
from pyturn.data.WithBackfire import WithBackfire
from pyturn.logic.Game import *

class ElectionEngine (BattleEngine):

    """
     Runs the election

    :author: James Heslin
    """
    """ ATTRIBUTES

     Holds all gameplay data

    vars  (private)

    """
    
    def __init__(self):
        self.vars = None
        self.setup_data()

    def setup_data(self):
        """
         Sets up data for ElectionGame

        @return  :
        @author
        """
        self.vars = GameplayVariables()
        partyA = self.create_party("Republicans")
        charA = partyA.create_character("Mitt Romney", {'pop':50, 'ent':500,
                                                        'inv':1000},
                                        ["Appeal", "Defame", "Lie"])
        partyA.add_member(charA)
        partyA.set_active_member(charA)
        
        partyB = self.create_party("Democrats")
        charB = partyB.create_character("Barack Obama", {'pop':50, 'ent':500,
                                                         'inv':1000},
                                        ["Legislate", 
                                         "Publish Birth Certificate", 
                                         "Respond To Disaster"])
        partyB.add_member(charB)
        partyB.set_active_member(charB)
        
        self.vars.parties.append(partyA)
        self.vars.parties.append(partyB)

        self.vars.active_party = 1
        
        action1 = ModAttribute("Appeal", {'in':"{performer} is appealing to the rich!", 
            'done':"{performer} appealed to the rich! His {attr} attribute has increased by {value}!"}, 
                                    'popularity', 10, False)
        action2 = ModAttribute("Defame", {'in':"{performer} is insulting {target} publicly!", 
            'done':"{target}'s {attr} has fallen by {value}!"}, 
                                    'popularity', -10, True)
        action3 = ModAttribute("Lie", {'in':"{performer} is lying to the public about {target}'s policy!", 
            'done':"{performer} lied to the public! His {attr} has decreased by {value}!"}, 
                                    'entourage', -50, True)
        action4 = ModAttribute("Legislate", {'in':"{performer} is legislating to make {target} and his rich friends pay for everyone's healthcare!", 
            'done':"{performer} appealed to the middle classes! His {attr} attribute has increased by {value}!"}, 
                                    'popularity', 10, True)
        action5 = ModAttribute("Publish Birth Certificate", {'in':"{performer} is showing {target} up by proving he's American!", 
            'done':"{target}'s {attr} has fallen by {value}!"}, 
                                    'popularity', -10, True)
        action6 = ModAttribute("Respond To Disaster", {'in':"{performer} is responding to Hurricane Sandy by volunteering to help with relocation!", 
            'done':"{performer} impressed the public, but his {attr} have less to do so they have decreased by {value}!"}, 
                                    'entourage', -50, False)
        
        # decorate the Lie action
        action3 = WithBackfire(action3)
        
        
        actions = {'Appeal':action1, 'Defame':action2, 'Lie':action3,
                   'Legislate':action4, 'Publish Birth Certificate':action5,
                   'Respond To Disaster':action6}
        self.vars.actions_dict = actions

    def perform_action(self, action):
        """
         Performs an action

        @param int action : An integer representing the action to be performed
        @return list : List of strings representing the results, with a flag
                       in index 0 representing the type of result
        @author
        """
        act = self.vars.get_action(action)
        active_party = self.vars.parties[self.vars.active_party]
        performer = active_party.get_active_member()
        target = None
        # Hypothetically, we would call get_char_choice here somehow
        
        if act.needs_target:
            if len(self.vars.parties) == 2:
               for i in xrange(len(self.vars.parties)):
                   if not i == self.vars.active_party:
                       target_party = self.vars.parties[i]
                       target = target_party.get_active_member()
                       
            else:
                # Code for three or more parties here
                pass
            
        return (self.execute(act, performer, target))

    def execute(self, act, performer, target=None):
        """
         Do the action: Semantically, the performer is performing the action on the
         target

        @param Character performer : The Character performing the action
        @param Character target : The target of the action
        @return list : List of strings containing output about the action
        @author
        """
        results = ["display"]
        format_dict = {'performer': performer.name,
                       'target': target.name,
                       'attr': act.attr_str,
                       'value': abs(act.value)}
        
        if target:
            for op in act.operations:
                op(target, act.attr_str, act.increase_by)
                results.append(act.in_act_str % (performer.name, target.name))
                results.append(act.done_act_str % (target.name))
        else:
            for op in act.operations:
                op(performer, act.attr_str, act.increase_by)
                results.append(act.in_act_str % (performer.name, 'himself'))
                results.append(act.done_act_str % (performer.name))
            
        return results


    def create_party(self, name):
        """
         Factory method to create a new Party

        @param string name : The name of the party
        @return Party :
        @author
        """
        return PoliticalParty(name)
    
    def get_options(self):
        char = self.vars.parties[self.vars.active_party].get_active_member()
        ch_act =[CHOOSE_FLAG]
        ch_act.extend(char.actions_list)
        #print ch_act
        return ch_act

    def dead(self):
        for i in self.vars.parties:
            if i.dead():
                return [i.name + " are now out of the race!"]

    def end_turn(self):
        d = self.dead()
        if d is not None:
            res = [-1]
            res.extend(d)
            #print res
            return res
        if self.vars.active_party < len(self.vars.parties) -1:
            self.vars.active_party = self.vars.active_party+1
        else:
            self.vars.active_party = 0
        return [1]
            
    def get_desc(self):
        return self.vars.parties[self.vars.active_party].get_state()

# NOT USING THIS YET - It's wrong
    def get_char_choice(self, curr_action):
        """
         Get a list of the choices available as targets of the current action

        @param string curr_action : A string representing the current action
        @return string :
        @author
        """
        char = self.vars.parties[self.vars.active_party].get_active_member()
        return char.actions_list[curr_action]


