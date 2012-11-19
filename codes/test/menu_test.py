from menu_item import menu_item
from menu import menu

class menu_test:
    m_items = []
    m_items.append(menu_item("Attack"))
    m_items2 = []
    m_items2.append(menu_item("Blast"))
    m_items2.append(menu_item("Heal"))
    m_items3 = []
    m_items3.append(menu_item("Linktacular Slash"))
    m_items3.append(menu_item("Slashtacular Link"))
    m_items4 = []
    m_items4.append(menu_item("HP Potion"))
    m_items4.append(menu_item("Mana Potion"))
    m_items2.append(menu("Combo Attack", m_items3))
    m_items.append(menu("Special Attack", m_items2))
    m_items.append(menu("Potion", m_items4))
    m = menu("Top level", m_items)
    while True:
        m.select()
