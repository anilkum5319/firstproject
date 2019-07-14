#!/usr/bin/python

########## Right Triangle Shape ##########

x=int(input("Enter The Number Of Rows:"))

#for y in range(1,x+1):        #########  Here x is Number of Rows , 0+1 = 1 in range ( 1,1) means 1 start
    #for z in range(1,y+1):   ########## here z is number of starts indicates also can write range(y)
         #print("*",end=" ")
    #print()

######### SQUARE Pattaren Shape #######

#for y in range(x):
    #print('*'*x)   ## ----- Print star n number of times, if we give 2 start it wil print 2 stars ----

#for y in range(x):   #### --- Represents number of rows
    #for z in range(x): #### --- represents number of stars
        #print('*',end=" ") ##### --- end with empty line and print star
    #print() #### represents with new line every time 


########### ^ Shape ##########

#for i in range(1,x+1):
    #print(" "*(x-i),end=" ")
    #for j in range(i,i+1):
        #print(chr(64+i),end=" ")
        #if i>=2:
           #print(" "*(2*i-4),end=" ")
           #for k in range(i,i+1):
              #print(chr(64+i),end=" ")
    #print()


#####################   XX-MAS TREE SHAPE ############

for a in range(1,x+1,2):
    for i in range(1,x+1):
        print(" "*(2*x-i-a),end=" ")
        for j in range(1,i+a):
           print("*",end=" ")
        print()
for b in range(1,x+1):
    print(" "*(x-4),end=" " )
    print("+"*4)































