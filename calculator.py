#calculator program

#this function add two numbers
def add(x, y):
    return x + y

#this function subtracts two numbers
def subtract(x, y):
    return x - y

#this function multiplies two numbers
def multiply(x, y):
    return x * y

#this function divides two numbers
def divide(x, y):
    return x / y

print("select operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
    #input from the users
    choice = input("Enter choice(1/2/3/4): ")

    #check if choice is one of the four option
    if choice in('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            
        #next calculation
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

        else:
            print("Invalid Input")



