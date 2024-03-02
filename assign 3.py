print("Welcome to the Temprature Conversion App")
#take user input
f=float(input("What is given temperature in degree Fahrenheit:"))

#convertions
celsius=(5*(f-32)/9)

kelvin=round(celsius+273.15)
#round function
f=round(f,4)
celsius=round(celsius ,4)
kelvin=round(kelvin ,4)

print(f"Degree Fahrenheit-{f}")
print(f"Degree celsius ={celsius}")
print(f"Degree kelvin={kelvin}")
