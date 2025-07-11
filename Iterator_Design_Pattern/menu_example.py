from abc import ABC, abstractmethod

# -----------------------------
# Iterator Interface
# -----------------------------
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

# -----------------------------
# Concrete Iterators
# -----------------------------
class DinerMenuIterator(Iterator):
    def __init__(self, items):
        self.items = items
        self.position = 0

    def has_next(self):
        return self.position < len(self.items)

    def next(self):
        if not self.has_next():
            raise StopIteration
        item = self.items[self.position]
        self.position += 1
        return item


class PancakeHouseMenuIterator(Iterator):
    def __init__(self, items):
        self.items = items
        self.position = 0

    def has_next(self):
        return self.position < len(self.items)

    def next(self):
        if not self.has_next():
            raise StopIteration
        item = self.items[self.position]
        self.position += 1
        return item


# -----------------------------
# Menu Item
# -----------------------------
class MenuItem:
    def __init__(self, name, description, vegetarian, price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def __str__(self):
        return f"{self.name}, {self.price} -- {self.description}"

# -----------------------------
# Menu Interfaces
# -----------------------------
class Menu(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

# -----------------------------
# Menus
# -----------------------------
class DinerMenu(Menu):
    def __init__(self):
        self.menu_items = []
        self.add_item("Vegetarian BLT", "Fakin' Bacon with lettuce & tomato on whole wheat",
                      True, 2.99)
        self.add_item("BLT", "Bacon with lettuce & tomato on whole wheat",
                      False, 2.99)
        self.add_item("Soup of the day", "Soup with a side of potato salad",
                      False, 3.29)

    def add_item(self, name, description, vegetarian, price):
        self.menu_items.append(MenuItem(name, description, vegetarian, price))

    def create_iterator(self):
        return DinerMenuIterator(self.menu_items)


class PancakeHouseMenu(Menu):
    def __init__(self):
        self.menu_items = []
        self.add_item("Pancake Breakfast", "Pancakes with scrambled eggs and toast", True, 2.99)
        self.add_item("Regular Pancake", "Pancakes with fried eggs and sausage", False, 2.99)
        self.add_item("Blueberry Pancake", "Pancakes with blueberries", True, 3.49)

    def add_item(self, name, description, vegetarian, price):
        self.menu_items.append(MenuItem(name, description, vegetarian, price))

    def create_iterator(self):
        return PancakeHouseMenuIterator(self.menu_items)


# -----------------------------
# Waitress (Client)
# -----------------------------
class Waitress:
    def __init__(self, pancake_menu, diner_menu):
        self.pancake_menu = pancake_menu
        self.diner_menu = diner_menu

    def print_menu(self):
        pancake_iterator = self.pancake_menu.create_iterator()
        diner_iterator = self.diner_menu.create_iterator()

        print("MENU\n----\nBREAKFAST")
        self._print_menu(pancake_iterator)

        print("\nLUNCH")
        self._print_menu(diner_iterator)

    def _print_menu(self, iterator):
        while iterator.has_next():
            item = iterator.next()
            print(item)


# -----------------------------
# Main Program
# -----------------------------
if __name__ == "__main__":
    pancake_menu = PancakeHouseMenu()
    diner_menu = DinerMenu()
    waitress = Waitress(pancake_menu, diner_menu)
    waitress.print_menu()
