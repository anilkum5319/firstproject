#!/usr/bin/python3.6

x = eval(input("Enter the Number:"))
 
for i in range(2,x):          ## Here, we took range from start 2 , bcoz we have 0 and 1 by its own divided and multiplied
   if x % i == 0:
       print("Given Number Is Not Prime Number!")
       break
else:
   print("Given Number Is Prime Number!")
