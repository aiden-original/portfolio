dictionarry = {
    0:["X",1,"X"],
    1:["1","X","X"],
    2:["X",1,"3"],
}


def horizontal(x):
    for i in dictionarry:
        print("---------------------------")
        check = 0
        for l in range(3):
            print(dictionarry.get(i)[l])
            if (dictionarry.get(i)[l]) == x:
                check +=1
            print("check",check)
        if check == 3:
            return "winner"
        

def vertical(x):
    for i in range(3):
        print("---------------------------")
        check = 0
        for l in range(3):
            print(dictionarry.get(l)[i])
            if (dictionarry.get(l)[i]) == x:
                check +=1
            
        print("check",check)
        if check == 3:
            return "winner"

def rightDiagonal(x):
    for i in range(1):
        print("---------------------------")
        check = 0
        for l in range(3):
            print(dictionarry.get(l)[l])
            
            if (dictionarry.get(l)[l]) == x:
                check +=1
        print("check",check)
        if check == 3:
            return "winner"


def leftDiagonal(x):
    for i in range(1):
        print("---------------------------")
        check = 0
        for l in range(3):
            print(dictionarry.get(l)[2-l])
            
            if (dictionarry.get(l)[2-l]) == x:
                check +=1
        print("check",check)
        if check == 3:
            return "winner"
leftDiagonal("X")

def winnerChecker(x,player):
    if (horizontal(x) or vertical(x) or rightDiagonal(x) or leftDiagonal(x)):
        print("heh")
winnerChecker("x","aiden")