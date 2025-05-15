from abc import ABC, abstractmethod


class PizaaStore(ABC):
    def order_pizzas(self, type_):
        pizza = self.create_pizza(type_)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        print()
        print("Your pizza order have already prepared!")

    @abstractmethod
    def create_pizza(self, type_):
        pass


class NyPizzaStore(PizaaStore):
    def create_pizza(self, type_):
        if type_ == 'pepperoni':
            return NyStylePepperoniPizza()
        elif type_ == 'veggie':
            return NyStyleVeggiePizza()
        elif type_ == 'cheese':
            return NyStyleCheesePizza()


class ChicagoPizzaStore(PizaaStore):
    def create_pizza(self, type_):
        if type_ == 'pepperoni':
            return ChicagoStylePepperoniPizza()
        elif type_ == 'veggie':
            return ChicagoStyleVeggiePizza()
        elif type_ == 'cheese':
            return ChicagoStyleCheesePizza()





# Product
class Pizza:
    def __init__(self, name, dough, sauce, toppings):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings


    def prepare(self):
        print('Prepare' + self.name)
        print("Tossing dough:" + self.dough)
        print("Add sauce:" + self.sauce)
        print("Add toppings:")
        for topping in self.toppings:
            print("\t\t\t" + topping)
        print()



    def bake(self):
        print('Bake ' + self.name + " for 20 minutes")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")



class NyStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__(name="NY Style pepperoni",
                         dough="Thin crust dough",
                         sauce="Tomato sauce",
                         toppings=["Sauce", "cheese", "pepperoni"])


class NyStyleVeggiePizza(Pizza):
    def __init__(self):
        super().__init__(name="NY Style veggie",
                         dough="Thin crust dough",
                         sauce="Pesto sauce",
                         toppings=["Sauce", "cheese", "vegetable"])


class NyStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__(name="NY Style cheese",
                         dough="Thin crust dough",
                         sauce="Mustard sauce",
                         toppings=["Sauce", "Blue cheese", "Normal cheese"])


class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__(name="Chicago Style pepperoni",
                         dough="Thick crust dough",
                         sauce="Tomato sauce",
                         toppings=["Sauce", "cheese", "pepperoni"])


class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self):
        super().__init__(name="Chicago Style veggie",
                         dough="Thick crust dough",
                         sauce="Mustard sauce",
                         toppings=["Sauce", "cheese", "vegetable"])


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__(name="Chicago Style cheese",
                         dough="Thick crust dough",
                         sauce="Normal sauce",
                         toppings=["Sauce", "pesto cheese", "Normal cheese"])


# ---------------------------------------------------------------------------------------------
# Main Program

ny_pizza_store = NyPizzaStore()
chicago_pizza_store = ChicagoPizzaStore()

print("Ny pizza order:")
ny_pizza_store.order_pizzas("pepperoni")
print(100*"-")
print("Chicago pizza order:")
chicago_pizza_store.order_pizzas("pepperoni")
