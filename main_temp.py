from temperature import celsius_to_fahrenheit
from temperature import fahrenheit_to_celsius
from temperature import celsius_to_kelvin

print("1.C to F")
print("2.F to C")
print("3.C to K")

ch = int(input("Enter choice: "))

if ch == 1:
    c = float(input("Enter C: "))
    print(celsius_to_fahrenheit.convert(c))

elif ch == 2:
    f = float(input("Enter F: "))
    print(fahrenheit_to_celsius.convert(f))

elif ch == 3:
    c = float(input("Enter C: "))
    print(celsius_to_kelvin.convert(c))