# NAMED CONSTANTS
nMERCURY_FACTOR = 0.38
nVENUS_FACTOR = 0.91
nMOON_FACTOR = 0.165
nMARS_FACTOR = 0.38
nJUPITER_FACTOR = 2.34
nSATURN_FACTOR = 0.93
nURANUS_FACTOR = 0.92
nNEPTUNE_FACTOR = 1.12
nPLUTO_FACTOR = 0.066

# 1. Input the name and the Earth Weight.
sName = input("What is Your Name : ")
fEarth_Weight = float(input("And What is your Earth Weight?: "))

#2. Calculations; Weight = Earth Weight x specific planet's Surface Gravity Factor
nMercuryWeight = fEarth_Weight * nMERCURY_FACTOR
nVenusWeight = fEarth_Weight * nVENUS_FACTOR
nMoonWeight = fEarth_Weight * nMOON_FACTOR
nMarsWeight = fEarth_Weight * nMARS_FACTOR
nJupiterWeight = fEarth_Weight * nJUPITER_FACTOR
nSaturnWeight = fEarth_Weight * nSATURN_FACTOR
nUranusWeight = fEarth_Weight * nURANUS_FACTOR
nNeptuneWeight = fEarth_Weight * nNEPTUNE_FACTOR
nPlutoWeight = fEarth_Weight * nPLUTO_FACTOR

# 3 Output weights on different planets
print( sName,"here are your weights on our Solar System's planets:")
print(format("Weight on Mercury:", "40s"), format(nMercuryWeight,'10.2f'))
print(format("Weight on Venus:", "40s"), format(nVenusWeight,'10.2f'))
print(format("Weight on Moon:", "40s"), format(nMoonWeight,'10.2f'))
print(format("Weight on Mars:", "40s"), format(nMarsWeight,'10.2f'))
print(format("Weight on Jupiter:", "40s"), format(nJupiterWeight,'10.2f'))
print(format("Weight on Saturn:", "40s"), format(nSaturnWeight,'10.2f'))
print(format("Weight on Uranus:", "40s"), format(nUranusWeight,'10.2f'))
print(format("Weight on Neptune:", "40s"), format(nNeptuneWeight,'10.2f'))
print(format("Weight on Pluto:", "40s"), format(nPlutoWeight,'10.2f'))


