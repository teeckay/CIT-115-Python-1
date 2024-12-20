
# Get the name of the person whose tests are to be averaged and graded.
sTesters_Name = input("Name of the person that we are calculating the grades for: ")
# 1 Get the 4 Test Scores:
iTest_1 = int(input("Test 1: "))
iTest_2 = int(input("Test 2: "))
iTest_3 = int(input("Test 3: "))
iTest_4 = int(input("Test 4: "))
# Code checking the 4 scores are not less than zero
if iTest_1 < 0 or iTest_2 < 0 or iTest_3 < 0 or iTest_4 < 0:
    print("Test scores must be greater than 0")
    raise SystemExit

# Prompt the user whether to drop the lowest grade or not.
sDrop_Lowest_Score = input("Do you wish to drop the Lowest Grade Y or N?: ").upper()
#Code checking the user uses Y or N to drop the lowest score ,then
# Calculate the averages and  what the lowest score is if one is to be dropped
# OUTPUT AS A FLOAT
if sDrop_Lowest_Score == "Y":
    if iTest_1 <= iTest_2 and iTest_1 <= iTest_3 and iTest_1 <= iTest_4:
        iLowest_Score = iTest_1
    elif iTest_2 <= iTest_3 and iTest_2 <= iTest_4:
        iLowest_Score = iTest_2
    elif iTest_3 <= iTest_4:
        iLowest_Score = iTest_3
    else:
        iLowest_Score = iTest_4

    fAverage_Tests = (iTest_1 + iTest_2 + iTest_3 + iTest_4 - iLowest_Score) / 3

elif sDrop_Lowest_Score == "N":
    fAverage_Tests = (iTest_1 + iTest_2 + iTest_3 + iTest_4) / 4
else:
    print("Enter Y or N to Drop the Lowest Grade.")
    raise SystemExit

# Code to determine the test's average letter grade value

if fAverage_Tests >= 97.0:
    sLetter_Grade = "A+"
elif fAverage_Tests >= 94.0:
    sLetter_Grade = "A"
elif fAverage_Tests >= 90.0:
    sLetter_Grade = "A-"
elif fAverage_Tests >= 87.0:
    sLetter_Grade = "B+"
elif fAverage_Tests >= 84.0:
    sLetter_Grade = "B"
elif fAverage_Tests >= 80.0:
    sLetter_Grade = "B-"
elif fAverage_Tests >= 77.0:
    sLetter_Grade = "C+"
elif fAverage_Tests >= 74.0:
    sLetter_Grade = "C"
elif fAverage_Tests >= 70.0:
    sLetter_Grade = "C-"
elif fAverage_Tests >= 67.0:
    sLetter_Grade = "D+"
elif fAverage_Tests >= 64.0:
    sLetter_Grade = "D"
elif fAverage_Tests >= 60.0:
    sLetter_Grade = "D-"
else:
    sLetter_Grade = "F"
# Output the user's name, average and grade
print(f"{ sTesters_Name } test average is : { fAverage_Tests }")
print(f"Letter Grade for the test is : { sLetter_Grade } ")










