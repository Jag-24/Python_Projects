#A BMI calculator

Name = input("Enter your name: ")
height_m = float(input("Enter your height(in meters): "))
weight_kg = float(input("Enter your weight(in kg): "))

bmi = weight_kg / (height_m ** 2)
print("bmi: ") 
print (bmi)

if bmi < 25 and bmi > 18:
    print(Name)
    print("is healthy")
if bmi > 25:
    print(Name)
    print("is overweight")
if bmi < 18:
    print(Name)
    print("is underweght")