
# Sub systems
class CPU:
    def start(self):
        print("CPU: Booting up processor...")

    def execute(self):
        print("CPU: Executing programs...")

class Memory:
    def load(self):
        print("Memory: Loading data into RAM...")

class HardDrive:
    def read(self):
        print("HardDrive: Reading system files...")

# _______________________________________________________________________________________________________________
# Facade Design Pattern
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        print("\n==== Starting Computer ====")
        self.cpu.start()
        self.memory.load()
        self.hard_drive.read()
        self.cpu.execute()
        print("==== Computer Ready ====\n")

# _______________________________________________________________________________________________________________
# Client code

# Without Facade (Complex)
print("\n** Without Facade **")
cpu = CPU()
memory = Memory()
hard_drive = HardDrive()
cpu.start()
memory.load()
hard_drive.read()
cpu.execute()

# With Facade (Simple)
print("\n** With Facade **")
computer = ComputerFacade()
computer.start_computer()  # Just one method call!