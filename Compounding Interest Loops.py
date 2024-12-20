# While loop asking for different types of inputs, if not, raise a Value Error
while True:
    try:
        fDeposit = float(input("What is the Original Deposit (positive value): "))
        fInterestRate = float(input("What is the Interest Rate (positive value): ")) /100/12 # to decimal then per month
        iNumMonths = int(input("What is the Number of Months (positive value): "))
        fGoalAmt = float(input("What is the Goal Amount (can enter 0 but not negative): "))

        #If any values are negative, print the error msg and restart the loop from the top
        if fDeposit <= 0 or fInterestRate <= 0 or iNumMonths <= 0 or fGoalAmt < 0:
            raise ValueError
        else:
            break # Stop the loop if all values are valid

    except ValueError:
        print("Input must a positive numeric value")

# Calculations and Loop to execute num of months to compound interest rate
#Deposit for the month is multiplied by the interest rate then added to the deposit
# for a new calculation for next month
fGoalDepositCalc = fDeposit # 2 separate deposit variables to calculate number of months to goal amt
for iCompoundMonths in range(1,iNumMonths + 1):
    fInterestThisMonth = fDeposit * fInterestRate
    fDeposit += fInterestThisMonth
    print(f" Month {iCompoundMonths} Account Balance is $ {fDeposit:.2f}")

#Loop predicting number of compounding months to reach the Goal Amount
iGoalMonths = 0
while fGoalDepositCalc < fGoalAmt:
    fInterestThisMonth = fGoalDepositCalc * fInterestRate
    fGoalDepositCalc += fInterestThisMonth
    iGoalMonths += 1

# Output
print(f" It will take {iGoalMonths} months to reach the goal of $ {fGoalAmt:.2f}")




