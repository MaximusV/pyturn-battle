import unittest
from pyturn.data.GameplayVariables import GameplayVariables
from pyturn.logic.DBManager import DBManager

from pyturn.data.Character import Character
from pyturn.data.PoliticalParty import PoliticalParty
from pyturn.data.ModAttribute import ModAttribute
from pyturn.data.WithBackfire import WithBackfire


class decorator_test(unittest.TestCase):

    def setUp(self):
        tom = Character('Tom', {'HP': 10, 'AD': 5, 'DF': 3})
        dick = Character('Dick', {'HP': 10, 'AD': 5, 'DF': 3})
        decr_act = ModAttribute("Punch",
                                        {'in': "{performer} punched {target}!",
                                         'done': "{target}'s {attr} reduced by {value}!"},
                                        'HP', -4)
        partA = PoliticalParty('Pirate Party')
        partA.add_member(tom)
        partA.add_member(dick)
        partA.set_active_member(tom)
                
        self.vars = GameplayVariables()
        self.vars.parties = [partA]
        self.vars.active_party = 0
        self.vars.actions_dict = {'Punch': decr_act}
        
    def testDecoration(self):
        self.db = DBManager(self.vars)
        
        print 'Attaching DBmanager to vars'
        self.vars.attach(self.db)
        
        dbs_last_subject = (self.db.last_sub, )
        #print vars(dbs_last_subject)
        self.vars.active_party = 666
        
        print 'Calling notify on self.vars'
        self.vars.notify()
        
        self.assertNotEqual(dbs_last_subject[0],
                         self.db.last_sub)
        print 'Asserted that DBManagers instance of vars has changed'
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
