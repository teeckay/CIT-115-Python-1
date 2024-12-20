# Compound Interest: Variables below ask for Money invested, at what interest rate as a percentage,
# Number of years of investment and how many times a year the investment compounds.

fPrincipal_Investment = float(input("Enter the starting principal: "))
fInterest_Rate = float(input("Enter the annual interest rate: ")) / 100
iCompounding = float(input("How many times per year is the interest compounded?: "))
fNumber_Of_Periods = int(input("For how many years will the account earn interest?: "))

# CALCULATIONS: Future investment value is calculated using the Compound Interest formula and provided variable amounts
# FV = PV * (1+r/m)^m*t

fFuture_Value = fPrincipal_Investment * ( 1 +  fInterest_Rate / iCompounding  ) ** ( iCompounding * fNumber_Of_Periods )

#OUTPUT to see the future value of the investment.

print(f"At the end of{ fNumber_Of_Periods: } years you will have $ {fFuture_Value:,.2f}")





