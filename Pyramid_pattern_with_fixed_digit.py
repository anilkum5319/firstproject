#!/usr/bin/python
n=int(input('Enter The N Value:'))
for i in range(n):#0,1,2,3,4
    print((' '*(n-i-1))+ (str(i+1)+' ')*(i+1))

