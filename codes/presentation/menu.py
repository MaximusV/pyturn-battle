from menu_item import menu_item

class menu(menu_item):
    """Composite pattern: menu inherits from menu_item"""

    def __init__(self, label, menu_list):
        menu_item.__init__(self, label)
        self.menu_list = menu_list

    def display_list(self):
        i = 1
        for item in self.menu_list:
            item.present(i)       
            i += 1
        sel = int(raw_input("Select: "))
        return self.menu_list[sel-1]

    def select(self):
        self.display_list().select()
