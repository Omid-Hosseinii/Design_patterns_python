# container.py
from dependency_injector import containers, providers
from services import Engine, Car, Engine1

class Container(containers.DeclarativeContainer):
    engine_provider = providers.Singleton(Engine)  # Singleton: Same instance everywhere
    engine_provider2 = providers.Singleton(Engine1)  # Singleton: Same instance everywhere
    car_provider1 = providers.Factory(Car, engine=engine_provider)  # New Car each time
    car_provider2 = providers.Factory(Car, engine=engine_provider2)  # New Car each time