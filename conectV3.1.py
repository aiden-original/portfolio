dictionary={
    1: ["c1","","c2","","c3","","c4","","c5","","c6","","c7",""],
    2: ["c1","","c2","","c3","","c4","","c5","","c6","","c7",""],
    3: ["c1","","c2","","c3","","c4","","c5","","c6","","c7",""],
    4: ["c1","","c2","","c3","","c4","","c5","","c6","","c7",""],
    5: ["c1","","c2","","c3","","c4","","c5","","c6","","c7",""],
    6: ["c1","","c2","","c3","","c4","","c5","","c6","","c7",""],
}

import time
winner="none"
rw=""
for g in range(int(len(dictionary[1])/2)):
    rw = rw+  (f"{str(g+1).center(4)}")

def display():
   
    print(" "+rw)
    
    
    for i in dictionary:
        array=(dictionary.get(i))
    
        counter = 1
        print("+---"*(int(len(array)/2))+"+")
        
        
        output=""
        for i in range(int(len(array)/2)):
            output=output+(f"|{(array[counter]).center(3)}");
            counter+=2
        print(output+"|")
    print("+---"*(int(len(array)/2))+"+")
    
#function drop
def drop(x,y):
    currentR=0
    for i in range(len(dictionary)):
        if (dictionary[i+1])[(2*x)-1] =="" :
            currentR=i
        else:
            dictionary[currentR+1][2*x-1] = str(y)
        if i == len(dictionary)-1:
            dictionary[currentR+1][2*x-1] = str(y)
        
#------------------------------------------------------------------------#------------------------------------------------------------------------
#------------------------------------------------------------------------
def function_win_up(row,column,x,player):
    #only if row is from 6 to 4
    global winner
    counting=0
    if row >= 4 and row <= 6:
        for l in range(4):
            if (dictionary[row-l])[(2*column)-1] == str(x):
                counting+=1 
        if counting == 4:
            print ("winner")
            winner = player
#------------------------------------------------------------------------
def function_win_right(row,column,x,player):
    #change logic for left
    global winner
    counting=0
    if column >= 1 and column <= 4:
        for l in range(4):
            if (dictionary[row])[(2*(column+l))-1] == str(x):
                counting+=1 
        if counting == 4:
            print ("winner") 
            winner = player
#------------------------------------------------------------------------
def function_win_right_dia(row,column,x,player):
    #change logic for left
    global winner
    counting=0
    if (row >= 4 and row <= 6) and (column >= 1 and column <= 4):
        for l in range(4):
            if (dictionary[row-l])[(2*(column+l))-1] == str(x):
                counting+=1 
        if counting == 4:
            print ("winner")  
            winner = player
#------------------------------------------------------------------------
def function_win_left_dia(row,column,x,player):
    #change logic for left
    global winner
    counting=0
    if (row >= 4 and row <= 6) and (column >=  4 and column <= 7):
        for l in range(4):
            if (dictionary[row-l])[(2*(column-l))-1] == str(x):
                counting+=1 
        if counting == 4:
            print ("winner")  
            winner = player






def function_win(p,l):
    for k in range(7):
        for u in range(6):#
            function_win_up(u+1,k+1,p,l)
            function_win_right(u+1,k+1,p,l)
            function_win_right_dia(u+1,k+1,p,l)
            function_win_left_dia(u+1,k+1,p,l)
            if winner != "none":
                print(f"player:{l}, you have won")
                quit()

print("this is a game of connect 4 ")

P1 =input("player1 please enter your name ")
P2 =input("player2 please enter your name ")
#----------------------------------------------------------------------------------------------
end = "yes"  
while end != "no":
    times = int(input("please enter the time in seconds for thinking in seconds") )
    if str(type(times)) == "<class 'int'>":
        print("pass")
        end = "no"
display()
#-----------------------------------------------------------------------------------------------
while winner =="none":
    
    time.sleep(times)
    valid ="no"
    P1input =int(input(f"{P1} please pick a column to drop a counter(only the number)"))
    while valid=="no":
        if P1input>=1 and P1input<= int(len(dictionary[1])/2):
            valid="yes"
        else:
            print("please enter a number in range")
            P1input =int(input(f"{P1} please pick a column to drop a counter(only the number)"))
    drop(P1input,"X")
    display()
    function_win("X",P1)
    
    
    
    
    
    
    
    time.sleep(times)
    valid ="no"
    P2input =int(input(f"{P2} please pick a column to drop a counter(only the number)"))
    while valid=="no":
        if P2input>=1 and P2input<= int(len(dictionary[1])/2):
            valid="yes"
        else:
            print("please enter a number in range")
            P2input =int(input(f"{P2} please pick a column to drop a counter(only the number)"))
    drop(P2input,"0")
    display()
    function_win("0",P2)