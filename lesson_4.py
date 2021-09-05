import math

#assignment #1
def conversion(fahrenheit):
    celsius = float(((fahrenheit-32)*5)/9)
    return(celsius)
print("98.6 can be converted to",conversion(98.6), "celsius")

#assignment2 
def sphere_volume(radius):
    volume = float(((radius**3)*math.pi)*4/3)
    return volume
print(sphere_volume(2))

#assignment 3

def factorial(num):
    num1=1
    if num <0:
        return None
    elif num == 0:
        return 1
    for i in range(1,num+1):
        num1 = num1*i
    return num1
print(factorial(4))