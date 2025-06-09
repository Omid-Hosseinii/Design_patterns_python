# The Adaptee has an incompatible interface
class Adaptee:
    def specific_request(self):
        return "Data from Adaptee"

# Target Interface expected by Client
class Target:
    def request(self):
        raise NotImplementedError

# Adapter translates from Target to Adaptee
class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specific_request()

# Client uses only the Target interface
def client_code(target: Target):
    print(target.request())

# Usage
adaptee = Adaptee()
adapter = Adapter(adaptee)
client_code(adapter)
