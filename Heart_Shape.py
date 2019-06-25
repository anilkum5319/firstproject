#!/usr/bin/python
for row in range(6):
    for col in range(7):
            if  (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
                #print("*",end="")
            #else:
               #print(end=" ")
    #print()


## If we want to run this same in Python2 
                print "*",
            else:
                print " ",
    print

print (" This is loukySri Heart");'\n'


