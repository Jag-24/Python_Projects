import math


Radius = input("Please enter radius: ")
Radius = float(Radius)
Volume = (4*math.pi*(Radius**3))/3
Volume = str(Volume)
print("Volume of sphere: " + Volume)