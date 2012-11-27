import unittest
from pyturn.data.Character import Character
from pyturn.data.ModAttribute import ModAttribute
from pyturn.data.WithBackfire import WithBackfire


class decorator_test(unittest.TestCase):

    def setUp(self):
        self.tom = Character('Tom', {'HP': 10, 'AD': 5, 'DF': 3})
        self.dick = Character('Dick', {'HP': 10, 'AD': 5, 'DF': 3})
        self.decr_act = ModAttribute("Punch",
                                        {'in': "{performer} punched {target}!",
                                         'done': "{target}'s {attr} reduced by {value}!"},
                                        'HP', -4)

    def testUndecoratedAttack(self):
        #print 'ModAttribute.execute(Tom, Dick) \n'
        
        results = self.decr_act.execute(self.tom, self.dick)

        self.assertEqual(results[1], 'Tom punched Dick!')
        self.assertEqual(results[2], 'Dick\'s HP reduced by 4!')

    def testDecoratedAttack(self):
        self.assertEqual(self.dick.attributes_dict['HP'], 10)
        self.assertEqual(self.tom.attributes_dict['HP'], 10)
        
        print 'ModAttribute.execute(Tom, Dick) \n'
        act_with_backfire = WithBackfire(self.decr_act)
        results = self.decr_act.execute(self.tom, self.dick)
        
        print 'Results: \n'
        for res in results[1:]:
            print '\t' + res + '\n'
        
        self.assertEqual(self.dick.attributes_dict['HP'], 6)
        self.assertEqual(self.tom.attributes_dict['HP'], 10)

        print 'Decorating.. WithBackfire(ModAttribute)\n'
        results = act_with_backfire.execute(self.tom, self.dick)
        print 'Results: \n'
        for res in results[1:]:
            print '\t' + res + '\n'
            
        self.assertEqual(self.dick.attributes_dict['HP'], 2)
        self.assertEqual(self.tom.attributes_dict['HP'], 8)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
