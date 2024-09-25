class car:
    
    def __init__(self):
        print("please Insert Your Key")
        self.start_engine()
    
    def start(self):
        print("Car Started")
    
    def move(self):
        print("car Moving")
    
    def break_(self):
        print("car stopped")

    def start_engine(self):
        print("Engine Start")
        self.start()

class BMW(car):
    def __init__(self):
        print("Welcome to BMW World")
        super().__init__()

Bmw_car = BMW()

Bmw_car.move()

Bmw_car.break_()
