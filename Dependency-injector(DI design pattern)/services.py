# services.py
class Engine:
    def start(self):
        return "Engine started!"

class Engine1:
    def start(self):
        return "Engine1 started!"

class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def drive(self):
        return self.engine.start()