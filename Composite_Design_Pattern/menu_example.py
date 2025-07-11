from abc import ABC, abstractmethod
from typing import List


# ===== COMPONENT =====
class MenuComponent(ABC):
    def add(self, component: "MenuComponent"):
        raise NotImplementedError()

    def remove(self, component: "MenuComponent"):
        raise NotImplementedError()

    def get_child(self, index: int) -> "MenuComponent":
        raise NotImplementedError()

    def get_name(self) -> str:
        raise NotImplementedError()

    def get_description(self) -> str:
        raise NotImplementedError()

    def get_price(self) -> float:
        raise NotImplementedError()

    def is_vegetarian(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def print(self):
        pass


# ===== LEAF =====
class MenuItem(MenuComponent):
    def __init__(self, name: str, description: str, vegetarian: bool, price: float):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_price(self) -> float:
        return self.price

    def is_vegetarian(self) -> bool:
        return self.vegetarian

    def print(self):
        veg = "(v)" if self.vegetarian else ""
        print(f"  {self.name} {veg}, {self.price} -- {self.description}")


# ===== COMPOSITE =====
class Menu(MenuComponent):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.menu_components: List[MenuComponent] = []

    def add(self, component: MenuComponent):
        self.menu_components.append(component)

    def remove(self, component: MenuComponent):
        self.menu_components.remove(component)

    def get_child(self, index: int) -> MenuComponent:
        return self.menu_components[index]

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def print(self):
        print(f"\n{self.get_name()}, {self.get_description()}")
        print("-" * 40)
        for component in self.menu_components:
            component.print()


# ===== CLIENT =====
class Waitress:
    def __init__(self, all_menus: MenuComponent):
        self.all_menus = all_menus

    def print_menu(self):
        self.all_menus.print()


# ===== MAIN PROGRAM =====
def main():
    pancake_house_menu = Menu("PANCAKE HOUSE MENU", "Breakfast")
    diner_menu = Menu("DINER MENU", "Lunch")
    cafe_menu = Menu("CAFE MENU", "Dinner")

    all_menus = Menu("ALL MENUS", "All menus combined")
    all_menus.add(pancake_house_menu)
    all_menus.add(diner_menu)
    all_menus.add(cafe_menu)

    pancake_house_menu.add(MenuItem("Pancakes", "Delicious pancakes", True, 2.99))
    pancake_house_menu.add(MenuItem("Waffles", "Waffles with syrup", True, 3.59))

    diner_menu.add(MenuItem("Burger", "Beef burger with fries", False, 5.99))
    diner_menu.add(MenuItem("Veggie BLT", "Veggie bacon with lettuce & tomato", True, 4.99))

    cafe_menu.add(MenuItem("Soup", "Hot vegetable soup", True, 3.29))
    cafe_menu.add(MenuItem("Steak", "Grilled steak with veggies", False, 8.99))

    waitress = Waitress(all_menus)
    waitress.print_menu()


main()
