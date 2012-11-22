import unittest
from codes.presentation.CLIPresentation import CLIPresentation
from codes.presentation.GUIPresentation import GUIPresentation
from codes.presentation.GameCLI import GameCLI
from codes.presentation.GameGUI import GameGUI

class TestPresentation(unittest.TestCase):
    
    def setUp(self):
        self.pres_cli = CLIPresentation(GameCLI())
        self.pres_gui = GUIPresentation(GameGUI())

    def test_display(self):
        self.pres_cli.display("Some test message")
        self.pres_gui.display("Some test message")
        
    def test_choice(self):
        self.pres_cli.get_choice(["Test Action 1", "Test Action 2", 
                              "Test Action 3"])
        print self.pres_gui.get_choice(["Test Action 1", "Test Action 2", 
                              "Test Action 3"])

