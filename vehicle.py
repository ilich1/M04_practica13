class vehicle:
    def __init__(self, make, model, year, color, numWheels, maxSpeed):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.num_wheels = numWheels
        self.max_speed = maxSpeed

    def getMake(self):
        return self.make

    def setMake(self, make):
        self.make = make

    def getModel(self):
        return self.model

    def setModel(self, model):
        self.model = model

    def getYear(self):
        return self.year

    def setYear(self, year):
        self.year = year

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getNumWheels(self):
        return self.numWheels

    def setNumWheels(self, num_wheels):
        self.numWheels = num_wheels

    def getMaxSpeed(self):
        return self.maxSpeed

    def setMaxSpeed(self, max_speed):
        self.maxSpeed = max_speed

    def parts(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Color:", self.color)
        print("Number of Wheels:", self.num_wheels)
        print("Max Speed:", self.max_speed)