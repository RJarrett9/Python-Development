vehicleType = ""
vehicleYear = ""
vehicleMake = ""
vehicleModel = ""
vehicleDoor = ""
vehicleRoof = ""

class Vehicle:
    def __init__(self, type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


Type = Vehicle(input("What is the type of vehicle you are using? ex: car\n"))

vehicleYear = input("What is the year of your car?")
vehicleMake = input("Who is the maker of your car?")
vehicleModel = input("What is the model of your car?")
vehicleDoor = input("How many doors does your car have?")
vehicleRoof = input("What type of roof does your car have?")

vehicleInfo = Automobile(vehicleYear, vehicleMake, vehicleModel, vehicleDoor, vehicleRoof)

print("\n")
print("Vehicle type:", Type.type)
print("Year:", vehicleInfo.year)
print("Make:", vehicleInfo.make)
print("Model:", vehicleInfo.model)
print("Number of doors:", vehicleInfo.doors)
print("Roof type:", vehicleInfo.roof)
print("\n")