print("SIM Calculator : Perform basic arithmetic operations here\n")

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        return "Divison by 0 is not possible."
    return x/y


while True:
    first_num = float(input("Enter First Number : "))
    second_num = float(input("Enter Second Number : "))

    print("Operation you want to perform :- Addition(+) , Subtraction(-) , Multiplication(*) , Divison(/) ")
    operation= input("Choose (e.g. for Addition(+), type-> addition):- ")
    operation.lower()

    if operation == "addition":
        print(f"{first_num} + {second_num} =", add(first_num,second_num))
    elif operation == "subtraction":
        print(f"{first_num} - {second_num} =", subtract(first_num,second_num))
    elif operation == "multiplication":
        print(f"{first_num} * {second_num} =", multiply(first_num,second_num))
    elif operation == "divison":
        print(f"{first_num} / {second_num} = ",divide(first_num,second_num))
    else:
        print("Invalid input!")

    nxt_calculation = input("\nDo you want to perform another calculation? (yes/no): ")  
    if nxt_calculation.lower() != "yes":
        print("Thanks for using SIM Calculator")
        break
         
