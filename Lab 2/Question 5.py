# This code calculates z using the equation z = (x + y)*(x + y) - 2*x*y

x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

z = (x + y) * (x + y) - 2 * x * y

print(f"The value of z is: {z}")
