# for i in range(3): #column
   # for j in range(4): #Row
    #    print("*", end=" ")
   # print()
"""
------------------------------------------
1. 
* * * * * 
* * * * 
* * * 
* * 
* 

n = 5

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
----------------------------------------
2.
* 
* * 
* * *
* * * * 
* * * * * 
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()

--------------------------------------------
3. 
    *
   ***
  *****
 *******
*********
    
for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end = "")

    for k in range(2 * i - 1):
        print("*", end="")
    print()
--------------------------------------------------------
4.
n = 5 btw ///////
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end = "")

    for k in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):

    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
    --------------------------------------------
"""
n = 5
for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end = "")

    for k in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):

    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()