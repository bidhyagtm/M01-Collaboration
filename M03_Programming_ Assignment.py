"""
Filename: M03_Programming_Assignment.py
Author: Bidhya Gautam
Date: 2/1/2023

This program accepts user input for a car. The app store "car" as a default vehicle in a super class and 
ask the user for the year, make, model, doors, and type of roof and store the data in the corresponding attributes .
User's data is printed out.
"""

#Vehicle class definition
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

#Automobile class definition
class Automobile(Vehicle):
    #assigning 'car' as default vehicle type for automobile class
    def __init__(self, year, make, model, doors, roof, vehicle_type='car'):
        #calling parent class method
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

#main function definition
def main():
    #initializing the automobile object
    car = Automobile(None, None, None, None, None)
    #getting inputs from the users and saving into the attributes
    print("\nPlease enter the details of a car")
    car.year = input("Year: ")
    car.make = input("Make: ")
    car.model = input("Model: ")
    car.doors = input("Doors (2 or 4): ")
    car.roof = input("Roof (solid or sun roof): ")
    #printing the data
    print("\n***Vehicle Details***")
    print("Type:", car.vehicle_type)
    print("Year:", car.year)
    print("Make:", car.make)
    print("Model:", car.model)
    print("Number of doors:", car.doors)
    print("Type of roof:", car.roof)

if __name__ == '__main__':
    main()