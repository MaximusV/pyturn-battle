import unittest
from codes.presentation.CLIPresentation import *
from codes.presentation.GameCLI import *

class TestPresentation(unittest.TestCase):
    
    def setUp(self):
        self.pres = CLIPresentation(GameCLI())

    def test_display(self):
        self.pres.display("Some test message")
        
    def test_choice(self):
        self.pres.get_choice(["Test Action 1", "Test Action 2", 
                              "Test Action 3"])

