#Temperature converter program

def celsius_to_farenheit(celsius):
    return (celsius *9/5)+32
def farenheit_to_celsius(farenheit):
    return (farenheit -32)*5/9
def kelvin_to_celsius(kelvin):
    return (kelvin +273.15)
def celsius_to_kelvin(celsius):
    return (celsius -273.15)
def kelvin_to_fareiheit(kelvin):
    return (kelvin +273.15)*9/5+32
def farenheit_to_kelvin(farenheit):
    return (farenheit -273.15)*5/9+32


print("Temperature converter")
print("1. celsius to farenheit")
print("2. farenheit to celsius")
print("3.kelvin to celsius")
print("4. celsius to kelvin")
print("5. kelvin to farenheit")
print("6. farenheit to kelvin")

choice=int(input("Enter your choice (1-6):"))
temp=float(input("Enter the temperature to convert:"))

if choice==1:
    print(f"{temp} degree celsius is equal to {celsius_to_farenheit(temp)} degree farenheit")
elif choice==2:
    print(f"{temp} degree farenheit is equal to {farenheit_to_celsius(temp)} degree celsius")
elif choice==3:
    print(f"{temp} kelvin is equal to {kelvin_to_celsius(temp)} degree celsius")
elif choice==4:
    print(f"{temp} degree celsius is equal to {celsius_to_kelvin(temp)} kelvin")
elif choice==5:
    print(f"{temp} degree farenheit is equal to {farenheit_to_kelvin(temp)} kelvin")
elif choice==6:
    print(f"{temp} kelvin is equal to {kelvin_to_farenheit(temp)} degree farenheit")
else:   
    print("Invalid choice,please run the program again and select a valid option.")

    