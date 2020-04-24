


green = ('\033[32m' + u'\u25c9' + '\033[0m') 
red = ('\033[31m' + u'\u25c9' + '\033[0m')
blue =('\033[34m' + u'\u25c9' + '\033[0m')


while True: 
    try:
        x = int(input("Enter the size of the playing area (2-9): "))
        if 10 > x > 1:
            break                
    except : 
        print ("Enter number !")
    else : 
        print ("The number must be between 2 and 9! ")

def stone_rotation (z):
    if  main_list[z] == green:                          
        main_list[z] = red
    else:                                       
        if  main_list[z] == red:
            main_list[z] = blue
        else:
            main_list[z] = green

main_list= [green] * x*x


import random

for g in range (3*x):
    rand_line = random.randrange(0, x)
    for ra_l in range (x):
        stone_rotation (rand_line*x-x+ra_l)  

for g in range (random.randrange(0, 3)):
    for ra_u in range (x):
        stone_rotation (ra_u*x+ra_u)

for g in range (3*x):
    rand_column = random.randrange(0, x)
    for ra_s in range (x):
        stone_rotation (rand_column+x*ra_s)

for g in range (random.randrange(0, 3)):
    for ra_u2 in range (x,0,-1):
        stone_rotation (ra_u2*x-ra_u2)
 
    

#items = (green, red, blue)                     
#import random
#for ra in range (x*x):                                                          ### wrong ###  code without possible solution 
#    main_list = main_list1.append(random.sample(items, 1))                      #list of all random items in field    
#main_list = [ item for elem in main_list1 for item in elem]                     # make list flat



import string
abc=list(string.ascii_lowercase)         # list of alphabet characters 

def my_function ():                             
     for i in range (x):
          if i == 0:
               print ("*",end = "")                     
               for k in range (x):
                   print (" ",abc[k],end = "")       # print alphabet characters in first line 
               print()

          for j in range (x):
               if j == 0:
                   print (i+1," ",end = "")               # print numbers in first column
               print (main_list[i*x+j]," ",end = "")       # print all items from current list off all items     
          print ()
     print ("-",end ="")
     print ()

def check ():
    ok = 0
    for ch in range (x*x-1):
        if main_list[ch] != main_list[ch+1]:
            ok = 1
    if ok ==0:
        print ("Victory !!!")
        raise SystemExit
    if m == "exit":
        print ("Game over")
        raise SystemExit

m=0
while   x > 1:

    my_function()
    check()
    
    m = input("Enter a row, column or diagonal for stone rotations. If you want to exit game enter 'exit': ")


    while True:
        print("\033c")                                  # clear window 
       
        try:            
            m = int(m)
            if x+1 > m > 0:
                for t in range (x):                             
                    stone_rotation (m*x-x+t)                     # stone rotations in a line  
                break
            else :
                print ("Number has to be in range of field !  ")  
                break        
            
        except:
            if m == "*":
                for v in range (x):                             
                    stone_rotation (v*x+v)                        # stone rotations in a diagonal (from top to the bottom)                    
                break
            if m == "-":
                for r in range (x,0,-1):                    
                    stone_rotation (r*x-r)                             # stone rotations in a diagonal (from bottom to the top)                     
                break

            try: 
                    m = int (abc.index(m))                                       
                    if  abc[x] > abc[m] >= abc[0]:
                        n = m
                        for s in range (x): 
                            stone_rotation (n+x*s)                        # stone rotations in a column                             
                        break
                    else:
                        print ("Letter has to be in range of field ! ")
                    break           
    
            except: 
                    print ("Number or letter has to be in range of field ! ") 
                    break

        
          



