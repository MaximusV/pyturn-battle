import unittest
from pyturn.presentation.CLIPresentation import CLIPresentation
from pyturn.presentation.GUIPresentation import GUIPresentation
from pyturn.presentation.CLInterface import CLInterface
from pyturn.presentation.GUInterface import GUInterface

class TestPresentation(unittest.TestCase):
    
    def setUp(self):
        self.pres_cli = CLIPresentation(CLInterface())
        self.pres_gui = GUIPresentation(GUInterface())

    def test_display(self):
        self.pres_cli.display("Some test message")
        self.pres_gui.display("Some test message")
        
    def test_choice(self):
        self.pres_cli.get_choice(["Test Action 1", "Test Action 2", 
                              "Test Action 3"])
        print self.pres_gui.get_choice(["Test Action 1", "Test Action 2", 
                              "Test Action 3"])

