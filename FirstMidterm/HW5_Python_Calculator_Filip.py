print("Please select one of the operations:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


def Add(x, y):
    return x + y

def Sub(x, y):
    return x - y

def Mul(x, y):
    return x * y

def Div(x, y):
    return x / y

while True:
    operation = input("Enter your choice(1/2/3/4): ")

    
    if operation in ('1', '2', '3', '4'):

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

        except ValueError:
            print("Invalid input. Please note that only numbers allowed. Try entering a number.")
            continue

        if operation == '1':
            print(num1, "+", num2, "=", Add(num1, num2))

        elif operation == '2':
            print(num1, "-", num2, "=", Sub(num1, num2))

        elif operation == '3':
            print(num1, "*", num2, "=", Mul(num1, num2))

        elif operation == '4':
            try:
                print(num1, "/", num2, "=", Div(num1, num2))
            except:
                print("Sorry but we can't divide with 0")
    
        finishingup = input("Would you like to do a new calculation? (yes/no): ")
        if finishingup == "no":
          break
        if finishingup == "yes":
          continue
        else:
         print("Not a valid input. Enter yes or no.")


      