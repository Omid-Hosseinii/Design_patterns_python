from abc import ABC, abstractmethod

# Interfaces Classes
# ----------------------------------------------------------------------------------------------------------------------

class IObserver(ABC):
    @abstractmethod
    def update(self): pass

class ISubject(ABC):
    @abstractmethod
    def register_observer(self, observer: IObserver): pass
    @abstractmethod
    def remove_observer(self, observer: IObserver): pass
    @abstractmethod
    def notify_observer(self): pass


class IDisplay(ABC):
    @abstractmethod
    def display(self): pass


# ----------------------------------------------------------------------------------------------------------------------
# Concrete Classes


class WeatherData(ISubject):
    def __init__(self):
        self.observer_list = []
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def register_observer(self, observer: IObserver):
        self.observer_list.append(observer)

    def remove_observer(self, observer: IObserver):
        self.observer_list.remove(observer)

    def notify_observer(self):
        for observer in self.observer_list:
            observer.update()


    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure

    def measurements_changed(self):
        self.notify_observer()

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()




class CurrentConditionsDisplay(IObserver, IDisplay):
    def __init__(self, weather_data: WeatherData):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def update(self):
        self.temperature = self.weather_data.get_temperature()
        self.humidity = self.weather_data.get_humidity()
        self.pressure = self.weather_data.get_pressure()
        self.display()

    def display(self):
        print("Current Conditions Display has been updated.")
        print("\ttemp is: ", self.temperature)
        print("\thumidity is: ", self.humidity)
        print("\tpressure is: ", self.pressure)
        print("-"*100)



class StatisticsDisplay(IObserver, IDisplay):
    def __init__(self, weather_data: WeatherData):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.temperature = None
        self.pressure = None

    def update(self):
        self.temperature = self.weather_data.get_temperature()
        self.pressure = self.weather_data.get_pressure()
        self.display()

    def display(self):
        print("Statistics Display has been updated.")
        print("\ttemp is: ", self.temperature)
        print("\tpressure is: ", self.pressure)
        print("-" * 100)



class ForecastDisplay(IObserver, IDisplay):
    def __init__(self, weather_data: WeatherData):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def update(self):
        self.temperature = self.weather_data.get_temperature()
        self.humidity = self.weather_data.get_humidity()
        self.pressure = self.weather_data.get_pressure()
        self.display()

    def display(self):
        print("Statistics Display has been updated.")
        print("\t The average is: ", (self.temperature + self.humidity + self.pressure) / 3 )
        print("-" * 100)


# ----------------------------------------------------------------------------------------------------------------------
# Main Program

def main():
    weather_data_station = WeatherData()
    current_conditions_display = CurrentConditionsDisplay(weather_data_station)
    statistics_display = StatisticsDisplay(weather_data_station)
    forecast_display = ForecastDisplay(weather_data_station)

    print('**************************************Update information**************************************')
    weather_data_station.set_measurements(0.121231, 0.121234, 0.121235)
    print('**************************************Update information**************************************')
    weather_data_station.set_measurements(0.1211, 0.1234, 0.1235)
    print('**************************************Update information**************************************')
    weather_data_station.set_measurements(2.1211, 3.1234, 5.1235)



if __name__ == "__main__":
    main()