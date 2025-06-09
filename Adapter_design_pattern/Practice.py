from abc import ABC, abstractmethod


class ITarget(ABC):
    @abstractmethod
    def request(self):
        pass


class MyTarget(ITarget):
    def request(self):
        print("***MyTarget send a request***")

# ----------------------------------------------------------------

class IThirdPartyTarget(ABC):
    @abstractmethod
    def specific_request(self):
        pass

class ThirdPartyTargetAdaptee(IThirdPartyTarget):
    def specific_request(self):
        print("$$$ThirdPartyTargetAdaptee send a request$$$")


# ---------------------------------------------------------------------------
class Client:
    def __init__(self, target):
        self.target = target

    def do_somthing(self):
        print("I'm calling the request method of target:")
        self.target.request()
        print("the request method of target has been called!")
# -----------------------------------------------------------------------------
# object Adapter:
class TargetAdapter(ITarget):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        self.adaptee.specific_request()

# class adapter:
class TargetClassAdapter(ThirdPartyTargetAdaptee, ITarget):
    def request(self):
        self.specific_request()

# -----------------------------------------------------------------------------
# main program
def main():
    # works as well as we expected
    my_target = MyTarget()
    client1 = Client(my_target)
    client1.do_somthing()
    print(100*'-')
    # it's not work!
    third_party_adaptee = ThirdPartyTargetAdaptee()
    # we must convert to out expected, using adapter
    adapter = TargetAdapter(third_party_adaptee)
    client2 = Client(adapter)
    client2.do_somthing()
    print(100*'-')
    class_adapter = TargetClassAdapter()
    client3 = Client(class_adapter)
    client3.do_somthing()



if __name__ == "__main__":
    main()
