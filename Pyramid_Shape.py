#!/usr/bin/python
n=int(input('Enter The N Rows:'))
#for i in range(0,n):
  #for j in range(0,n-i-1):
   #print(end=" ")
  #for j in range(0,2*2*i+1):
   #print("*",end="")
  #print()

########## Using for loop ###########

def pyramid(rows):
        for i in range(rows):
                   print(''*(rows-i-1)+'*'*(2*i+1))
   #pyramid(5)
