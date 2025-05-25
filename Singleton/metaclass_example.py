class NamingChecker(type):
    def __new__(cls, name, bases, dct):
        # print(name)
        # print(bases)
        # print(dct)
        for key in dct:
            print("key is", key)
            print("----------------------------------------------")
            print("dct is", dct[key])
            if callable(dct[key]) and not key.startswith('do_'):
                raise TypeError("All methods must start with 'do_'")
        return super().__new__(cls, name, bases, dct)

class Task(metaclass=NamingChecker):
    def do_work(self):
        print("Working...")

# This is fine, but below will raise an error
# class BadTask(metaclass=NamingChecker):
#     def work(self):  # ❌ Error!
#         pass


