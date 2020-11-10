import math
# Handling of exception

try:
    c = 8/0
    print(c)

except ZeroDivisionError:
    print("Cannot devide by zero")

finally:
    print("Check once again!!!")

print()

try:
    b = sqrt(-47)
    print(b)
except:
    print("Enter a positive real number")


finally:
    print("Sqaure of a real number cannot be negative")


# Raising an exception
# If the temperature in Kelvin is negative,exception will be raised
# After raising an exception, code after it will not get executed

temp_k = float(input("Enter temperature in Kelvin:"))


def temp_conversion(temp_k):
    temp_f = (temp_k-273.15)*(9/5)+32
    return temp_f


if temp_k < 0:
    raise Exception("Temperature in Kelvin cannot be negative")
else:
    print("Temperature in Fahrenheit:", temp_conversion(temp_k))
