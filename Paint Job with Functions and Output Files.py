# Importing the math module to use the ceil function to round up to the next highest gallon
import math


# Get float input with validation function
def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Invalid entry. Please enter a positive float number.")
            else:
                return value
        except ValueError:
            print("Invalid entry. Please enter a positive float number.")


# Function to calculate how many gallons are needed for the job.
def getGallonsOfPaint(fSquareFtWall, fFeetPerGallonPaint):
    return int(math.ceil(fSquareFtWall / fFeetPerGallonPaint))


# Function to calculate Labor Hours to paint the wall as a float
def getLaborHours(fLaborHoursPerGallon, gallons_of_paint):
    return float(fLaborHoursPerGallon * gallons_of_paint)


# Function to return the Labor Cost to paint the wall as a float
def getLaborCost(fLaborHours, fPaintLaborPerHour):
    return float(fLaborHours * fPaintLaborPerHour)


# Function to calculate and return the Paint Cost to paint the wall
def getPaintCost(gallons_of_paint, fPaintPrice):
    return float(gallons_of_paint * fPaintPrice)


# Function to return the tax rate for the state the job is for
def getSalesTax(State_Job):
    if State_Job == "CT":
        fTax_Rate = .06
    elif State_Job == "MA":
        fTax_Rate = .0625
    elif State_Job == "ME":
        fTax_Rate = .085
    elif State_Job == "NH":
        fTax_Rate = .0
    elif State_Job == "RI":
        fTax_Rate = .07
    elif State_Job == "VT":
        fTax_Rate = .06
    else:
        fTax_Rate = 0.

    return fTax_Rate


# Function to output values to the screen formatted
def showCostEstimate(fSquareFtWall, fPaintPrice, fFeetPerGallonPaint, fLaborHoursPerGallon,
                     fPaintLaborPerHour, sState_Job, sLast_Name):
    # Calculate gallons of paint needed to print
    gallons_of_paint = getGallonsOfPaint(fSquareFtWall, fFeetPerGallonPaint)
    # Calculate labor hours needed to print
    Labor_Hours = getLaborHours(fLaborHoursPerGallon, gallons_of_paint)
    # Calculate labor cost to print
    Labor_Cost = getLaborCost(Labor_Hours, fPaintLaborPerHour)
    # Calculate paint cost to print
    Paint_Cost = getPaintCost(gallons_of_paint, fPaintPrice)
    # Get state tax rate to print
    State_Tax_Rate = getSalesTax(sState_Job)
    #Get tax to calculate total cost
    Tax = State_Tax_Rate * (Paint_Cost + Labor_Cost)
    # Calculate total cost to print
    Total_Cost = Labor_Cost + Paint_Cost + Tax

    # Create formatted output values to print to the screen assigned to a variable to then return
    # values printed with the function to use to write to the file.
    Output_To_Screen = (
        f" Customer Last Name: {sLast_Name}\n"
        f" Gallons of paint: {gallons_of_paint}\n"
        f" Hours of labor: {Labor_Hours:,.2f}\n"
        f" Paint charges: ${Paint_Cost:,.2f}\n"
        f" Labor charges: ${Labor_Cost:,.2f}\n"
        f" Tax: ${Tax:,.2f}\n"
        f" Total cost: ${Total_Cost:,.2f}\n"
    )
    print(Output_To_Screen)
    return Output_To_Screen


def main():
    # Ask user for inputs
    fSquareFtWall = getFloatInput("Enter wall space in square feet: ")
    fPaintPrice = getFloatInput("Enter paint price per gallon: ")
    fFeetPerGallonPaint = getFloatInput("Enter feet per gallon: ")
    fLaborHoursPerGallon = getFloatInput("How many labor hours per gallon: ")
    fPaintLaborPerHour = getFloatInput("Labor charge per hour: ")
    sState_Job = input("What state will this job take place? ")
    sLast_Name = input("What is the customer's last name? ")

    # Get the cost estimate to write to a file
    Cost_Estimate = showCostEstimate(fSquareFtWall, fPaintPrice, fFeetPerGallonPaint,
                                     fLaborHoursPerGallon, fPaintLaborPerHour,
                                     sState_Job, sLast_Name)

    # Writing the cost estimate to a file and concatenating the last name to the filename
    with open(f"{sLast_Name}_PaintJobOutput.txt", "w") as file:
        file.write(Cost_Estimate)
    print(f"File: {sLast_Name}_PaintJobOutput.txt was created")


main()
