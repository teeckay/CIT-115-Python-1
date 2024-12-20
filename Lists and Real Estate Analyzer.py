
def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Input a number that is greater than 0.")
            else:
                return value
        except ValueError:
            print("Input must be a numeric value greater than 0.")


def getMedian(Sales_Values):
    # Sort the Sales Values list using list.sort() to have it in ascending order
    Sales_Values.sort()
    # Count how many entries for sales were entered to calculate the Median
    Number_Of_Sales_Values = len(Sales_Values)


    # If the number of sales entries is odd, the median is the middle list value
    if Number_Of_Sales_Values % 2 == 1:
        fMedian = Sales_Values[Number_Of_Sales_Values // 2]
    # If the number of entries is even, calculate the 2 middle list values and average those values
    else:
        Middle_Value = Number_Of_Sales_Values // 2
        fMedian = (Sales_Values[Middle_Value - 1] + Sales_Values[Middle_Value]) / 2

    # Return the calculated median as a float
    return fMedian

def main():
    #Interest rate constant
    COMMISSION_RATE = 0.03
    # Variable to accumulate sales values.
    Sales_Values_List = []
    #Variable to count number of entered sales values from the list
    Number_Of_Sales_Values = len(Sales_Values_List)

    #Loop appending entered sales values and exiting the loop when N is entered
    while True:
        fSales_Value_Input = getFloatInput("Enter property sales value: ")
        Sales_Values_List.append(fSales_Value_Input)
        sAnother_Input = input("Enter another value Y or N: ").upper()
        if sAnother_Input == 'N':
            break
    # Sorting the accumulated list from smallest to largest to aid in calculations
    Sales_Values_List.sort()

    # Loop Outputting each entry in the sorted list formatted as currency with 2 decimal positions
    iCount = 1
    for fValue in Sales_Values_List:
        print(f"Property {iCount}: ${fValue:<10,.2f}")
        iCount += 1

    # Determine and print the minimum sales value formatted as currency with 2 decimals
    fMin_Sales_Value = Sales_Values_List[0]
    print(f"{"Minimum:":11s}{"$":2s}{fMin_Sales_Value:,.2f}")

    # Determine and print the maximum value formatted as currency with 2 decimals
    fMax_Sales_Value = Sales_Values_List[-1]
    print(f"{"Maximum:":11s}{"$":2s}{fMax_Sales_Value:,.2f}")

    # Calculate and print the total value formatted as currency with 2 decimals
    fTotal_Sales_Value = sum(Sales_Values_List)
    print(f"{"Total:":11s}{"$":2s}{fTotal_Sales_Value:,.2f}")

    # Calculate and print the average value formatted as currency with 2 decimals
    fAverage_Sales_Value = fTotal_Sales_Value / len(Sales_Values_List)
    print(f"{"Average:":11s}{"$":2s}{fAverage_Sales_Value:,.2f}")

    # Calculate and print the median value as currency with 2 decimals
    fMedian_Sales_Value = getMedian(Sales_Values_List)
    print(f"{"Median:":11s}{"$":2s}{fMedian_Sales_Value:,.2f}")

    # Calculate and print the commission formatted as currency with 2 decimals
    fCommission_Of_Sales_Value = fTotal_Sales_Value * COMMISSION_RATE
    print(f"{"Commission:":10s}{"$":2s}{fCommission_Of_Sales_Value:,.2f}")


# Call the main function to start the program
main()
