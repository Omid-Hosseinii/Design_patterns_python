from abc import ABC, abstractmethod

class Pizza:
    def __init__(self, name):
        self.name = name

    def prepare(self):
        pass

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass


class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__(name="pepperoni")


class ClamPizza(Pizza):
    def __init__(self):
        super().__init__(name="calm")


class VeggiePizza(Pizza):
    def __init__(self):
        super().__init__(name="veggie")


class CheesePizza(Pizza):
    def __init__(self):
        super().__init__(name="cheese")



class SimplePizzaFactory:

    @staticmethod
    def create_pizza(type_):
        if type_ == "pepperoni_pizza":
            return PepperoniPizza()
        if type_ == "clam_pizza":
            return ClamPizza()
        if type_ == "veggie_pizza":
            return VeggiePizza()
        if type_ == "cheese_pizza":
            return CheesePizza()


class PizzaStore:
    def __init__(self):
        pass

    @staticmethod
    def order_pizza(type_):
        pizza = SimplePizzaFactory.create_pizza(type_)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        print("Your pizza order have already prepared!")

# ---------------------------------------------------------------------------------------------
# Main Program

pizza_store = PizzaStore()
pizza_store.order_pizza("pepperoni_pizza")