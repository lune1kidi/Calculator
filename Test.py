print("Hi, I am Lune's calculator, i will assist you with basic mathematician operations such as ADDITION, SUBTRACTION, MULTIPLICATIONS and DIVISONS.")

while True:
    try:
        choice = int(input("Enter number '1' for ADDITION, number '2' for SUBTRACTION, number '3' for MULTIPLICATION or number '4' for DIVISION: "))
        if choice == 1:
            print("Your choice is '1' which is ADDITION.")
            break
        elif choice == 2:
            print("Your choice is '2' which is SUBTRACTION.")
        elif choice == 3: 
            print("Your choice is '3' which is MULTIPLICATION.")
        elif choice == 4:
            print("Your choice is '4' which is DIVISON.")
        else:
            print("Your syntax is wrong, enter '1' for ADDITION, '2' for SUBTRACTION, '3' for MULTIPLICATION or '4' for DIVISION: ")
    except ValueError:
        print("Your input should be numbers from 1 to 4, not letters. ")

x = int(input("Enter your 'X' Number: "))
y = int(input("Enter your 'Y' Number: "))

def addition(x, y):
    result = x + y
    print(f"Your result is: {result}")
def subtraction(x, y):
    result = x - y
    print(f"Your result is: {result}")
def multiplication(x, y):
    result = x * y
    print(f"Your result is: {result}")
def division(x, y):
    result = x / y
    print(f"Your result is: {result}")
    
if choice == 1:
    addition(x, y)
if choice == 2:
    subtraction(x, y)
if choice == 3:
    multiplication(x, y)
if choice == 4:
    division(x, y)

    while True:
        again = input("Do you want to use Lune's calculator again? If you want type 'Yes' or if you don't want type 'No': ")
    
        if again == "Yes":
            print("Its my pleasure!")
            break
        elif again == "No":
            print("Goodbye!")
            exit()
        else:
            print("Your syntax is wrong: Enter 'Yes' or 'No': ")