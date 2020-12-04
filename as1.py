num1 = raw_input("PLease enter No1: ")
num2 = raw_input("Please enter No2: ")
print("\n")

print("Please specify your operation")
print("Enter 1 for Addition")
print("Enter 2 for Subtraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")
operation = raw_input()

print("\n")

if (operation == "1"):
    print("The result is " + str(int(num1) + int(num2)))

elif (operation == "2"):
    print("The result is " + str(int(num1) - int(num2)))

elif (operation == "3"):
    print("The result is " + str(int(num1) * int(num2)))

elif (operation == "4"):
    print("The result is " + str(int(num1) / int(num2)))


else:
    print("Invalid Operation Entered")

print("Thank you for using our program!!!")
