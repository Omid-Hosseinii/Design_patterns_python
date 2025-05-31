from abc import ABC, abstractmethod

class IFlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyWithWings(IFlyBehavior):
    def fly(self):
        print("Flying with Wings")


class IQuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass

class Squack(IQuackBehavior):
    def quack(self):
        print("Squack")


class Duck:
    def __init__(self, fly_behavior: IFlyBehavior, quack_behavior: IQuackBehavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior


    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()


class MallardDuck(Duck):
    def __init__(self):
        self.fly = FlyWithWings()
        self.quack = Squack()
        super().__init__(self.fly, self.quack)

    def set_fly_behavior(self, fly_behavior: IFlyBehavior):
        self.fly = fly_behavior

    def set_quack_behavior(self, quack_behavior: IFlyBehavior):
        self.quack = quack_behavior



client_duck = MallardDuck()
client_duck.perform_fly()
client_duck.perform_quack()





