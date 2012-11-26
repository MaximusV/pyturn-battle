import unittest
from pyturn.data.Character import Character
from pyturn.data.ModAttribute import ModAttribute
from pyturn.data.WithBackfire import WithBackfire


class decorator_test(unittest.TestCase):

    def setUp(self):
        self.tom = Character('Tom', {'HP': 10, 'AD': 5, 'DF': 3})
        self.dick = Character('Dick', {'HP': 10, 'AD': 5, 'DF': 3})
        self.decr_act = ModAttribute("Punch",
                                        {'in': "%s punched %s!",
                                         'done': "That really hurt %s!"},
                                        'HP', 8)

    def testUndecoratedAttack(self):
        #print 'ModAttribute.execute(Tom, Dick) \n'
        results = self.decr_act.execute(self.tom, self.dick)

        self.assertEqual(results[1], 'Tom punched Dick!')
        self.assertEqual(results[2], 'That really hurt Dick!')

    def testDecoratedAttack(self):
        print 'ModAttribute.execute(Tom, Dick) \n'
        act_with_backfire = WithBackfire(self.decr_act)
        results = self.decr_act.execute(self.tom, self.dick)
        print 'Results: \n'
        for res in results:
            print '\t' + res + '\n'

        print 'Decorating.. WithBackfire(ModAttribute)\n'
        results = act_with_backfire.execute(self.tom, self.dick)
        print 'Results: \n'
        for res in results:
            print '\t' + res + '\n'

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
