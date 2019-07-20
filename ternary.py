####### Terentory Operators ######
### 3 condistions will be on aplying, since its terentory Operator ### 

#x=int(input("Enter first value:"))
#y=int(input("Enter Second value:"))
#z=int(input("Enter Third value:"))
#max = x if x>y or y>z and x>z else y if y>z else z
#print("Max Value:",max)
#print ("Both values are Equeal:" if x==y else "First value is Grater then Second Value:" if x>y else "First Value is Smaler then Second Value:")
###########Special  opereater ######

# Identitey Operator ######
# 1. is , is not   ----------- is = always identify the Address ; == operator looks for the Content value ####
#list1=[10,20,30,40]
#list2=[10,20,30,40]
#print(id(list1))
#print(id(list2))
#print(list1 is list2)
#print(list1 == list2)

#x=200
#y=300
#print (id(x))
#print (id(y))
#print (x is y)
#print (x is not y)
#print (x == y)


###### Membership Operator ##

###### in; not in are the membership Operaters , is used to test whether value/varible is found in a squence #######

#x=[10,20,30,40,50]
#print ( 30 in x)
#print ( 20 not in x)
#print (" " in x) #### =======> Out is False,bcoz, there is no space in x-list values. 
#print (' ' not in x)

######### Modules #######

## Modules is nothing but a set of Functions and varibles and values and sets ###
### main module is used by import ####

#import math as k # ======  renaming the function using alliasing !! math is satanded library
#print (k.sqrt(100))
#print (k.pi)

#import os
#x= os.getcwd()
#print ( x )
#print (os.system)

### write a program for Area of Circle --- which is ||(pi)r2 Value

#from math import *
#r=int(input("Enter Radius Value:"))
#area= pi*r**2
#print ( " The Area of the Circle : ", area )

##### Input and Output Statement ###

#Python-2##
#raw_input()  #----- Typecasting is must, Always treated as string value 
#input()      # ----- No typeCasting 

#Python-3##
#input()      #----- Typecasting is must, No more raw_input in python3, raw_input treated as input in python3.

#print ("The Sum:",int(input("Enter The First Value:"))+int(input("Enter The Second Value:")))  # ------ This is Short form #

#x=input("Enter the 1st Value:")
#y=input("Enter the 2nd Value:")
#x1=int(x)    # -------  Defining int value separatly 
#y1=int(y)    # -------  Defining int value separatly 
#print ("The Total Sum :", x1+y1, '\n' "The Total Suprestion:", x1-y1)

##### 2--Floating values getting from keyboard ##

#x,y = [float(a)for a in input("Enter The 2 Float Values :").split(';')]  ## Here, default sepration concider as emtey space,also you can define separation, which you like ...: , . etc
#print ("The float Sum :", x+y)



##### 4--intiger values getting from keyboard ##

#a,b,c,d =  [int(x)for x in input("Enter 4-Int Values:").split(',')]    
#print ("The Int Sum :", a+b+c+d)  # Float values are not alowed here.

# eval(): --- Evaluates and executes an expressions

#x=eval(input("Enter Some Date:"))
#print(type(x))
#print (x)
#for x1 in x:
    #print(x1)


######## *** Command Line Arguments  *** #####

#from sys import argv
#print ("The Number Of Command Line Arguments:",len(argv))
#print ("The List Of Command Line Arguments:",argv)
#print ("Command Line Arguments One by One:")
#for x in argv:
       #print(argv)

#print ("Slice Operator Results :", argv[1:4])


################################################## Flow Controls #####################

#Flow control divide in to 3-statements
#1. Conditional statement

#if and ifelse statements

#### IF -- Else ###

#x=input("Enter Any Name:")
#if x == "Loukya":
#if x:                                   # ----------- This will satisfied if you give any value !!
    #print("Hello Anil, Good Morning")
    #print ("If Condistion Satesfied")
#else:
    #print("If-Else Condistion Not Satisfied")

#print ("If Condistion Satesfied")

######## IF ; ELIF ; ELSE Statements Example ############

#B=input("Enter Your Brand Shirt:")
#if B == "Arrow":
    #print ("My Favirate Shirt is Arrow Brand Shirt ")
#elif B == "Roadstar":
    #print ("Roadstar Brand Shirt Is My Luck Shirt")
#elif B == "RedTape":
    #print ("Redtape Brand Shirts Are for Sweathers")
#elif B == "BIBA":
    #print ("BIBA Brand Offer is Buy One Get One")
#else:
    #print ("Other Brands Are Not Good To Ware !!")


#2. iterative/loops Statements  --- This will be used for, whne we need a code to be run repeatedly, then will go for iterative statments
######### we have two loops in iterative statements , they are for-loop and while-loop

# Example : for loop
#a=input("Enter The string Value:")
#for i in a:
    #print("Good Morning",a)
######################################

#for x in range(1,50):
    #if x%2!=0:
        #print("This is ODD Numbers:",x)
    #else:
        #print("This is Even Numbers:",x)

#while True:  
    #print("Hello Anil, Good Morning")    ##### This one also called infinite loop 

#x=0
#while x<=100:
    #print(x)
    #x+=1


#3. Tranfer Statements ----- Loops and Control statements ( Continue, Pass & Break) to handle looping requremnts
      ##we have 3 - Tranfer statements i.e 1. continue ((This will used for skiping current itteration and continue next itterastion)) 2. break ( To beak the itterastion/any loop, if we use break statment, loop will be stop there it self >> 3. pass { just to pass the statement}
## Break Example ##

#x=[10,20,30,40,500,50,600,60]
#for i in x:
    #if i>400:
        #print("Sorry We can Not Process This Order, As You Dont Have Insurence:")
        #break
    #print("The Items Value Is:",i,"Rupees")

### Continue Example ###

#for i in x:
    #if i>400:
        #print("Sorry We can Not Process This Order, As You Dont Have Insurence:")
        #continue
    #print("The Items Value Is:",i,"Rupees")
    

####### Nested Loops:  it is a loop that occurs with in the another loop

for i in range(5):
    for j in range(5):    #  here inside one for loop , we have difine another for loop is called nested !!
        print("i={} and j={}".format(i,j))

