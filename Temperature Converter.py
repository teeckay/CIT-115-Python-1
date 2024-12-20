# Introduction and asking for temperature and temperature type input from the user.

print("Welcome, I am Tiudy Kamau, Let us Calculate some Temperatures")
fTemperature = float( input("Enter a Temperature: ") )
sTemperature_Type =  input("Is the temp F for Fahrenheit or C for Celsius?:")

# Temperature Calculations and Output for either F or f for Fahrenheit and C or c for Celsius:
if sTemperature_Type == "F":
     if fTemperature > 212:
         print( "Temp can not be > 212")
         raise SystemExit
     else:
         fCelsius = ( 5.0 / 9 ) * ( fTemperature - 32 )
         print(f"The Celsius equivalent is: {fCelsius:,.1f} " )

elif sTemperature_Type == "f":
    if fTemperature > 212:
         print( "Temp can not be > 212")
         raise SystemExit
    else:
         fCelsius = ( 5.0 / 9 ) * ( fTemperature - 32 )
         print(f"The Celsius equivalent is: {fCelsius:,.1f} " )

elif sTemperature_Type == "C":
    if fTemperature > 100:
        print("Temp can not be > 100")
        raise SystemExit
    else:
        fFahrenheit = ( (9.0 / 5.0 ) * fTemperature + 32 )
        print(f"The Fahrenheit equivalent is: {fFahrenheit:,.1f} ")

elif sTemperature_Type == "c":
    if fTemperature > 100:
        print("Temp can not be > 100")
        raise SystemExit
    else:
        fFahrenheit = ( (9.0 / 5.0 ) * fTemperature + 32 )
        print(f"The Fahrenheit equivalent is: {fFahrenheit:,.1f} ")

else:
     print("You must enter an F or a C")
     raise SystemExit