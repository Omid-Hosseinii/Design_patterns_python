# Old interface
class OldInterface:
    def old_method(self):
        pass

# New interface
class NewInterface:
    def new_method(self):
        pass

# Two-Way Adapter
class TwoWayAdapter(OldInterface, NewInterface):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    # Old code calls this
    def old_method(self):
        print("Redirecting old_method to new_method...")
        return self.adaptee.new_method()

    # New code calls this
    def new_method(self):
        print("Redirecting new_method to old_method...")
        return self.adaptee.old_method()
