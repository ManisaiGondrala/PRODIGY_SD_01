print("Enter the Temperature value:")
n = float(input())

print("Enter the scale that you want to convert from:")
print("C - For Celsius")
print("K - For Kelvin")
print("F - For Fahrenheit")
c1 = input().strip()

print("Enter the scale that you want to convert to:")
print("C - For Celsius")
print("K - For Kelvin")
print("F - For Fahrenheit")
c2 = input().strip()

if c1.upper() == c2.upper():
    print("You have entered the same scale for both conversion. Please enter a valid input.")
elif (c1.upper() == "C") and (c2.upper() == "K"):
    x = n + 273.15
    print(f"{n} Celsius converted to {x} Kelvin")
elif (c1.upper() == "C") and (c2.upper() == "F"):
    x = (1.8 * n) + 32
    print(f"{n} Celsius converted to {x} Fahrenheit")
elif (c1.upper() == "K") and (c2.upper() == "C"):
    x = n - 273.15
    print(f"{n} Kelvin converted to {x} Celsius")
elif (c1.upper() == "K") and (c2.upper() == "F"):
    x = ((n - 273.15) * 1.8) + 32
    print(f"{n} Kelvin converted to {x} Fahrenheit")
elif (c1.upper() == "F") and (c2.upper() == "K"):
    x = ((n - 32) * 5/9) + 273.15
    print(f"{n} Fahrenheit converted to {x} Kelvin")
elif (c1.upper() == "F") and (c2.upper() == "C"):
    x = (n - 32) * 5/9
    print(f"{n} Fahrenheit converted to {x} Celsius")
else:
    print("Invalid input. Please enter valid temperature scales.")
