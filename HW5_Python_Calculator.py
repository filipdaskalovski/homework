print("Please select one of the operations:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


def add(x, y):
    return x + y

def Subtract(x, y):
    return x - y

def Multiply(x, y):
    return x * y

def Divide(x, y):
    return x / y

while True:
    operation = input("Enter choice(1/2/3/4): ")

    
    if operation in ('1', '2', '3', '4'):

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        except ValueError:
            print("Invalid input. Please note that only numbers allowed. Try entering a number.")
            continue

        if operation == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif operation == '2':
            print(num1, "-", num2, "=", Subtract(num1, num2))

        elif operation == '3':
            print(num1, "*", num2, "=", Multiply(num1, num2))

        elif operation == '4':
            #print(num1, "/", num2, "=", Divide(num1, num2))
            try:
                print(num1, "/", num2, "=", Divide(num1, num2))
            except:
                print("Sorry but we can't divide with 0")
    
        finishingup = input("Would you like to do a new calculation? (yes/no): ")
        if finishingup == "no":
          break
        else:
         print("Not a valid input. Enter yes or no.")


      