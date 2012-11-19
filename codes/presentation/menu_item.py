class menu_item:
    def __init__(self, label):
        self.label = label # The label that will be shown
        #self.exe = exe # The executable that is called on selecting

    def present(self, n):
        print n, self.label

    def select(self):
        #exe()
        print self.label, "!!!!"
