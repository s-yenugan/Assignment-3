def factorial(n):
    if n < 2:
        return 1
    else:
        return n * (factorial(n-1))
number = int(input("Enter a Number: "))
result = factorial(number)
print ("Factorial of", number, "is: ", result)
    



import math
a = float(input("Enter a Number: "))

sqr_value = math.sqrt(a)
nat_log = math.log(a)
num_sine = math.sin(a)

print("Square root of", a, "is:", sqr_value)
print("Natural logarithm (ln) of", a, "is:", nat_log)
print("Sine of", a, "radians is:", num_sine)
