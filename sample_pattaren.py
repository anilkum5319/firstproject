# Write a Python program to construct the following pattern for Pictorial, using a nested for loop.


#x=5;
#for i in range(x):
    #for j in range(i):
        #print('*',end=" ")
    #print()
#for i in range(x,0,-1):
    #for j in range(i):

        #print('*',end=" ")
    #print()

#* 
#* * 
#* * * 
#* * * * 
#* * * * * 
#* * * * 
#* * * 
#* * 
#*


##### Write a program to display the follwing trangle.......  CTS Interview QAS

#a=int(input("Enter The Value:"))  #a+6

#for i in range(a):
    #print(" "*(a+i))
    #for j in range(i):
        #print(i-j,end=" ")
    
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1 
# 6 5 4 3 2 1

######## To Get Below Pattren

#a=int(input("Enter The Value:"))  #a+6

#for i in range(a):
    #print(" "*(a+i+1))
    #for j in range(i):
        #print(j-i,end=" ")
    #print()
         
#-1     
#-2 -1         
#-3 -2 -1           
#-4 -3 -2 -1             
#-5 -4 -3 -2 -1              
#-6 -5 -4 -3 -2 -1                
#-7 -6 -5 -4 -3 -2 -1


######## To Get Below Pattren

#a=int(input("Enter The Value:"))  #a+6

#for i in range(a):
    #print(" "*(a+i))
    #for j in range(i):
        #print(i-a,end=" ")
         
#-7           
#-6 -6            
#-5 -5 -5             
#-4 -4 -4 -4              
#-3 -3 -3 -3 -3               
#-2 -2 -2 -2 -2 -2                
#-1 -1 -1 -1 -1 -1 -1 


###### To Get Below Pattern

#a=int(input("Enter The Value:"))  #a+6

#for i in range(a):
    #print(" "*(a-i-1),end=" ")
    #for j in range(0,i+1):
        #print(j+1,end="")
    #print()


#      1
#     12
#    123
#   1234
#  12345
# 123456


########## To Get Below Pattern

#a=int(input("Enter The Value:"))  #a+6

#for i in range(a):
    #for j in range(0,i+1):
        #print(j+1,end=" ")
    #print()

#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5 
#1 2 3 4 5 6 
#1 2 3 4 5 6 7 
#1 2 3 4 5 6 7 8

######## Reverse Pattern

#a=int(input("Enter The Value:"))  #a+6

#for i in range(a,0,-1):
    #print(" "*(a-i-1),end=" ")
    #for j in range(0,i+1):
        #print(j+1,end="")
    #print()

#123456789
#12345678
#1234567
#123456
#12345
#1234
#123
#12


# To get below pattern

#a=int(input("Enter The Value:"))  #a+6

#for i in range(a):
    #print(" "*(a-i+1),end=" ")
    #for j in range(i+1):
        #print(j+1,end=" ")
    #print()

#        1 
#       1 2 
#      1 2 3 
#     1 2 3 4 
#    1 2 3 4 5 
#   1 2 3 4 5 6 
#  1 2 3 4 5 6 7

  
# <<<< To get below pattern >>>>>

#a=int(input("Enter The Value:"))  #a+6

#for i in range(a):
    #print(" "*(a+1),end=" ")
    #for j in range(0,i+1):
        #print(j+1,end="")
   #print()

#       1
#       12
#       123
#       1234
#       12345


#a=int(input("Enter The Value:"))  #a+6

#for i in range(a):
    #print(" "*(a-1-i),end=" ")
    #for j in range(i,0,-1):
        #print(j+1,end="")
    #print()

#       2
#      32
#     432
#    5432
#   65432
#  765432
# 8765432

## ++++ To print below pattern ++++++=

#x = 1
#for i in range(0, 5):
    #for j in range(5, i, -1):
        #print(x, end=" ")
        #x = x + 1
    #print()
    #x = 1

#1 2 3 4 5 
#1 2 3 4 
#1 2 3 
#1 2 
#1

####################  To Print Piramid Shape or triangle shape ############

#x=int(input("Enter The Number Of Rows:"))

#for i in range(1,x):
    #for j in range(1,x-i-1):
             #print(end=" ")
    #for j in range(1,i+1):
          #print("*",end=" ")
    #print()

########## Using for loop ###########

#def pyramid(rows):
        #for i in range(rows):
            #print(' ' *(rows-i-1)+'*'*(2*i+1))
   #pyramid(5)
#print(pyramid(x))

#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
# *************
#***************

####################  To Print Piramid Reverse Shape or Reverse triangle shape ############

#for i in range(x,0,-1):
    #for j in range(0,x-i):
             #print(end=" ")
    #for j in range(0,i):
          #print("*",end=" ")
    #print()
    
# * * * * * * * * 
#  * * * * * * * 
#   * * * * * * 
#    * * * * * 
#     * * * * 
#      * * * 
#       * * 
#        *


#############  To Print Right Triangle Shape ###################

#for i in range(1,x+1):
    #for j in range(1,i+1):
        #print("*", end=" ")
    #print()

#* 
#* * 
#* * * 
#* * * * 
#* * * * * 
#* * * * * * 
#* * * * * * * 
#* * * * * * * *  

#############  To Print Reverse Right Triangle Shape ############

#for i in range(x,0,-1):
    #for j in range(i):
        #print("*",end=" ")
    #print()

# * * * * * * * * 
# * * * * * * * 
# * * * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

############# To Print Diamond Shape ############

#x=int(input("Enter The Number Of Rows:"))
#for i in range(1,x):
    #for j in range(1,x-i+1):
        #print(end=" ")
    #for j in range(1,i+1):
        #print("*",end=" ")
    #print()
#for i in range(x,0,-1):
    #for j in range(0,x-i):
          #print(end=" ")
    #for j in range(0,i):
          #print("*",end=" ")
    #print()
    
#         *
#        * *
#       * * *
#      * * * *
#     * * * * *
#    * * * * * *
#   * * * * * * *
#  * * * * * * * *
# * * * * * * * * *
#* * * * * * * * * *
#* * * * * * * * * *
#* * * * * * * * * * 
# * * * * * * * * * 
#  * * * * * * * * 
#   * * * * * * * 
#    * * * * * * 
#     * * * * * 
#      * * * * 
#       * * * 
#        * * 
#         * 



################

########### To print any Alphabet pattaren, we use 7-rows and 5-col ############

########### To Print Squere Shape #########

#for rows in range(7):   # 0-rows to 6-rows
    #for col in range(5): # 0-col to 4-col
        #print("*",end=' ')
    #print()

#* * * * * 
#* * * * * 
#* * * * * 
#* * * * * 
#* * * * * 
#* * * * * 
#* * * * * 

######## To print only Stars on 0-col and 4-col ######

#for rows in range(7):
    #for col in range(5):
        #if (col==0 or col==4):
            #print("*",end=" ")
        #else:
            #print(" ",end=" ")
    #print()

# *       * 
# *       * 
# *       * 
# *       * 
# *       * 
# *       * 
# *       *

########### To Print Below Stars ############

#for rows in range(7):
    #for col in range(5):
        #if (rows==0 or rows==6):
        #if ((col==0 or col==4) or (rows==0 or rows==6)):
            #print("*",end=" ")
        #elif(rows in {1,2,3,4,5}) and (col in {0,4}):  ## This way also can write as per Durga Sir.
            #print("*",end=" ")
        #else: print(" ", end=" ")   # This indicates Empty space 
    #print()
        

# * * * * * 
# *       * 
# *       * 
# *       * 
# *       * 
# *       * 
# * * * * *

########### To Print Below Stars ############

for rows in range(7):
    for col in range(5):
        if ((rows==0 or rows==3 or rows==6) or (col==0 or col==4)):
          print("+",end=" ")
        else: print(" ", end=" ")   # This indicates Empty space 
    print()


# * * * * * 
# *       * 
# *       * 
# * * * * * ----- For this row, you have to add rows==3 --> (rows==0 or rows==3 or rows==6)
# *       * 
# *       * 
# * * * * *


########### To Print Below Stars ############

#for rows in range(7):
    #for col in range(5):
        #if ((rows==0 or rows==3 or rows==6) or (col==0 or col==2 or col==4)): # added col==2 to get middle col line.
          #print("+",end=" ")
        #else: print(" ", end=" ")   # This indicates Empty space 
    #print()


# + + + + + 
# +   +   + 
# +   +   + 
# + + + + + 
# +   +   + 
# +   +   + 
# + + + + +

#####################  To Print ''''' A ''''' Shape ###############

#for rows in range(7):
    #for col in range(5):
        #if ((col==0 or col==4) and rows!=0) or ((rows==0 or rows==4) and (col>0 and col<4)):
           #print("*",end="")
        #else:
            #print(end=" ")
    #print()

#  ***  
# *   * 
# *   * 
# ***** 
# *   * 
# *   * 
# *   * 


################ To Print ''''' E ''''' Shape ###############





################ To Print ''''' F ''''' Shape ###############

#for rows in range(8):
    #for col in range(4):
        #if ((col==0 or col==4)) or ((rows==0 or rows==4) and (col>0 and col<4)):
           #print("*",end="")
        #else:
            #print(end=" ")
    #print()

#*****
#*   
#*   
#*   
#*****
#*   
#*   
#*
#*


#!/usr/bin/python3
# prettytable import PrettyTable
    
#x = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])

#x.add_row(["Adelaide",1295, 1158259, 600.5])
#x.add_row(["Brisbane",5905, 1857594, 1146.4])
#x.add_row(["Darwin", 112, 120900, 1714.7])
#x.add_row(["Hobart", 1357, 205556, 619.5])
#x.add_row(["Sydney", 2058, 4336374, 1214.8])
#x.add_row(["Melbourne", 1566, 3806092, 646.9])
#x.add_row(["Perth", 5386, 1554769, 869.4])

#print(x.get_string(title="Australian cities"))

#./table_title.py 
#+-------------------------------------------------+
#|                Australian cities                |
#+-----------+------+------------+-----------------+
#| City name | Area | Population | Annual Rainfall |
#+-----------+------+------------+-----------------+
#|  Adelaide | 1295 |  1158259   |      600.5      |
#|  Brisbane | 5905 |  1857594   |      1146.4     |
#|   Darwin  | 112  |   120900   |      1714.7     |
#|   Hobart  | 1357 |   205556   |      619.5      |
#|   Sydney  | 2058 |  4336374   |      1214.8     |
#| Melbourne | 1566 |  3806092   |      646.9      |
#|   Perth   | 5386 |  1554769   |      869.4      |
#+-----------+------+------------+-----------------+









