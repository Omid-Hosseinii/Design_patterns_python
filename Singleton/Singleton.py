# A. Classic Singleton (Not thread-safe)
class Singleton:
    _instance = None

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("This is a singleton!")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Singleton()
        return cls._instance


# Usage
s1 = Singleton.get_instance()
s2 = Singleton.get_instance()
assert s1 is s2

# ---------------------------------------------------------------------------------------------------


# B. Thread-safe Singleton
import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if ThreadSafeSingleton._instance is not None:
            raise Exception("Use get_instance()")

    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = ThreadSafeSingleton()
        return cls._instance

# Usage
singleton = ThreadSafeSingleton.get_instance()


# ---------------------------------------------------------------------------------------------------

# C. Singleton using Decorator
def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class MyService:
    pass

# Usage
service1 = MyService()
service2 = MyService()
assert service1 is service2



# ---------------------------------------------------------------------------------------------------

# D. Singleton using Metaclass
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Config(metaclass=SingletonMeta):
    def __init__(self):
        self.name = "AppConfig"

# Usage
c1 = Config()
c2 = Config()
assert c1 is c2




# ---------------------------------------------------------------------------------------------------


# Example: Using Singleton behind the scenes, combined with DI

from abc import ABC, abstractmethod


# Interface (Abstraction)
class ILogger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass


# Concrete Singleton Implementation
class ConsoleLogger(ILogger):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConsoleLogger, cls).__new__(cls)
        return cls._instance

    def log(self, message: str):
        print(f"[LOG]: {message}")


# App depends on ILogger, not ConsoleLogger
class App:
    def __init__(self, logger: ILogger):
        self.logger = logger

    def run(self):
        self.logger.log("App started.")


