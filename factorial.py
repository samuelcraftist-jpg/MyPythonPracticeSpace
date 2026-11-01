
print("----------------------")
print("Factorial calculations")
print("----------------------")

#Factorial funtion built from scratch (recursion)
def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)

try:
    inpu = int(input("Enter the input to get factorial of that number: "))
    if inpu == 0:
        print("The factorial of 0 is 1.")
    elif inpu < 1:
        print("Nah bro, im ain't doing that math. Are u dumb enough to calculate negative factorial ")

    else:
        print("The factorial of", inpu, "is", fact(inpu))
except ValueError:
    print("Hell nah, just enter integer value bro, it starts from 0(like 1, 2, 3...n). Btw this is value error")
