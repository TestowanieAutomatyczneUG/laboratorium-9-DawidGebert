from Car import Car

class CarImpl:
    def __init__(self, car: Car):
        self.car = car

    def impl_checkFuel(self):
        if self.car.needsFuel():
            return "Wystarczająco Paliwa"
        return "Za Mało paliwa"

    def impl_checkEngineTemperature(self):
        if self.car.getEngineTemperature() > 100:
            return "Silnik za gorący"
        return "Normalna temperatura silnika"

    def impl_setDesitnation(self, destination):
        return f"Kierunek to {destination}"