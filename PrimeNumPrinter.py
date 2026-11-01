print("-------------------------------------")
print("Prime numbers between 1 to Your limit")
print("-------------------------------------")

lim = int(input("Enter ur limit: "))

for num in range(lim):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


