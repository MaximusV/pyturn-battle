from BattleEngine import BattleEngine
from codes.data.PoliticalParty import PoliticalParty
from codes.data.GameplayVariables import GameplayVariables
from codes.data.IncreaseAttribute import IncreaseAttribute
from codes.data.ReduceAttribute import ReduceAttribute
from codes.logic.Game import *

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
        
        action1 = IncreaseAttribute("Appeal", {'in':"%s is selling %s to the rich!", 
            'done':"%s appealed to the rich! His popularity has increased!"}, 
                                    'pop', 10, False)
        action2 = ReduceAttribute("Defame", {'in':"%s is insulting %s publicly!", 
            'done':"%s's popularity has fallen!"}, 
                                    'pop', 10, True)
        action3 = ReduceAttribute("Lie", {'in':"%s is lying to the public about %s's policy!", 
            'done':"%s lied to the public! His entourage has decreased!"}, 
                                    'ent', 50, True)
        action4 = IncreaseAttribute("Legislate", {'in':"%s is legislating to make %s and his rich friends pay for everyone's healthcare!", 
            'done':"%s appealed to the middle classes! His popularity has increased!"}, 
                                    'pop', 10, False)
        action5 = ReduceAttribute("Publish Birth Certificate", {'in':"%s is showing %s up by proving he's American!", 
            'done':"%s's popularity has fallen!"}, 
                                    'pop', 10, True)
        action6 = ReduceAttribute("Respond To Disaster", {'in':"%s is responding to Hurricane Sandy by volunteering %s to help with relocation!", 
            'done':"%s impressed the public, but his entourage have less to do so they have decreased numbers!"}, 
                                    'ent', 50, False)
        
        actions = {'Appeal':action1, 'Defame':action2, 'Lie':action3,
                   'Legislate':action4, 'Publish Birth Certificate':action5,
                   'Respond To Disaster':action6}
        self.vars.actions_dict = actions

    def perform_action(self, action):
        """
         Performs an action

        @param int action : An integer representing the action to be performed
        @return string :
        @author
        """
        #print "Action", action
        act = self.vars.get_action(action)
        #print act.name
        return (self.execute(act, self.vars.parties[self.vars.active_party].get_active_member()))

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
        
        if target:
            act.operations[0](target, act.attr_str, act.increase_by)
            results.append(act.in_act_str % (performer.name, target.name))
            results.append(act.done_act_str % (target.name))
        else:
            act.operations[0](performer, act.attr_str, act.increase_by)
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


