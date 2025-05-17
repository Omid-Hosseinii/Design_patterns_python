from abc import ABC, abstractmethod


class PizaaStore(ABC):
    def order_pizzas(self, type_):
        pizza = self.create_pizza(type_)

        pizza.prepare()
        pizza.show_toppings()
        pizza.bake()
        pizza.cut()
        pizza.box()
        print()
        print("Your pizza order have already prepared!")

    @abstractmethod
    def create_pizza(self, type_):
        pass


class NYPizzaStore(PizaaStore):
    def __init__(self):
        self.ny_ingredient_factory = NYPizaaIngredientFactory()


    def create_pizza(self, type_):
        if type_ == 'cheese':
            return CheesePizza(self.ny_ingredient_factory)
        elif type_ == 'clam':
            return ClamPizza(self.ny_ingredient_factory)
        elif type_ == 'veggie':
            return VeggiePizza(self.ny_ingredient_factory)


class ChicagoPizzaStore(PizaaStore):
    def __init__(self):
        self.chicago_ingredient_factory = ChicagoPizaaIngredientFactory()


    def create_pizza(self, type_):
        if type_ == 'cheese':
            return CheesePizza(self.chicago_ingredient_factory)
        elif type_ == 'clam':
            return ClamPizza(self.chicago_ingredient_factory)
        elif type_ == 'veggie':
            return VeggiePizza(self.chicago_ingredient_factory)



class PizzaIngredientFactory:
    def __init__(self, Pizza_style_name):
        self.Pizza_style_name = Pizza_style_name

    def create_dough(self):
        pass

    def create_sauce(self):
        pass

    def create_cheese(self):
        pass

    def create_pepperoni(self):
        pass

    def create_clam(self):
        pass

    def veggies(self):
        pass


class NYPizaaIngredientFactory(PizzaIngredientFactory):
    def __init__(self):
        super().__init__("New York Pizza")

    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FreshClams()

    def veggies(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]




class ChicagoPizaaIngredientFactory(PizzaIngredientFactory):
    def __init__(self):
        super().__init__("Chicago Pizza")

    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_cheese(self):
        return MozzarellaCheese()

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FrozenClams()

    def veggies(self):
        return [BlackOlive(), Spanich(), EggPlant()]


class ThinCrustDough:
    def __init__(self):
        self.name = 'ThinCrustDough'


class MarinaraSauce:
    def __init__(self):
        self.name = 'MarinaraSauce'


class PlumTomatoSauce:
    def __init__(self):
        self.name = 'PlumTomatoSauce'


class ReggianoCheese:
    def __init__(self):
        self.name = 'ReggianoCheese'


class MozzarellaCheese:
    def __init__(self):
        self.name = 'MozzarellaCheese'


class Garlic:
    def __init__(self):
        self.name = 'Garlic'


class Onion:
    def __init__(self):
        self.name = 'Onion'


class Mushroom:
    def __init__(self):
        self.name = 'Mushroom'


class RedPepper:
    def __init__(self):
        self.name = 'RedPepper'


class BlackOlive:
    def __init__(self):
        self.name = 'BlackOlive'


class Spanich:
    def __init__(self):
        self.name = 'Spanich'


class EggPlant:
    def __init__(self):
        self.name = 'EggPlant'


class SlicedPepperoni:
    def __init__(self):
        self.name = 'SlicedPepperoni'


class FreshClams:
    def __init__(self):
        self.name = 'FreshClams'


class FrozenClams:
    def __init__(self):
        self.name = 'FrozenClams'


# Product
class Pizza(ABC):
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.cheese = None
        self.pepperoni = None
        self.clam = None
        self. veggies = []

    @abstractmethod
    def prepare(self):
        pass

    def show_toppings(self):
        toppings = (self.dough, self.sauce, self.cheese, self.pepperoni, self.clam, self.veggies)

        print("The toppings are:")
        for topping in toppings:
            if isinstance(topping, list):
                for item in topping:
                    print("\t" + item.name)
            elif topping:
                print(topping.name)


    def bake(self):
        print('Bake ' + self.name + " for 20 minutes")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def set_name(self, name_):
        self.name = name_

    def get_name(self):
        return self.name


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory
        super().__init__("Cheese " + ingredient_factory.Pizza_style_name)

    def prepare(self):
        print("preparing " + self.name)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()




class ClamPizza(Pizza):
    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory
        super().__init__("clam " + ingredient_factory.Pizza_style_name)

    def prepare(self):
        print("preparing " + self.name )
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()



class VeggiePizza(Pizza):
    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory
        super().__init__("Veggies " + ingredient_factory.Pizza_style_name)

    def prepare(self):
        print("preparing " + self.name )
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.veggies()


# ------------------------------------------------------------------------------------------------------------
# Main Program

# ny store
print()
print("New York Order:\n")
ny_pizza_store = NYPizzaStore()
ny_pizza_store.order_pizzas('veggie')
print(100*"-" + "\n" + "Chicago Order:\n")
# chicago store
chicago_pizza_store = ChicagoPizzaStore()
chicago_pizza_store.order_pizzas('veggie')
