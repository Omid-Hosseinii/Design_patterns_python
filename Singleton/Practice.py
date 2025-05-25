# import threading
#
# class ClassicSingleton:
#     __instance = None
#
#     def __init__(self):
#         if self.__instance is not None:
#             raise Exception("ClassicSingleton is already initialized")
#
#
#     @classmethod
#     def get_instance(cls):
#         if cls.__instance is None:
#             cls.__instance = ClassicSingleton()
#         return cls.__instance
#
# # ------------------------------------------------------------------------------------
#
# class ThreadSafeSingleton:
#     _instance = None
#     _lock = threading.Lock()
#
#     def __init__(self):
#         if self._instance is not None:
#             raise Exception("ThreadSafeSingleton is already initialized")
#
#     @classmethod
#     def get_instance(cls):
#         with cls._lock:
#             if cls._instance is None:
#                 cls._instance = ThreadSafeSingleton()
#         return cls._instance


# ------------------------------------------------------------------------------------

# def singleton(cls):
#     _instances = {}
#
#     def wrapper(*args, **kwargs):
#         if cls not in _instances:
#             _instances[cls] = cls(*args, **kwargs)
#         return _instances[cls]
#     return wrapper
#
# @singleton
# class Logger:
#     def __init__(self, message):
#         self.message = message
#
#
# logger1 = Logger("hello")
# logger2 = Logger("world")
# print(logger1.message)
# print(logger2.message)


# ------------------------------------------------------------------------------------

# class MetaSingleton(type):
#     _instance = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instance:
#             cls._instance[cls] = super().__call__(*args, **kwargs)
#         return cls._instance[cls]
#
#
# class Logger(metaclass=MetaSingleton):
#     def __init__(self, message):
#         self.message = message
#
# logger1 = Logger("hello")
# logger2 = Logger("world")
# print(logger1.message)
# print(logger2.message)