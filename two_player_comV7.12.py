import random 
import re
import time
import math
P1score = 0
P2score = 0
P1statPoint = 0 
P2statPoint = 0 
P1projectileUP = 0
P2projectileUP = 0

P11buff = "no"
P21buff = "no"

P12buff = "no"
P22buff = "no"

P13buff = "no"
P23buff = "no"

P1knight = 2
P2knight = 2
P1knightUP =0
P2knightUP =0

P1reflect=10
P2reflect=10

P1reflectUP=0
P2reflectUP=0

P1clericUP=0
P2clericUP=0


preset = {
    "druid":("druid",10,60,110,10,30),
    "mage":("mage",10,5,100,65,20),
    "knight":("knight",100,50,0,0,50),
    "hunter" :("hunter",60,50,20,20,50),
    "cleric":("cleric",40,40,40,40,40)
    
}
print("the druid  times 2 the effectiveness of life related skills(lifesteal)" )
print("the mage -4(base, scales with lv) magic related accurace chances" )
print("the knight has times 2 effectiveness of non-magic block and access to reflective dmg(base 10%)" )
print("the hunter convert all projectiles related skills into scalable barrage attack(base 2 projectiles)" )
print("the cleric times 10 the effectiveness of healing skill and buff skill related skill plus access to the buff skill" )
print("loading...")
print("\n"*2)
time.sleep(4)
P1dead="no"
P2dead="no"
Edead="no"

P1druidUP=0 
P2druidUP=0

P1godhood = "no"
P2godhood = "no"
P1onfire ="no"
P2onfire ="no"
Eonfire = "no"

turn = "P1"
P1score = 0
P2score = 0
P1fireT = "first"
P2fireT = "first"
EfireT = "first"

P1block = "no"
P2block = "no"
Eblock = "no"

P1blockStack = 0
P2blockStack = 0
EblockStack = 0

P1blockAmount = 0
P2blockAmount = 0
EblockAmount = 0


P1losses = 0
P2losses = 0


P1lv = 1 
P2lv = 1 
auto = -2
Slot =0

P1exp = 0 
P2exp = 0 

x = 0
elv = 1 
P1fireT = "first"
P2fireT = "first"

complete = "no"


gold = 0 
EnewHP = 1
PnewHP = 1
P1fairTotal = 222
P2fairTotal= 222

Import = input("do you want load a saved run, type(yes/no) ")
if Import == "yes" or Import == "y" or Import == "Yes":
    print("\n")
    fileName = str(input("what's you saves name "))
    fileName = fileName +".txt" 
    file = open(fileName,"r")
    file = file.read()
    file = str(file)
    file = file.split("$")
    userpic = str(input("which username are you going to uses old or new. "))
    
    P1userStat = file[0]
    P2userStat = file[1]

    userStat = str(userStat)
    userStat = userStat.replace("(","")
    userStat = userStat.replace(" ","")
    userStat = userStat.replace("'","")
    userStat = userStat.strip('"')
    userStat = userStat.replace(")","")
    userStat = userStat.strip(" ")
    userStat = userStat.split(",")
    if userpic == "new":
        P1userStat[0] = saveUserName
    time.sleep(2)
    print("\n"*2)
    
    
    
    P1attack = int(P1userStat[1])
    P1defence = int(P1userStat[2])
    P1magic_attack = int(P1userStat[3])
    P1magic_defence = int(P1userStat[4])
    P1HP = int(P1userStat[5])
    P1lv = int(P1userStat[6])
    P1exp = (P1userStat[7])
    
    P1exp = P1exp.replace(")","")
    P1exp = int(P1exp) 
    
    P1godhood = P1userStat[8]
    P1score = P1userStat[9]
    
    ####
    P2attack = int(P2userStat[1])
    P2defence = int(P2userStat[2])
    P2magic_attack = int(P2userStat[3])
    P2magic_defence = int(P2userStat[4])
    P2HP = int(P2userStat[5])
    P2lv = int(P2userStat[6])
    P2exp = (P2userStat[7])
    P2exp = P2exp.replace(")","")
    P2exp = int(P2exp) 
    
    P2godhood = P2userStat[8]
    P2score = P2userStat[9]
    ##
    
    P1boxStats = (P1userName,P1attack,P1defence,P1magic_attack,P1magic_defence,P1HP,P1lv,P1exp)
    P1boxName = ("P1userName","P1attack","P1defence","P1magic_attack","P1magic_defence","P1HP","P1lv","P1exp")
    P2boxStats = (P2userName,P2attack,P2defence,P2magic_attack,P2magic_defence,P2HP,P2lv,P2exp)
    P2boxName = ("P2userName","P2attack","P2defence","P2magic_attack","P2magic_defence","P2HP","P2lv","P2exp")
    P1tem = 0 
    P2tem = 0 
    for i in P1boxStats:
        if len(str(i)) > P1tem:
            P1tem = len(str(i)) 
    for i in P2boxStats:
        if len(str(i)) > P2tem:
            P2tem = len(str(i)) 
    print("these are the players stats;")        
    print(f"+{'-'*(P1tem+20)}+"," "*10,f"+{'-'*(P2tem+20)}+")
    for i in range(len(P1boxStats)):
        P1outbox = str(f"{P1boxName[i]}: {P1boxStats[i]}")
        P2outbox = str(f"{P2boxName[i]}: {P2boxStats[i]}")
        print(f"|{(P1outbox).center(P1tem+20)}|"," "*10,f"|{(P2outbox).center(P2tem+20)}|")
    print(f"+{'-'*(P1tem+20)}+"," "*10,f"+{'-'*(P2tem+20)}+")     
        

    print("\n")
    print("\n")     
    
    
    IMRestart = input("if the stats are correct type yes, if not type no \n")
    if IMRestart == "yes" or IMRestart == "Yes" :
        print("ok great, countinue to play")
    else:
        print("okay the progam will restart, so when you enter the code you have to restart the game from scratch ");
        quit()
    restrictSUM = "YES"
    
else:
    while ((P1fairTotal > 200)) or P2fairTotal> 200:
        informantion= input("do you want a description on the skills ")
        while informantion == "yes" or informantion == "Yes" or informantion == "sure" or informantion == "Sure" or informantion == "yeah" or informantion == "Yeah":
            print("\n")
            print(f"the skills: \n1.lifesteal \n2.slash\n3.eternal flame\n4.heal\n5.block\n6.arrow\n(wait)")
            inType = input("what skill do you want informantion about(type all for all)")
            if inType == "lifesteal" or inType == "Lifesteal" or inType == "one" or inType == "1" or inType == "One":
                print("\n")
                print("lifesteal is a skill that scales off magic power and it takes some health from enemny for onself ,its probably last forever")
                print("\n")
            elif inType == "slash" or inType == "Slash" or inType == "two" or inType == "2" or inType == "Two":
                print("\n")
                print("slash is a phisical attack that scales off attack power and it doesnt have any special effects")
                print("\n")
            elif inType == "eternal flame" or inType == "Eternal flame" or inType == "three" or inType == "3" or inType == "Three":
                print("\n")
                print("eternal flame is a flame that stays on the enemy until 3 turns pass not really eternal if you ask me,\n eternal flame does 3 times damage the very first uses so make good uses of it")
                print("\n")
            elif inType == "heal" or inType == "Heal" or inType == "four" or inType == "4" or inType == "Four":
                print("\n")
                print("heal is a skill that allows you to heal a choosen target by a percentage of their maxp hp,it's locked by cap players can't heal monsters as their mana is too pure")
                print("\n")
            elif inType == "Block" or inType == "block" or inType == "five" or inType == "5" or inType == "Five":
                print("\n")
                print("Block is a skill that does exactly as it's name, it blocks all attacks excluding eternal flame passive fire dmg if it has enought block, maximum of ∞ charges ")
                print("\n")
            elif inType == "arrow" or inType == "Arrow" or inType == "six" or inType == "6" or inType == "Six":
                print("\n")
                print(" arrow is a skill where physical or magic arrows are thrown,  ")
                print("\n")
            else:
                print("\n"*2) 
                print("Lifesteal is a skill that scales off magic power and it takes some health from enemy for oneself ,its probably last forever(until the end of the battle)\n\nSlash is a physical attack that scales off attack power and it doesn't have any special effects\n\nEternal flame is a flame that stays on the enemy until 3 turns pass not really eternal if you ask me,\neternal flame does 3 times damage the very first uses so make good uses of it \n\nHeal is a skill that allows you to heal a choosen target by a percentage of their maxp hp \n,it is locked by cap and players cannot heal monsters as otherworldly mana is too pure\nBlock is a skill that does exactly as it's name, it blocks all attacks excluding eternal flame passive fire dmg if it has enought block, maximum of ∞ charges\narrow is a skill where physical or magic arrows are thrown")
                time.sleep(20)
                break
                
            informantion= input("do you want a description on more skills ")
                
        print("\n"*3)
        a='your max stat points must add to 200 or below'
        b="you have 5 different stats"
        c="lifesteal and fire affected by magic attack sand slash scales off by attack"
        d="the maximum roll you can recive on the dices is 20"
        e="attack chances are based on magic/attack chance"
        f="these variables need to be lower than the dices roll for you to hit the enemy"
        print(f"{a.center(75)}\n{b.center(75)}\n{c.center(75)}\n{d.center(75)}\n{e.center(75)}\n{f.center(75)}")
        print("\n")
            
            
        complete = "no"
        while complete == "no":
            P1preset = input("player 1 do you want to load a preset")
            if P1preset =="yes" or P1preset =="Yes" or P1preset =="Y" or P1preset =="y":
                print(f"the presets:")
                for i in preset:
                    print(preset.get(i))
                try:
                    P1userName = input("what is player 1 username")
                    P1presetName= input("what is the name of the present")
                    ii = 1
                    for i in preset:
                        if (i == P1presetName) or (str(ii) == str(P1presetName)):
                            P1boxstat=(preset.get(i))
                            P1presetName= (P1boxstat[0])
                            P1attack = int(P1boxstat[1])
                            P1defence = int(P1boxstat[2])
                            P1magic_attack = int(P1boxstat[3])
                            P1magic_defence = int(P1boxstat[4])
                            P1HP = int(P1boxstat[5])
                            break
                        ii+=1
                    P1boxStats = (P1userName,P1attack,P1defence,P1magic_attack,P1magic_defence,P1HP)
                    P1boxName = ("P1userName","P1attack","P1defence","P1magic_attack","P1magic_defence","P1HP")
                    
                    P1tem = 0 
                     
                    for i in P1boxStats:
                        if len(str(i)) > P1tem:
                            P1tem = len(str(i)) 
                    
                    print("these are the selected preset stats;")        
                    print(f"+{'-'*(P1tem+20)}+")
                    for i in range(len(P1boxStats)):
                        P1outbox = str(f"{P1boxName[i]}: {P1boxStats[i]}")
                        
                        print(f"|{(P1outbox).center(P1tem+20)}|")
                    print(f"+{'-'*(P1tem+20)}+") 
                    p1RES=input(f"are these the correct stats?(yes/no) ")
                    if p1RES != "yes" and p1RES != "y" and p1RES != "Y" and p1RES != "Yes":
                        print(int("car"))
                except:
                    continue
            else:
                try:
                    P1userName= input("what is player 1 name")
                    P1fairTotal=200
                    P1attack = int(input(f"{P1userName} what is your attack(intergers from 1 to 199) you have {P1fairTotal} allocation points left"))
                    P1fairTotal-=P1attack
                    P1defence = int(input(f"{P1userName} what is your defence(intergers from 1 to 199) you have {P1fairTotal} allocation points left"))
                    P1fairTotal-=P1defence
                    P1magic_attack = int(input(f"{P1userName} what is your magic attack(intergers from 1 to 199) you have {P1fairTotal} allocation points left"))
                    P1fairTotal-=P1magic_attack
                    P1magic_defence = int(input(f"{P1userName} what is your magic defence(intergers from 1 to 199) you have {P1fairTotal} allocation points left")) 
                    P1fairTotal-=P1magic_defence
                    P1HP= int(input(f"{P1userName} what is your hp(intergers from 1 to 199) you have {P1fairTotal} allocation points left"))
                    P1fairTotal-=P1HP
                    
                        
                    P1userStats = (P1userName,P1attack,P1defence,P1magic_attack,P1magic_defence,P1HP) 
                    for i in range(1,len(P1userStats)):
                        if abs(int(P1userStats[i])) != int(P1userStats[i]):
                            print(f"{P1userName} don't enter negative")
                            con = int("yes")
                except:
                    continue
            complete= "yes"
        print("\n"*10)
        complete = "no"
        while complete == "no":
            P2preset = input("player 2 do you want to load a preset")
            if P2preset =="yes" or P2preset =="Yes" or P2preset =="Y" or P2preset =="y":
                print(f"the preset:")
                for i in preset:
                    print(preset.get(i))
                try:
                    P2userName = input("what is player 2 username")
                    P2presetName= input("what is the name of the present")
                    ii =1 
                    for i in preset:
                        if (i == P2presetName) or (str(ii) == str(P2presetName)):
                            P2boxstat=(preset.get(i))
                            P2presetName = (P2boxstat[0])
                            P2attack = int(P2boxstat[1])
                            P2defence = int(P2boxstat[2])
                            P2magic_attack = int(P2boxstat[3])
                            P2magic_defence = int(P2boxstat[4])
                            P2HP = int(P2boxstat[5])
                            break
                        ii+=1
                    P2boxStats = (P2userName,P2attack,P2defence,P2magic_attack,P2magic_defence,P2HP)
                    P2boxName = ("P2userName","P2attack","P2defence","P2magic_attack","P2magic_defence","P2HP")
                    
                    P2tem = 0 
                     
                    for i in P2boxStats:
                        if len(str(i)) > P2tem:
                            P2tem = len(str(i)) 
                    
                    print("these are the selected preset stats;")        
                    print(f"+{'-'*(P2tem+20)}+")
                    for i in range(len(P2boxStats)):
                        P2outbox = str(f"{P2boxName[i]}: {P2boxStats[i]}")
                        
                        print(f"|{(P2outbox).center(P2tem+20)}|")
                    print(f"+{'-'*(P2tem+20)}+") 
                    P2RES=input(f"'\n' are these the correct stats?(yes/no) ")
                    if P2RES != "yes" and P2RES != "y" and P2RES != "Y" and P2RES != "Yes":
                        print(int("car"))
                except:
                    continue
            else:
                try:
                    P2userName= input("what is player 2 name")
                    P2fairTotal=200
                    P2attack = int(input(f"{P2userName} what is your attack(intergers from 1 to 199) you have {P2fairTotal} allocation points left"))
                    P2fairTotal-=P2attack
                    P2defence = int(input(f"{P2userName} what is your defence(intergers from 1 to 199) you have {P2fairTotal} allocation points left"))
                    P2fairTotal-=P2defence
                    P2magic_attack = int(input(f"{P2userName} what is your magic attack(intergers from 1 to 199) you have {P2fairTotal} allocation points left"))
                    P2fairTotal-=P2magic_attack
                    P2magic_defence = int(input(f"{P2userName} what is your magic defence(intergers from 1 to 199) you have {P2fairTotal} allocation points left")) 
                    P2fairTotal-=P2magic_defence
                    P2HP= int(input(f"{P2userName} what is your hp(intergers from 1 to 199) you have {P2fairTotal} allocation points left"))
    
                    P2userStats = (P2userName,P2attack,P2defence,P2magic_attack,P2magic_defence,P2HP)
                    for i in range(1,len(P2userStats)):
                        if abs(int(P2userStats[i])) != int(P2userStats[i]):
                            print(f"{P2userName} don't enter negative")
                            con = int("yes")
                except:
                    continue
            complete= "yes"
        if P1fairTotal <200:
            P1statPoints += 200-P1fairTotal
        if P1fairTotal <200:
            P2statPoints += 200-P2fairTotal





            
            
            
            

        P1fairTotal = (P1attack+P1defence+P1magic_attack+P1magic_defence+P1HP) 
        P2fairTotal = (P2attack+P2defence+P2magic_attack+P2magic_defence+P2HP)
        if P1fairTotal> 200:
            print(f"player {P1userName} please enter total stats below 201")
        if P2fairTotal> 200:
            print(f"player {P2userName} please enter total stats below 201")
print("\n")
endgame = "no"
P1newHP = P1HP
P2newHP = P2HP

while endgame != "yes":
    enemydic= {
    "goblin":"17,1,0,8,140",
    "dragon":"19,15,1,14,300"
    }

    n = random.randint(0,len(enemydic)-1)
    print(n)
    count = 0 
    for i in enemydic:
        if count == n:
            enemy = (f"{i},{enemydic.get(i)}")
        count += 1
    enemy = enemy.split(",")
    lvEnemyName = enemy[0]
    lvEnemyAttack = int(enemy[1])
    lvEnemyDefence = int(enemy[2])
    lvEnemyMagic_attack = int(enemy[3])
    lvEnemyMagic_defence = int(enemy[4])
    lvEnemyHP = int(enemy[5])
    EpassiveFireTurn = 0
    Eonfire ="no"
    #player one stats and exp
    while P1exp >= 2**P1lv :
        if P1exp >= 2**P1lv:
            P1exp = P1exp - 2**P1lv
            P1lv = P1lv + 1 
            P1statPoint = P1statPoint + 1
    if P1statPoint >= 1 :
            print(f"{P1userName} you have {P1statPoint}statPoints")
            P1statUse = input(f"{P1userName} do you want to your stat point ")
    
            while c or P1statUse == "Yes"  :
                P1statMany = int(input(f"{P1userName} how many stat points do u want to use "))
                P1statChoice = input(f"{P1userName} what stat do you want increased ")
                if P1statMany <= P1statPoint:
    
                    if P1statChoice == "attack" or P1statChoice ==  "Attack":
                        P1attack = P1attack + (1*P1statMany) 
                        print(f"(attack is increased by {1*P1statMany} points)")
                        P1statPoint = P1statPoint - (1*P1statMany)
                    elif P1statChoice == "defence" or P1statChoice ==  "defence":
                        P1defence = P1defence + (2*P1statMany)
                        print(f"(defence is increased by {2*P1statMany} point times)")
                        P1statPoint = P1statPoint - (1*P1statMany)
                    elif P1statChoice == "magic attack" or P1statChoice ==  "Magic attack":
                        P1magic_attack = P1magic_attack + (2*P1statMany)
                        P1magic_defence = P1magic_defence + (1*P1statMany)
                        print(f"(magic attack is increased by {2*P1statMany} and magic defence is increased by {1*statMany} point)",statMany,"times")
                        P1statPoint = P1statPoint - (1*P1statMany)
                    elif P1statChoice == "magic defence" or P1statChoice ==  "Magic defence":
                        P1magic_defence = P1magic_defence + (3*P1statMany)
                        print(f"(magic_defence is increased by {3*P1statMany} point times)")
                        P1statPoint = P1statPoint - (1*P1statMany)
                    elif P1statChoice == "HP" or P1statChoice ==  "health" or P1statChoice ==  "Health" :
                        P1newHP = P1newHP + (10*P1statMany)
                        P1HP = P1HP (10*P1statMany)
                        print(f"(your Health is increased by {10*P1statMany} point times)")
                        P1statPoint = P1statPoint - (1*P1statMany)
                    else:
                        print("invalid")
                    print("remaining stats points:",P1statPoint)
                    P1statUse = input("use more skill points ")
                    print("\n")
            if P1statPoint >= 10 :
                if P1presetName == "druid":
                    P1statUse = input(f"{P1userName} do you want to uses your stat point on druidUP blooldline")
                    if P1statUse == "yes" or P1statUse == "Yes" or P1statUse == "y":
                        P1statMany = int(input(f"{P1userName} how many druidUP blooldline points do u want 1 per 10 statPoints"))
                        if (P1statMany*10)<=P1statPoint:
                            P1statPoint-=(P1statMany*10)
                            P1druidUP+=P1statMany
                if P1presetName == "hunter":
                    P1statUse = input(f"{P1userName} do you want to uses your stat point on hunter blooldline")
                    if P1statUse == "yes" or P1statUse == "Yes" or P1statUse == "y":
                        P1statMany = int(input(f"{P1userName} how many hunter blooldline points do u want 1 per 10 statPoints"))
                        if (P1statMany*10)<=P1statPoint:
                            P1statPoint-=(P1statMany*10)
                if P1presetName == "knight":
                    P1statUse = input(f"{P1userName} do you want to uses your stat point on knight blooldline")
                    if P1statUse == "yes" or P1statUse == "Yes" or P1statUse == "y":
                        P1statMany = int(input(f"{P1userName} how many knight points do u want 1 per 10 statPoints"))
                        for i in range(P1statMany):
                            P1statChoice= input(f"{P1userName} do you want to upgrade reflective dmg or block efficiency")
                            try:
                                if P1statChoice == "reflective" or P1statChoice == "Reflective":
                                    if (P1statMany*10)<=P1statPoint:
                                        P1statPoint-=(P1statMany*10)
                                        P1reflectUP+=P1statMany
                                elif P1statChoice == "block" or P1statChoice == "Block":
                                    if (P1statMany*10)<=P1statPoint:
                                        P1statPoint-=(P1statMany*10)
                                        P1blockUP+=P1statMany
                                    else:
                                        print(f"{P1userName} insufficent ammount")
                            except:
                                print("error")
                            P1projectileUP+=P1statMany    
                if P1presetName == "cleric":
                    P1statUse = input(f"{P1userName} do you want to uses your stat point on cleric blooldline")
                    if P1statUse == "yes" or P1statUse == "Yes" or P1statUse == "y":
                        P1statMany = int(input(f"{P1userName} how many cleric points do u want 1 per 10 statPoints"))
                        try:
                            if P1statMany*10 <= P1statPoint
                                P1statPoint-=(P1statMany*10)
                                P1clericUP+=P1statMany
                            else:
                                print("insufficent ammount")
                        except:
                            print("error")
                        
                        
    #player two stats and exp
    while P2exp >= 2**P2lv :
        if P2exp >= 2**P2lv:
            P2exp = P2exp - 2**P2lv
            P2lv = P2lv + 1 
            P2statPoint = P2statPoint + 1
    if P2statPoint >= 1 :
            print(f"{P2userName} you have ",P2statPoint,"statPoints")
            P2statUse = input(f"{P2userName}do you want to your stat point ")
    
            while P2statUse == "yes" or P2statUse == "Yes"  :
                P2statMany = int(input(f"{P2userName} how many stat points do u want to use "))
                P2statChoice = input(f"{P2userName} what stat do you want increased ")
                if P2statMany <= P2statPoint:
    
                    if P2statChoice == "attack" or P2statChoice ==  "Attack":
                        P2attack = P2attack + (1*P2statMany) 
                        print(f"(attack is increased by {1*P2statMany} points)")
                        P2statPoint = P2statPoint - (1*P2statMany)
                    elif P2statChoice == "defence" or P2statChoice ==  "defence":
                        P2defence = P2defence + (2*P2statMany)
                        print(f"(defence is increased by {2*statMany} point times)")
                        P2statPoint = P2statPoint - (1*P2statMany)
                    elif P2statChoice == "magic attack" or P2statChoice ==  "Magic attack":
                        P2magic_attack = P2magic_attack + (2*P2statMany)
                        P2magic_defence = P2magic_defence + (1*P2statMany)
                        print(f"(magic attack is increased by {2*P2statMany} and magic defence is increased by {1*statMany} point)",statMany,"times")
                        P2statPoint = P2statPoint - (1*P2statMany)
                    elif statChoice == "magic defence" or statChoice ==  "Magic defence":
                        magic_defence = magic_defence + (3*statMany)
                        print(f"(magic_defence is increased by {3*P2statMany} point times)")
                        P2statPoint = P2statPoint - (1*P2statMany)
                    elif P2statChoice == "HP" or P2statChoice ==  "health" or P2statChoice ==  "Health" :
                        P2newHP = P2newHP + (10*P2statMany)
                        P2HP = P2HP + (10*P2statMany)
                        print(f"(your Health is increased by {10*P2statMany} point times)")
                        P2statPoint = P2statPoint - (1*P2statMany)
                    else:
                        print("invalid")
                    print(f"{P2userName}, remaining stats points:",P2statPoint)
                    P2statUse = input(f"{P2userName} use more skill points? ")
                    print("\n")
            if P2statPoint >= 10 :
                if P2presetName == "druid":
                    P2statUse = input(f"{P2userName}do you want to uses your stat point on druidUP blooldline ")
                    if P2statUse == "yes" or P2statUse == "Yes" or P2statUse == "y":
                        P2statMany = int(input(f"{P2userName}how many druidUP blooldline points do u want 1 per 10 statPoints "))
                        if (P2statMany*10)<=P2statPoint:
                            P2statPoint-=(P2statMany*10)
                            P2druidUP+=P2statMany
                if P1presetName == "hunter":
                    P2statUse = input(f"{P2userName}do you want to uses your stat point on hunter blooldline ")
                    if P2statUse == "yes" or P2statUse == "Yes" or P2statUse == "y":
                        P2statMany = int(input(f"{P2userName} how many hunter blooldline points do u want 1 per 10 statPoints"))
                        if (P2statMany*10)<=P2statPoint:
                            P2statPoint-=(P2statMany*10)
                            P2projectileUP+=P2statMany      
                if P2presetName == "knight":
                    P2statUse = input(f"{P2userName} do you want to uses your stat point on knight blooldline")
                    if P2statUse == "yes" or P2statUse == "Yes" or P2statUse == "y":
                        P2statMany = int(input(f"{P2userName} how many knight points do u want 1 per 10 statPoints"))
                        for i in range(P2statMany):
                            P2statChoice= input(f"{P2userName} do you want to upgrade reflective dmg or block efficiency")
                            try:
                                if P2statChoice == "reflective" or P2statChoice == "Reflective":
                                    if (P2statMany*10)<=P2statPoint:
                                        P2statPoint-=(P2statMany*10)
                                        P2reflectUP+=P2statMany
                                elif P2statChoice == "block" or P2statChoice == "Block":
                                    if (P2statMany*10)<=P2statPoint:
                                        P2statPoint-=(P2statMany*10)
                                        P2blockUP+=P2statMany
                                    else:
                                        print(f"{P2userName} insufficent ammount")
                            except:
                                print("error")
                if P2presetName == "cleric":
                    P2statUse = input("do you want to uses your stat point on cleric blooldline")
                    if P2statUse == "yes" or P2statUse == "Yes" or P2statUse == "y":
                        P2statMany = int(input("how many cleric points do u want 1 per 10 statPoints"))
                        try:
                            if P2statMany*10 <= P2statPoint
                                P2statPoint-=(P2statMany*10)
                                P2clericUP+=P2statMany
                            else:
                                print("insufficent ammount")
                        except:
                            print("error")
        
        
        
        
        
        
        
    P1boxStats = (P1userName,P1attack,P1defence,P1magic_attack,P1magic_defence,P1HP,P1lv,P1exp)
    P1boxName = ("P1userName","P1attack","P1defence","P1magic_attack","P1magic_defence","P1HP","P1lv","P1exp")
    P2boxStats = (P2userName,P2attack,P2defence,P2magic_attack,P2magic_defence,P2HP,P2lv,P2exp)
    P2boxName = ("P2userName","P2attack","P2defence","P2magic_attack","P2magic_defence","P2HP","P2lv","P2exp")
    P1tem = 0 
    P2tem = 0 
    for i in P1boxStats:
        if len(str(i)) > P1tem:
            P1tem = len(str(i)) 
    for i in P2boxStats:
        if len(str(i)) > P2tem:
            P2tem = len(str(i)) 
    print("these are the players stats;")        
    print(f"+{'-'*(P1tem+20)}+"," "*10,f"+{'-'*(P2tem+20)}+")
    for i in range(len(P1boxStats)):
        P1outbox = str(f"{P1boxName[i]}: {P1boxStats[i]}")
        P2outbox = str(f"{P2boxName[i]}: {P2boxStats[i]}")
        print(f"|{(P1outbox).center(P1tem+20)}|"," "*10,f"|{(P2outbox).center(P2tem+20)}|")
    print(f"+{'-'*(P1tem+20)}+"," "*10,f"+{'-'*(P2tem+20)}+")     
        

    print("\n")
    print("\n")
    
    if P1lv > P2lv:
        lv = P1lv
    elif P1lv < P2lv:
        lv = P2exp
    else:
        lv = 1
    while elv != lv :
        twice = 1
        while twice != 3:
            randomstat= random.randint(0,4)
            if randomstat == 0 :
                lvEnemyAttack = int(lvEnemyAttack) + 1
            elif randomstat == 1 :
                lvEnemyDefence = int(lvEnemyDefence) + 1
            elif randomstat == 2 :
                lvEnemyMagic_attack = int(lvEnemyMagic_attack) + 1
            elif randomstat == 3 :
                lvEnemyMagic_defence = int(lvEnemyMagic_defence) + 1
            elif randomstat == 4 :
                lvEnemyHP = int(lvEnemyHP) + 5
            twice = twice + 1
        elv = elv + 1   
    SMaxHP = lvEnemyHP
    
    
    
    print ("enemy name:",lvEnemyName)
    print ("enemy attack:",lvEnemyAttack)
    print ("enemy defence:",lvEnemyDefence)
    print ("enemy magic_attack:",lvEnemyMagic_attack)
    print ("enemy magic_defence:",lvEnemyMagic_defence)
    print ("enemy HP:",lvEnemyHP)
    Eskills = ("slash","double_slash","mass_slash","heal","block")
    skills = (f"the skills: \n1.lifesteal \n2.slash\n3.eternal flame\n4.necromany\n5.heal\n5.heal\n6.arrow")
                
    print("\n")
    
    
    informSkills = ("these are the skill u can use")
    m = (informSkills,skills)
    m= (m)
    c = ("pick a skill;","\n",m)
    while (P1dead =="no" or P2dead=="no") and not Edead=="yes":
        if turn == "P1" :#-------------------------------------------------------------------
            print("\n "*3)
            try:
                if P1presetName == "hunter":
                    P1projectile = 2 + P1projectileUP
                else:
                    P1projectile = 1
            except:
                print("")
            if P1newHP>0:
                if P1losses > 4:
                    runDone = input("do u want to end game")
                    if runDone != "no"  :
                        trap = "you fell into a ditch and died","you got ganged by monster and was eaten alive","you got robbed of everything and froze to death","the monster from before had poisoned you and you die a painful and long death due to Carbon monoxide poisoning","i hate deserters so die","as you gain distance from your enemy, you missteped onto the magic trap you set previously"
                        UT = random.randint(0,(len(trap)-1))
                        UTrap = trap[UT]
                        print(f"{P1userName} you successflly ran away however{UTrap}")
                        P1newHP= 0
                        
                P1attackChoise = input(f"{P1userName} type who you want to target ({P2userName} or {lvEnemyName})")
                
                print(f"pick a skill from the skills: \n1.lifesteal \n2.slash\n3.eternal flame\n4.heal\n5.block\n6.arrow")
                if P1presetName =="cleric":
                    print("7.buffer")
                P1skillChoise = str(input())
                if P1attackChoise == "player2" or P1attackChoise == "Player2" or P1attackChoise == P2userName or P1attackChoise == str(1):
                    if P2newHP  >0:
                        totalBuff=1
                        if P22buff == "yes":
                            print(f"buff of {P2buff} on {P2userName} from {P2userName} is effective ")
                            totalBuff=totalBuff*P2buff
                        if P12buff == "yes":
                            print(f"buff of {P1buff} on {P2userName} from {P1userName} is effective")
                            totalBuff=totalBuff*P1buff
                        if totalBuff != 1:
                            print(f"buff of {totalBuff} on {P2userName}")
                        
                        TEMuserName= P2userName
                        TEMattack = P2attack*totalBuff
                        TEMdefence = P2defence*totalBuff
                        TEMmagic_attack = P2magic_attack*totalBuff
                        TEMmagic_defence = P2magic_defence*totalBuff
                        TEMHP= P2newHP
                        P1attackChoise = P2userName
                    else:
                        print("this choice is already dead you miss your turn")
                        P1attackChoise = "null"
                elif P1attackChoise == "mob" or P1attackChoise == "monster" or P1attackChoise == lvEnemyName or P1attackChoise == str(2):
                    if lvEnemyHP >0:
                        totalBuff=1
                        if P23buff == "yes":
                            print(f"buff of {P2buff} on {lvEnemyName} from {P2userName} is effective ")
                            totalBuff=totalBuff*P2buff
                        if P13buff == "yes":
                            print(f"buff of {P1buff} on {lvEnemyName} from {P1userName} is effective")
                            totalBuff=totalBuff*P1buff
                        if totalBuff != 1:
                            print(f"buff of {totalBuff} on {lvEnemyName}")
                        
                        TEMuserName= lvEnemyName
                        TEMattack = lvEnemyAttack*totalBuff
                        TEMdefence = lvEnemyDefence*totalBuff
                        TEMmagic_attack = lvEnemyMagic_attack*totalBuff
                        TEMmagic_defence = lvEnemyMagic_defence*totalBuff
                        TEMHP= lvEnemyHP
                        P1attackChoise = lvEnemyName
                    else:
                        print("this choice is already dead you miss your turn")
                        P1attackChoise = "null"
                elif P1attackChoise == "player1" or P1attackChoise == "Player1" or P1attackChoise == P1userName or P1attackChoise == str(3) or P1attackChoise == "me"or P1attackChoise == "myself" :
                    if P1newHP  >0:
                        totalBuff=1
                        if P11buff == "yes":
                            print(f"buff of {P1buff} on {P1userName} from {P1userName} is effective ")
                            totalBuff=totalBuff*P1buff
                        if P21buff == "yes":
                            print(f"buff of {P1buff} on {P1userName} from {P1userName} is effective")
                            totalBuff=totalBuff*P1buff
                        if totalBuff != 1:
                            print(f"buff of {totalBuff} on {P1userName}")
                        
                        TEMuserName= P1userName
                        TEMattack = P1attack*totalBuff
                        TEMdefence = P1defence*totalBuff
                        TEMmagic_attack = P1magic_attack*totalBuff
                        TEMmagic_defence = P1magic_defence*totalBuff
                        TEMHP= P1newHP
                        P1attackChoise = P1userName
                    else:
                        print("this choice is already dead you miss your turn")
                        P1attackChoise = "null"
                else:
                    P1attackChoise="null"
                    print(f"no target selected, {P1userName} yo have missed your turn")
                
                
                
                if P1attackChoise !="null":
                    print("\n"*2)
                    dice = int(random.randint(1,20))
                    #perception
                    
                    P1perception = (P1attack+P1magic_attack)
                    TEMPerception=(TEMmagic_attack+TEMattack)
                    accuracy=((TEMPerception/P1perception)*20)
                    if accuracy >20:
                        accuracy= 20
                    print(f"your accuracy against the selected enemy is {accuracy}")
                   
                    
                    print(f"{P1userName} your perception is {P1perception}")
                    print(f"{TEMuserName} your perception is {TEMPerception}")
                    print("\n")
                    
                    print (dice,"on the dice")
                    time.sleep(3)
                    #total acact 
                    
                    if dice == 20:
                        dmgScale = random.randint(2,10)
                        print(f"you got a 20 on a dice so your attack for this turn is mulriplied by {dmgScale}")
                        Tmagic_Attack = (((P1magic_attack*dmgScale) - TEMmagic_defence))
                        Tphysical_Attack = (((P1attack*dmgScale) - TEMdefence))
                    else:
                        dmgScale=0
                        Tmagic_Attack = (((P1magic_attack) - TEMmagic_defence))
                        Tphysical_Attack = (((P1attack) - TEMdefence))
                    if Tmagic_Attack <= 0:
                        Tmagic_Attack= 1
                    if Tphysical_Attack <= 0:
                        Tphysical_Attack= 1
                    
                    if P11buff == "yes":
                        print(f"buff of {P1buff}")
                        Tmagic_Attack = Tmagic_Attack*P1buff
                        Tphysical_Attack = Tphysical_Attack*P1buff
                        
                    if P21buff == "yes":
                        print(f"buff of {P2buff}")
                        Tmagic_Attack = Tmagic_Attack*P2buff
                        Tphysical_Attack = Tphysical_Attack*P2buff
                        
                    
                    
                    
                    print ("dice",dice)
                    if P1skillChoise == "lifesteal" or P1skillChoise == "Lifesteal" or P1skillChoise == "1":
                        P1skillChoise = "lifesteal"
                        try:
                            if P1presetName == "mage":
                                accuracy -= 4+(1*(10/P1lv))
                                print(f"new accuracy {accuracy}")
                        except:
                            print("")
                        
                        if accuracy <= dice:
                             
                            we = (Tmagic_Attack/10)   
                            try:
                                if P1presetName == "druid":
                                    P1druid = 2+P1druidUP
                                    we*P1druid
                            except:
                                print("")
                            displayVitality= "no"
                            P1newHP = P1newHP + we
                            TEMHP = TEMHP - we
                            if we > TEMHP:
                                displayVitality= "yes"
                                P1statPoint = P1statPoint - 1
                                
                            
                            print("\n")
                            print(f"{TEMuserName} lost",we,"HP from your lifesteal")
                            print("you gained",we,"additional HP from your lifesteal")
                            if displayVitality== "yes":
                                print("the additonal vitlity is gained from the environment at the cost of enraging the environment, they took 1 stats points");
                                displayVitality= "no"
                        else :
                            print("player has missed")
                            P1losses = P1losses + 1
                        P1skillChoise = "null"
                        turn = "enemy"
                    
                    elif P1skillChoise == "slash" or P1skillChoise== "Slash" or P1skillChoise== str("2") :
                        P1skillChoise = "slash"
                        if accuracy <= dice:
                            we = (Tphysical_Attack/2)                    
                            TEMHP = TEMHP - we
                            
                            print("\n")
                            print("you do",we,"physical damage from a slash ")
                            print("\n")
                            turn = "enemy"
                        else:
                            print("player has missed")
                            turn = "enemy"
                            P1losses = P1losses + 1
                        P1skillChoise = "null"
                        print("\n")
                    
                    elif P1skillChoise == "eternal flame" or P1skillChoise =="Eternal flame" or P1skillChoise == str("3"):
                        P1skillChoise = "eternal flame"
                        try:
                            if P1presetName == "mage":
                                accuracy -= 4+(1*(10/P1lv))
                                print(f"new accuracy {accuracy}")
                        except:
                            print("")
                        for i in range (P1projectile):
                            print(f"{i+1} attack")
                            if accuracy <= dice:
                                if P1fireT == "second":
                                    fdamage = int(Tmagic_Attack/10)
                                    TEMHP = TEMHP - (fdamage)
                                    print(f"{TEMuserName} will take {fdamage} fire damage")
                                elif P1fireT == "first":
                                    fdamage = int(Tmagic_Attack/3)
                                    TEMHP = TEMHP - fdamage
                                    print(f"{TEMuserName} will take {fdamage} fire damage")
                                    P1fireT = "second"
                                    
                                    
                                    if P1attackChoise == "player2" or P1attackChoise == "Player2" or P1attackChoise == "P2userName":
                                        P1passiveFIRE= 12 #first digit for who attacked and second for reciver
                                        P12passiveFIREDMG = Tmagic_Attack/20
                                        P2passiveFireTurn = 3
                                        P2onfire = "yes"
                                    elif P1attackChoise == "mob" or P1attackChoise == "monster" or P1attackChoise == "NPC":
                                        EpassiveFIRE= 13
                                        P13passiveFIREDMG = Tmagic_Attack/20
                                        EpassiveFireTurn = 3
                                        Eonfire= "yes"
                            else:
                                P1losses = P1losses + 1
                                print("missed")
                            if i != (P1projectile-1):
                                dice =  int(random.randint(1,20))
                                print(f"dice:{dice}")
                                if dice == 20:
                                    dmgScale = random.randint(2,10)
                                    print(f"you got a 20 on a dice so your attack for this turn is mulriplied by {dmgScale}")
                                    Tmagic_Attack = (((P1magic_attack*dmgScale) - TEMmagic_defence))
                                    Tphysical_Attack = (((P1attack*dmgScale) - TEMdefence))
                                else:
                                    dmgScale=0
                                    Tmagic_Attack = (((P1magic_attack) - TEMmagic_defence))
                                    Tphysical_Attack = (((P1attack) - TEMdefence))
                                if Tmagic_Attack <= 0:
                                    Tmagic_Attack= 1
                                if Tphysical_Attack <= 0:
                                    Tphysical_Attack= 1
                    elif P1skillChoise == "heal" or P1skillChoise == "Heal" or P1skillChoise == str(4):
                        P1skillChoise = "heal"
                        try:
                            if P1presetName == "mage":
                                accuracy -= 4+(1*(10/P1lv))
                                print(f"new accuracy {accuracy}")
                        except:
                            print("")
                        try:
                            if P1presetName == "cleric":
                                P1heal = 10+P1clericUP
                            else:
                                P1heal = 1
                        except:
                            print("")
                        if accuracy <= dice:
                            heal = int(P1HP/2.5)*P1heal
                            selfHeal=input("do you want to heal yourself?(y/n)")
                            if selfHeal == "yes" or selfHeal == "Yes" or selfHeal == "y" or selfHeal == "y":
                                print(f"healing used, you healed {heal}")
                                P1newHP = P1newHP + heal
                                if P1newHP > P1HP:
                                    P1newHP = P1HP
                                    print("blocked by cap")
                            else:
                                TEMHP = TEMHP+ heal
                                print(f"healing used, you healed {TEMuserName} by {heal}")
                                    
                                
                            #else:    
                        else:
                            print(f"there are few existences that can fail to cast a healing skill a pig and {userName} congrats")
                    elif P1skillChoise == "block" or P1skillChoise == "Block" or P1skillChoise == str(5):
                        P1skillChoise = "block"
                        P1block = "yes"
                        P1blockStack += 1
                        P1blockBase = input("do you want a magic or normal shield set(magic/normal)")
                        if P1blockBase == "magic" or P1blockBase == "Magic" :
                            P1blockAmount = int(P1magic_defence/2)
                        else:    
                            if P1presetName == "knight":
                                P1knight=2+P1knightUP
                                P1blockAmount = int(P1defence/2)*P1knight
                            else:
                                P1blockAmount = int(P1defence/2)
                        
                        print(f"{P1userName} has set a {P1blockBase} shield of {P1blockAmount}")
                    elif P1skillChoise == "arrow barrage" or P1skillChoise == "Arrow barrage" or P1skillChoise == str(6):
                        P1skillChoise = "arrow barrage"
                        try:
                            if P1presetName == "mage":
                                accuracy -= 4+(1*(10/P1lv))
                                print(f"new accuracy {accuracy}")
                        except:
                            print("")
                        for i in range (P1projectile):
                            print(f"{i+1} attack")
                            if accuracy <= dice:
                                we = (Tphysical_Attack/2)                    
                                TEMHP = TEMHP - we
                                
                                print("\n")
                                print("you do",we,"physical damage from an arrow barrage ")
                                
                            else:
                                print("missed")
                            if i != (P1projectile-1):
                                dice = int(random.randint(1,20))
                                print(f"dice:{dice}")
                                if dice == 20:
                                    dmgScale = random.randint(2,10)
                                    print(f"you got a 20 on a dice so your attack for this turn is mulriplied by {dmgScale}")
                                    Tmagic_Attack = (((P1magic_attack*dmgScale) - TEMmagic_defence))
                                    Tphysical_Attack = (((P1attack*dmgScale) - TEMdefence))
                                else:
                                    dmgScale=0
                                    Tmagic_Attack = (((P1magic_attack) - TEMmagic_defence))
                                    Tphysical_Attack = (((P1attack) - TEMdefence))
                                if Tmagic_Attack <= 0:
                                    Tmagic_Attack= 1
                                if Tphysical_Attack <= 0:
                                    Tphysical_Attack= 1
                    elif (P1skillChoise == "buffer" or P1skillChoise == "Buffer" or P1skillChoise == str(7)) and P1presetName =="cleric":
                        P1skillChoise = "buffer"
                        try:
                            P1buff = (10+P1clericUP)+dmgScale
                            P1buffT = math.ceil(1*(P1lv/10))
                            if str(TEMuserName) == str(P1userName):
                                P11buff = "yes"
                                P11buffT = P1buffT
                                print(f"{TEMuserName} has been buffed by {P1userName} with a multiplier of {P1buff} for {P1buffT} turn")
                            elif str(TEMuserName) == str(P2userName):
                                P12buff = "yes"
                                P12buffT = P1buffT
                                print(f"{TEMuserName} has been buffed by {P1userName} with a multiplier of {P1buff} for {P1buffT} turn")
                            elif str(TEMuserName) == str(lvEnemyName):
                                P13buff = "yes"
                                P13buffT = P1buffT
                                print(f"{TEMuserName} has been buffed by {P1userName} with a multiplier of {P1buff} for {P1buffT} turn")    
                            else:
                                print("invaild buff target")
                        except:
                            print("invalid buff choice")
                    else:
                        print("\n"*3)
                        print(P1skillChoise,"is not a skill")
                        print("you miss your turn due to your inability to spell a word correctly🤓")
                        print("please correctly type the skill you want to use next time")
                    print("\n"*2)
                    
                    print("\n"*2)
                    if P2dead != "yes":
                        if P1attackChoise == "player2" or P1attackChoise == "Player2" or P1attackChoise == P2userName:
                            if P2presetName =="knight":
                                P2reflect = 1 + P2reflectUP
                                DMG = TEMHP - P2newHP
                                P1newHP-= ((P2reflect/100)*DMG)
                                if P1dead =="no" and P1newHP <=0:
                                    P1dead ="yes" 
                                    P2exp += 4000*P1lv
                                    P2score+=400*P1lv
                            if P2block == "yes":
                                DMG = TEMHP - P2newHP
                                recivedDMG = P2blockAmount - DMG
                                if recivedDMG <0:
                                    recivedDMG = abs(recivedDMG)
                                    TEMHP = TEMHP - recivedDMG
                                    print(f"{P2userName} has blocked {P2blockAmount} damage and received {recivedDMG} damage this turn")
                                else:
                                    print(f"{P2userName} has blocked the attack")
                            else:
                                if P1skillChoise != "heal" and P1skillChoise != "block" and P1skillChoise != "buffer":
                                    DMG = abs(TEMHP - P2newHP)
                                    if DMG == 0 or DMG == int(0):
                                        DMG = "no"
                                    print(f"the {P2userName} has taken {DMG} damage this turn" )
                            P2newHP = TEMHP
                            if TEMHP <= 0:
                                if P2dead == "yes":
                                    print(f"{TEMuserName} is already dead")
                                elif P2dead == "no":
                                    print(f"{P1userName} you have killed {P2userName} and recived {4000*P2lv} experiances")
                                    P1exp = P1exp + (4000*P2lv)
                                    P2dead = "yes" 
                    if Edead != "yes":
                        if P1attackChoise == "mob" or P1attackChoise == "monster" or P1attackChoise == lvEnemyName:
                            if Eblock == "yes":
                                DMG = TEMHP - lvEnemyHP
                                recivedDMG = EblockAmount - DMG
                                if recivedDMG <0:
                                    recivedDMG = abs(recivedDMG)
                                    TEMHP = TEMHP - recivedDMG
                                    print(f"{lvEnemyName} has blocked {DMG} damage and received {recivedDMG} damage this turn")
                                else:
                                    print(f"{lvEnemyName} has blocked the attack")
                            else:
                                if P1skillChoise != "heal" and P1skillChoise != "block" and P1skillChoise != "buffer":
                                    DMG = (abs(TEMHP - lvEnemyHP))
                                    if DMG == 0 or DMG == int(0):
                                        DMG ="no"
                                    print(f"{lvEnemyName} has taken {DMG} damage this turn" )
                            lvEnemyHP = TEMHP
                            
                            if lvEnemyName =="goblin":
                                Mtype = 40
                            elif lvEnemyName =="dragon":
                                Mtype = 180   
                            if TEMHP <= 0:
                                if Edead == "yes":
                                    print(f"{TEMuserName} is already dead")
                                if Edead == "no":
                                    
                                    print(f"{P1userName} you have killed {lvEnemyName} and recived {Mtype*elv} experiances")
                                    P1exp = P1exp + (Mtype*elv)
                                        
                                    Edead = "yes" 
                
                    if P1dead != "yes":
                        if P1onfire =="yes":
                            if P1passiveFIRE == 21:
                                P1newHP = P1newHP - P21passiveFIREDMG
                                print(f"{P2userName} causes {P21passiveFIREDMG} passive fire damage on you")
                                P2exp += 4000*P1lv
                                P2score+=400*P1lv
                                if P1newHP <=0:
                                    print(f"the passive fire damage has killed {P1userName} and recived {4000*P1lv} experiances")
                                    P1dead = "yes"
                            elif P1passiveFIRE == 31:
                                P1newHP = P1newHP - P31passiveFIREDMG
                                print(f"{lvEnemyName} causes {P31passiveFIREDMG} passive fire damage on you")
                                if P1newHP <=0:
                                    print(f"the passive fire damage has killed {P1userName}")
                                    P1dead = "yes"
                            P1passiveFireTurn -=1
                            if P1passiveFireTurn == 0:
                                P1onfire ="no"
            turn = "P2" 
            if P11buff == "yes":
                P11buffT -=1
                if P11buffT==0:
                    P11buff == "no"
            if P21buff == "yes":
                P21buffT -=1
                if P21buffT==0:
                    P21buff == "no"
        elif turn == "P2" :#-------------------------------------------------------------------
            print("\n "*3)
            
            try:
                if P2presetName == "hunter":
                    P2projectile = 2 + P2projectileUP
                else:
                    P2projectile = 1
            except:
                print("")
            if P2newHP>0:
                if P2losses > 4:
                    runDone = input("do u want to end game")
                    if runDone != "no"  :
                        trap = "you fell into a ditch and died","you got ganged by monster and was eaten alive","you got robbed of everything and froze to death","the monster from before had poisoned you and you die a painful and long death due to Carbon monoxide poisoning","i hate deserters so die","as you gain distance from your enemy, you missteped onto the magic trap you set previously"
                        UT = random.randint(0,(len(trap)-1))
                        UTrap = trap[UT]
                        print(f"{P2userName} you successflly ran away however{UTrap}")
                        P2newHP= 0
                        
                P2attackChoise = input(f"{P2userName} type who you want to target ({P1userName} or {lvEnemyName})")
                print(f"pick a skill from the skills: \n1.lifesteal \n2.slash\n3.eternal flame\n4.heal\n5.block\n6.arrow")
                if P2presetName =="cleric":
                    print("7.buffer")
                P2skillChoise =  str(input())
                
                if P2attackChoise == "player1" or P2attackChoise == "Player1" or P2attackChoise == P1userName  or P2attackChoise == str(1):
                    if P1newHP > 0 :
                        totalBuff=1
                        if P11buff == "yes":
                            print(f"buff of {P1buff} on {P1userName} from {P1userName} is effective ")
                            totalBuff=totalBuff*P1buff
                            
                        if P21buff == "yes":
                            print(f"buff of {P2buff} on {P1userName} from {P2userName} is effective")
                            totalBuff=totalBuff*P2buff
                            
                        TEMuserName= P1userName
                        TEMattack = P1attack*totalBuff
                        TEMdefence = P1defence*totalBuff
                        TEMmagic_attack = P1magic_attack*totalBuff
                        TEMmagic_defence = P1magic_defence*totalBuff
                        TEMHP= P1newHP
                    else:
                        print("this choice is already dead you miss your turn")
                        P1attackChoise = "null"
                elif P2attackChoise == "mob" or P2attackChoise == "monster" or P2attackChoise == lvEnemyName or P2attackChoise == "2" :
                    if lvEnemyHP>0:
                        totalBuff=1
                        if P23buff == "yes":
                            print(f"buff of {P2buff} on {lvEnemyName} from {P2userName} is effective ")
                            totalBuff=totalBuff*P2buff
                        if P13buff == "yes":
                            print(f"buff of {P1buff} on {lvEnemyName} from {P1userName} is effective ")
                            totalBuff=totalBuff*P1buff
                        
                        TEMuserName= lvEnemyName
                        TEMattack = lvEnemyAttack*totalBuff
                        TEMdefence = lvEnemyDefence*totalBuff
                        TEMmagic_attack = lvEnemyMagic_attack*totalBuff
                        TEMmagic_defence = lvEnemyMagic_defence*totalBuff
                        TEMHP= lvEnemyHP
                        P2attackChoise = lvEnemyName
                    else:
                        print("this choice is already dead you miss your turn")
                        P1attackChoise = "null"
                elif P2attackChoise == "player2" or P2attackChoise == "Player2" or P2attackChoise == P2userName or P2attackChoise == str(3) or P2attackChoise == "me"or P2attackChoise == "myself" :
                    if P2newHP  >0:
                        totalBuff=1
                        if P22buff == "yes":
                            print(f"buff of {P2buff} on {P2userName} from {P2userName} is effective ")
                            totalBuff=totalBuff*P2buff
                        if P12buff == "yes":
                            print(f"buff of {P1buff} on {P2userName} from {P1userName} is effective")
                            totalBuff=totalBuff*P1buff
                        if totalBuff != 1:
                            print(f"buff of {totalBuff} on {P2userName}")
                        
                        TEMuserName= P2userName
                        TEMattack = P2attack*totalBuff
                        TEMdefence = P2defence*totalBuff
                        TEMmagic_attack = P2magic_attack*totalBuff
                        TEMmagic_defence = P2magic_defence*totalBuff
                        TEMHP= P2newHP
                        P1attackChoise = P2userName
                    else:
                        print("this choice is already dead you miss your turn")
                        P1attackChoise = "null"
                else:
                    P2attackChoise="null"
                    print(f"no target selected, {P2userName} your have missed your turn")
                
                
                if P2attackChoise !="null":
                    print("\n"*2)
                    
                    dice = int(random.randint(1,20))
                    
                    
                    time.sleep(3)
                    #total acact 
                    
                    if dice == 20:
                        dmgScale = random.randint(2,10)
                        print(f"you got a 20 on a dice so your attack for this turn is mulriplied by {dmgScale}")
                        Tmagic_Attack = (((P2magic_attack*dmgScale) - TEMmagic_defence))
                        Tphysical_Attack = (((P2attack*dmgScale) - TEMdefence))
                    else:
                        dmgScale=0
                        Tmagic_Attack = (((P2magic_attack) - TEMmagic_defence))
                        Tphysical_Attack = (((P2attack) - TEMdefence))
                    if Tmagic_Attack <= 0:
                        Tmagic_Attack= 1
                    if Tphysical_Attack <= 0:
                        Tphysical_Attack= 1
                    
                    if P22buff == "yes":
                        print(f"buff of {P2buff}")
                        Tmagic_Attack = Tmagic_Attack*P2buff
                        Tphysical_Attack = Tphysical_Attack*P2buff
                        
                    if P12buff == "yes":
                        print(f"buff of {P1buff}")
                        Tmagic_Attack = Tmagic_Attack*P1buff
                        Tphysical_Attack = Tphysical_Attack*P1buff
                        
                    
                    
                    #perception
                    
                    P2perception = (Tphysical_Attack+Tmagic_Attack)
                    TEMPerception=(TEMmagic_attack+TEMattack)
                    accuracy=((TEMPerception/P2perception)*20)
                    if accuracy >20:
                        accuracy= 20
                    
                   
                    print(f"{P2userName} your perception is {P2perception}")
                    print(f"{TEMuserName} your perception is {TEMPerception}")
                    print(f"your accuracy against the selected enemy is {accuracy}")
                    print("\n")
                    print("\n")
                    
                    print ("dice",dice)
                    
                    if P2skillChoise == "lifesteal" or P2skillChoise == "Lifesteal" or P2skillChoise == "1":
                        P2skillChoise = "lifesteal"
                        try:
                            if P2presetName == "mage":
                                accuracy -= 4+(1*(10/P2lv))
                                print(f"new accuracy {accuracy}")
                        except:
                            print("")
                        
                        if accuracy <= dice:
                            #copy
                            we = (Tmagic_Attack/10)   
                            try:
                                if P2presetName == "druid":
                                    P2druid = 2+P2druidUP
                                    we*P2druid
                            except:
                                print("")
                            displayVitality= "no"
                            P2newHP = P2newHP + we
                            TEMHP = TEMHP - we
                            if we > TEMHP:
                                displayVitality= "yes"
                                P2statPoint = P2statPoint - 1
                                
                            
                            print("\n")
                            print(f"{TEMuserName} lost",we,"HP from your lifesteal")
                            print("you gained",we,"additional HP from your lifesteal")
                            if displayVitality== "yes":
                                print("the additonal vitlity is gained from the environment at the cost of enraging the environment, they took 1 stats points");
                                displayVitality= "no"
                        else :
                            print(f"{P2userName} you missed")
                            P2losses = P2losses + 1
                        P2skillChoise = "null"
                        
                    
                    elif P2skillChoise == "slash" or P2skillChoise== "Slash" or P2skillChoise== str("2") :
                        P2skillChoise = "slash"
                        if accuracy <= dice:
                            we = (Tphysical_Attack/2)                    
                            
                            TEMHP = TEMHP - we
                            
                            
                            print("\n")
                            print("you do",we,"physical damage from a slash ")
                            print("\n")
                            
                        else:
                            print(f"{P2userName} you missed")
                            
                            P2losses = P2losses + 1
                        P2skillChoise = "null"
                        print("\n")
                    
                    elif P2skillChoise == "eternal flame" or P2skillChoise =="Eternal flame" or P2skillChoise == str("3"):
                        P2skillChoise = "eternal flame"
                        try:
                            if P2presetName == "mage":
                                accuracy -= 4+(1*(10/P2lv))
                                print(f"new accuracy {accuracy}")
                        except:
                            print("")
                        for i in range (P2projectile):
                            print(f"{i+1} attack")
                            if accuracy <= dice:
                                if P2fireT == "second":
                                    fdamage = int(Tmagic_Attack/10)
                                    TEMHP = TEMHP - (fdamage)
                                    print(f"{TEMuserName} will take {fdamage} fire damage")
                                elif P2fireT == "first":
                                    fdamage = int(Tmagic_Attack/3)
                                    TEMHP = TEMHP - fdamage
                                    print(f"{TEMuserName} will take {fdamage} fire damage")
                                    P2fireT = "second"
                                    
                                    
                                    if P2attackChoise == "player1" or P2attackChoise == "Player1" or P2attackChoise == P1userName:
                                        P1passiveFIRE= 21 #first digit for who attacked and second for reciver
                                        P21passiveFIREDMG = Tmagic_Attack/20
                                        P1passiveFireTurn = 3
                                        P1onfire = "yes"
                                    elif P2attackChoise == "mob" or P2attackChoise == "monster" or P2attackChoise == "NPC":
                                        EpassiveFIRE= 23
                                        P23passiveFIREDMG = Tmagic_Attack/20
                                        EpassiveFireTurn = 3
                                        Eonfire = "yes"
                            else:
                                P2losses = P2losses + 1
                                print(f"miss")
                            if i != (P2projectile-1):
                                dice =  int(random.randint(1,20))
                                print(f"dice:{dice}")
                                if dice == 20:
                                    dmgScale = random.randint(2,10)
                                    print(f"you got a 20 on a dice so your attack for this turn is mulriplied by {dmgScale}")
                                    Tmagic_Attack = (((P1magic_attack*dmgScale) - TEMmagic_defence))
                                    Tphysical_Attack = (((P1attack*dmgScale) - TEMdefence))
                                else:
                                    dmgScale=0
                                    Tmagic_Attack = (((P1magic_attack) - TEMmagic_defence))
                                    Tphysical_Attack = (((P1attack) - TEMdefence))
                                if Tmagic_Attack <= 0:
                                    Tmagic_Attack= 1
                                if Tphysical_Attack <= 0:
                                    Tphysical_Attack= 1
                    elif P2skillChoise == "heal" or P2skillChoise == "Heal" or P2skillChoise == str(4):
                        P2skillChoise = "heal"
                        try:
                            if P2presetName == "mage":
                                accuracy -= 4+(1*(10/P2lv))
                                print(f"new accuracy {accuracy}")
                        except:
                            print("")
                        try:
                            if P1presetName == "cleric":
                                P1heal = 10+P1clericUP
                            else:
                                P1heal = 1
                        except:
                            print("")
                        if accuracy <= dice:
                            heal = int(P2HP/2.5)
                            selfHeal=input("do you want to heal yourself?(y/n)")
                            if selfHeal == "yes" or selfHeal == "Yes" or selfHeal == "y" or selfHeal == "y":
                                print(f"healing used, you healed {heal}")
                                P2newHP = P2newHP + heal
                                if P2newHP > P2HP:
                                    P2newHP = P2HP
                                    print("blocked by cap")
                            else:
                                TEMHP = TEMHP+ heal
                                print(f"healing used, you healed {TEMuserName} by {heal}")
                                
                                
                            #else:    
                        else:
                            print(f"there are few existences that can fail to cast a healing skill a pig and {P2userName} congrats")
                    elif P2skillChoise == "block" or P2skillChoise == "Block" or P2skillChoise == str(5):
                        P2skillChoise = "block"
                        P2block = "yes"
                        P2blockStack += 1
                        P2blockBase = input("do you want a magic or normal shield set(magic/normal)")
                        if P2blockBase == "magic" or P2blockBase == "Magic" :
                            P2blockAmount = int(P2magic_defence/2)
                        else:    
                            if P2presetName == "knight":
                                P2knight=2+P2knightUP
                                P2blockAmount = int(P2defence/2)*P2knight
                            else:
                                P2blockAmount = int(P2defence/2)
                    elif P2skillChoise == "arrow barrage" or P2skillChoise == "Arrow barrage" or P2skillChoise == str(6):
                        P2skillChoise = "arrow"
                        try:
                            if P2presetName == "mage":
                                accuracy -= 4+(1*(10/P2lv))
                                print(f"new accuracy {accuracy}")
                        except:
                            print("")
                        for i in range (P2projectile):
                            print(f"{i+1} attack")
                            if accuracy <= dice:
                                we = (Tphysical_Attack/2)                    
                                TEMHP = TEMHP - we
                                
                                print("\n")
                                print("you do",we,"physical damage from an arrow barrage ")
                            else:
                                print("missed")
                            if i != (P2projectile-1):
                                dice =  int(random.randint(1,20))
                                print(f"dice:{dice}")
                                if dice == 20:
                                    dmgScale = random.randint(2,10)
                                    print(f"you got a 20 on a dice so your attack for this turn is mulriplied by {dmgScale}")
                                    Tmagic_Attack = (((P1magic_attack*dmgScale) - TEMmagic_defence))
                                    Tphysical_Attack = (((P1attack*dmgScale) - TEMdefence))
                                else:
                                    dmgScale=0
                                    Tmagic_Attack = (((P1magic_attack) - TEMmagic_defence))
                                    Tphysical_Attack = (((P1attack) - TEMdefence))
                                if Tmagic_Attack <= 0:
                                    Tmagic_Attack= 1
                                if Tphysical_Attack <= 0:
                                    Tphysical_Attack= 1
                    elif (P2skillChoise == "buffer" or P2skillChoise == "Buffer" or P2skillChoise == str(7))and P2presetName =="cleric":    
                        P2skillChoise = "buffer"
                        try:
                            P2buff = (10+P2clericUP)+dmgScale
                            P2buffT = math.ceil(1*(P2lv/10))
                            if str(TEMuserName) == str(P2userName):
                                P21buff = "yes"
                                P21buffT = P2buffT
                                print(f"{TEMuserName} has been buffed by {P2userName} with a multiplier of {P2buff} for {P2buffT} turn")
                            elif str(TEMuserName) == str(P2userName):
                                P22buff = "yes"
                                P22buffT = P2buffT
                                print(f"{TEMuserName} has been buffed by {P2userName} with a multiplier of {P2buff} for {P2buffT} turn")
                            elif str(TEMuserName) == str(lvEnemyName):
                                P23buff = "yes"
                                P23buffT = P2buffT
                                print(f"{TEMuserName} has been buffed by {P2userName} with a multiplier of {P2buff} for {P2buffT} turn")    
                            else:
                                print("invaild buff target")
                        except:
                            print("invalid buff choice")
                    else:
                        print("\n"*3)
                        print(P2skillChoise,"is not a skill")
                        print("you miss your turn due to your inability to spell a word correctly🤓")
                        print("please correctly type the skill you want to use next time")
                    print("\n"*2)
                    
                    print("\n"*2)
                    
                    if P2attackChoise == "player1" or P2attackChoise == "Player1" or P2attackChoise == P1userName:
                        if P1presetName =="knight":
                            P1reflect = 1 + P1reflectUP
                            DMG = TEMHP - P1newHP
                            P2newHP-= ((P1reflect/100)*DMG)
                            if P2dead =="no" and P2newHP <=0:
                                P2dead ="yes" 
                                P1exp += 4000*P2lv
                                P1score+=400*P2lv
                        if P1block == "yes":
                            DMG = TEMHP - P1newHP
                            recivedDMG = P1blockAmount - DMG
                            if recivedDMG <0:
                                recivedDMG = abs(recivedDMG)
                                TEMHP = TEMHP - recivedDMG
                                print(f"{P1userName} has blocked {DMG} damage and received {recivedDMG} damage this turn")
                            else:
                                print(f"{P1userName} has blocked the attack")
                            
                        else:
                            if P2skillChoise != "heal" and P2skillChoise != "block" and P2skillChoise != "buffer":
                                DMG = abs(TEMHP - P1newHP)
                                if DMG == 0 or DMG == int(0):
                                    DMG ="no"
                                print(f"{P1userName} has taken {DMG} damage this turn" )
                        P1newHP = TEMHP
                        if TEMHP <= 0:
                            
                            if P1dead == "yes":
                                print(f"{TEMuserName} is already dead")
                            elif P1dead == "no":
                                print(f"{P2userName} you have killed {P1userName} and recived {4000*P2lv} experiances")
                                P2exp = P2exp + (4000*P2lv)
                                P1dead = "yes" 
                    if P2attackChoise == "mob" or P2attackChoise == "monster" or P2attackChoise == lvEnemyName:
                        if Eblock == "yes":
                            DMG = TEMHP - lvEnemyHP
                            recivedDMG = P2blockAmount - DMG
                            if recivedDMG <0:
                                recivedDMG = abs(recivedDMG)
                                TEMHP = TEMHP - recivedDMG
                                print(f"{lvEnemyName} has blocked {DMG} damage and received {recivedDMG} damage this turn")
                            else:
                                print(f"{lvEnemyName} has blocked the attack")
                        else:
                            if P2skillChoise != "heal" and P2skillChoise != "block" and P2skillChoise != "buffer":
                                DMG = abs(TEMHP - lvEnemyHP)
                                if DMG == 0 or DMG == int(0):
                                    DMG = "no"
                                print(f"the {lvEnemyName} has taken {DMG} damage this turn" )
                        
                        lvEnemyHP = TEMHP
                        
                        if lvEnemyName =="goblin":
                            Mtype = 40
                        elif lvEnemyName =="dragon":
                            Mtype = 180   
                        if TEMHP <= 0:
                            if Edead == "yes":
                                print(f"{TEMuserName} is already dead")
                            if Edead == "no":
                                print(f"{P2userName} you have killed {lvEnemyName} and recived {Mtype*elv} experiances")
                                P2exp += Mtype*elv
                                Edead = "first" 
                        if P2dead != "yes":
                            if P2onfire =="yes":
                                if P2passiveFIRE == 12:
                                    P2newHP = P2newHP - P12passiveFIREDMG
                                    print(f"{P1userName} causes {P12passiveFIREDMG} passive fire damage on you")
                                    P1exp += 4000*P2lv
                                    P1score+=400*P2lv
                                    if P2newHP <=0:
                                        print(f"the passive fire damage has killed {P2userName} and recived {4000*P2lv} experiances")
                                        P2dead = "yes"
                                elif P2passiveFIRE == 32:
                                    P2newHP = P2newHP - P32passiveFIREDMG
                                    print(f"{lvEnemyName} causes {P32passiveFIREDMG} passive fire damage on you")
                                    if P2newHP <=0:
                                        print(f"the passive fire damage has killed {P2userName}")
                                        P2dead = "yes"
                                P2passiveFireTurn -=1
                                if P2passiveFireTurn == 0:
                                    P2onfire ="no"
                
                    
            turn = "enemy"
            if P22buff == "yes":
                P22buffT -=1
                if P22buffT==0:
                    P22buff == "no"
            if P12buff == "yes":
                P12buffT -=1
                if P12buffT==0:
                    P12buff == "no"
        elif turn == "enemy" :#-------------------------------------------------------------------
            print("\n "*3)
            if lvEnemyHP>0:
                EattackChoise= str(random.randint(1,2))
                
                if EattackChoise == "1":
                    if P1HP >0:
                        totalBuff=1
                        if P11buff == "yes":
                            print(f"buff of {P1buff} on {P1userName} from {P1userName} is effective ")
                            totalBuff=totalBuff*P1buff
                            
                        if P21buff == "yes":
                            print(f"buff of {P2buff} on {P1userName} from {P2userName} is effective")
                            totalBuff=totalBuff*P2buff
                            
                        TEMuserName= P1userName
                        TEMattack = P1attack*totalBuff
                        TEMdefence = P1defence*totalBuff
                        TEMmagic_attack = P1magic_attack*totalBuff
                        TEMmagic_defence = P1magic_defence*totalBuff
                        TEMHP= P1newHP
                    else:
                        print("this choice is already dead you miss your turn")
                        EattackChoise = "null"
                elif EattackChoise == "2":
                    if P2newHP >0:
                        totalBuff=1
                        if P22buff == "yes":
                            print(f"buff of {P2buff} on {P2userName} from {P2userName} is effective ")
                            totalBuff=totalBuff*P2buff
                            
                        if P12buff == "yes":
                            print(f"buff of {P1buff} on {P2userName} from {P1userName} is effective")
                            totalBuff=totalBuff*P1buff
                            
                        TEMuserName= P2userName
                        TEMattack = P2attack*totalBuff
                        TEMdefence = P2defence*totalBuff
                        TEMmagic_attack = P2magic_attack*totalBuff
                        TEMmagic_defence = P2magic_defence*totalBuff
                        TEMHP= P1newHP
                    else:
                        print("this choice is already dead you miss your turn")
                        P1attackChoise = "null"
                else:
                    print("error")
                    EattackChoise="null"
                print(f"{lvEnemyName} choose to attack {TEMuserName}")
                dice = int(random.randint(1,20))
                
                TEMPerception=(TEMmagic_attack+TEMattack)
                EPerception=(Tmagic_Attack+Tphysical_Attack)
                accuracy=((TEMPerception/EPerception)*20)
                print("\n")
                if accuracy >20:
                    accuracy= 20
                print(f"{lvEnemyName} accuracy against the selected enemy is {accuracy}")
                print("\n")
                
                if dice == 20:
                    dmgScale = random.randint(2,10)
                    print(f"the {lvEnemyName} got a 20 on the dice so their attack for this turn is mulriplied by {dmgScale}")
                    Tmagic_Attack = (((lvEnemyMagic_attack*dmgScale) - TEMmagic_defence))
                    Tphysical_Attack = (((lvEnemyAttack*dmgScale) - TEMdefence))
                else:
                    dmgScale=0
                    Tmagic_Attack = (((lvEnemyMagic_attack) - TEMmagic_defence))
                    Tphysical_Attack = (((lvEnemyAttack) - TEMdefence))
                if Tmagic_Attack <= 0:
                    Tmagic_Attack= 1
                if Tphysical_Attack <= 0:
                    Tphysical_Attack= 1
                    
                
                if P23buff == "yes":
                    print(f"buff of {P2buff}")
                    Tmagic_Attack = Tmagic_Attack*P2buff
                    Tphysical_Attack = Tphysical_Attack*P2buff
                    
                if P13buff == "yes":
                    print(f"buff of {P1buff}")
                    Tmagic_Attack = Tmagic_Attack*P1buff
                    Tphysical_Attack = Tphysical_Attack*P1buff
                    
              
                
                fo = random.randint(0,len(Eskills)-1)
                Ehit = Eskills[fo]
                if Ehit == "slash":
                    if accuracy <= dice:
                        we = (Tmagic_Attack/2)                    
                        TEMHP = TEMHP - we
                        EhitT = "hit"
                        
                        
                    else:
                        print(f"the {lvEnemyName} has miss their {Ehit}")
                        print("\n")
                        EhitT = "miss"
                    
                    
                    print("\n")
                elif Ehit == "double_slash":
                    if accuracy <= dice:
                        we = (Tmagic_Attack)                   
                        TEMHP = TEMHP - we
                        EhitT = "hit"
                    else:
                        print(f"the {lvEnemyName} has miss their {Ehit}")
                        print("\n")
                        EhitT = "miss"
                    
                    
                elif Ehit == "mass_slash" :
                    if accuracy <= dice:
                        we = (Tmagic_Attack*2)                    
                        TEMHP = TEMHP - we
                        EhitT = "hit"
                    else:
                        print(f"the {lvEnemyName} has miss their {Ehit}")
                        print("\n")
                        EhitT = "miss"
                    
                    
                    print("\n")
                elif Ehit == "heal" or Ehit == "Heal" or Ehit == str(4):
                        if accuracy <= dice:
                            heal = int(10*elv)
                            print(f"{lvEnemyName} has used healing and healed {heal} hp")
                            lvEnemyHP = lvEnemyHP + heal
                            EhitT = "hit"
                            
                                
                                
                            #else:    
                        else:
                            EhitT = "miss"
                            print(f"there are few existences that can fail to cast a healing skill a pig and {lvEnemyName} congrats")
                elif Ehit == "block" or Ehit == "Block" or Ehit == str(5):
                    Eblock = "yes"
                    EblockStack += 1
                    
                    if lvEnemyMagic_attack > lvEnemyDefence:
                        EblockBase = 1
                    else:
                        EblockBase = 2
                    if EblockBase == "1" :
                        EblockAmount = int(lvEnemyMagic_defence/2)
                        EblockBase = "magic"
                    else:    
                        EblockAmount = int(lvEnemyDefence/2)
                        EblockBase = "normal"
                    
                    print(f"{lvEnemyName} has set a {EblockBase} shield of {EblockAmount}")
                    EhitT = "hit"
                
                
                    
                if EhitT !="miss":  
                    if P1dead !="yes":        
                        if EattackChoise == "1":
                            if P1presetName =="knight":
                                    P1reflect = 1 + P1reflectUP
                                    DMG = TEMHP - P1newHP
                                    lvEnemyHP-= ((P1reflect/100)*DMG)
                                    if Edead =="no" and lvEnemyHP <=0:
                                        Edead ="yes" 
                                        if lvEnemyName =="goblin":
                                            Mtype = 40
                                        elif lvEnemyName =="dragon":
                                            Mtype = 180   
                                        P1exp += Mtype*Elv
                                        P1score+=Mtype
                            if P1block == "yes":
                                DMG = TEMHP - P1newHP
                                recivedDMG = P1blockAmount - DMG
                                if recivedDMG <0:
                                    recivedDMG = abs(recivedDMG)
                                    TEMHP = TEMHP - recivedDMG
                                    print(f"{P1userName} has blocked {P1blockAmount} damage and received {recivedDMG} damage this turn")
                                else:
                                    print(f"{P1userName} has blocked the attack")
                            else:
                                if Ehit != "heal" and Ehit != "block":
                                    DMG = abs(TEMHP - P1newHP)
                                    print(f"DMG is {DMG}")
                                    if DMG == 0 or DMG == int(0):
                                        DMG ="no"
                                    print(f"{P1userName} has taken {DMG} damage this turn" )    
                            P1newHP = TEMHP
                            
                            if TEMHP <= 0:
                                if P2dead == "yes":
                                    print(f"{TEMuserName} is already dead")
                                if P1dead == "no":
                                    print(f"{lvEnemyName} has killed {P1userName}")
                                    P1dead = "first" 
                if EhitT !="miss":  
                    if P2dead !="yes":                    
                        if EattackChoise == "2":
                            if P2presetName =="knight":
                                    P2reflect = 1 + P2reflectUP
                                    DMG = TEMHP - P2newHP
                                    lvEnemyHP-= ((P2reflect/100)*DMG)
                                    if P1dead =="no" and P2newHP <=0:
                                        P1dead ="yes" 
                                        P2exp += 4000*P1lv
                                        P2score+=400*P1lv
                            if P2block == "yes":
                                DMG = TEMHP - P2newHP
                                recivedDMG = P2blockAmount - DMG
                                if recivedDMG <0:
                                    recivedDMG = abs(recivedDMG)
                                    TEMHP = TEMHP - recivedDMG
                                    print(f"{P2userName} has blocked {P2blockAmount} damage and received {recivedDMG} damage this turn")
                                else:
                                    print(f"{P2userName} has blocked the attack")
                            else:
                                if Ehit != "heal" and Ehit != "block":
                                    DMG = abs(TEMHP - P2newHP)
                                    if DMG == 0 or DMG == int(0):
                                            DMG = "no"
                                    print(f"{P2userName} has taken {DMG} damage this turn" )  
                                      
                            P2newHP = TEMHP
                            if TEMHP <= 0:
                                if P2dead == "yes":
                                    print(f"{TEMuserName} is already dead")
                                if P2dead == "no":
                                    print(f"{lvEnemyName} has killed {P2userName}")
                                    P2dead = "first"
                        
                if Edead != "yes":
                    if Eonfire =="yes":
                        if EpassiveFIRE == 13:
                            EHP = EHP - P13passiveFIREDMG
                            print(f"{P1userName} causes {P13passiveFIREDMG} passive fire damage on you")
                            if EHP <=0:
                                if lvEnemyName =="goblin":
                                    Mtype = 40
                                elif lvEnemyName =="dragon":
                                    Mtype = 180   
                                P1exp += Mtype*Elv
                                P1score+=Mtype
                                print(f"the passive fire damage has killed {EuserName} and {P1userName} has recived {Mtype*Elv} experiences")
                                Edead = "yes"
                        elif EpassiveFIRE == 23:
                            EHP = EHP - P23passiveFIREDMG
                            print(f"{P2userName} causes {P23passiveFIREDMG} passive fire damage on you")
                            if EHP <=0:
                                if lvEnemyName =="goblin":
                                    Mtype = 40
                                elif lvEnemyName =="dragon":
                                    Mtype = 180   
                                P2exp += Mtype*Elv
                                print(f"the passive fire damage has killed {EuserName} and {P2userName} has recived {Mtype*Elv} experiences")
                                P2score+=Mtype
                                Edead = "yes"
                        EpassiveFireTurn -=1
                        if P2passiveFireTurn == 0:
                            P2onfire ="no"
            print("\n")
            turn = "P1"
            if P23buff == "yes":
                P23buffT -=1
                if P23buffT==0:
                    P23buff == "no"
            if P13buff == "yes":
                P13buffT -=1
                if P13buffT==0:
                    P13buff == "no"
            
        print(f"{P1userName}:hp is {P1newHP}\n{P2userName}:hp is {P2newHP}\n{lvEnemyName}:hp is {lvEnemyHP}")    
    #    
    if P1newHP <= 0:
        
        print(f"{P1userName} you have died")
    if P2newHP <= 0:
        
        print(f"{P2userName} you have died")    
    if lvEnemyHP <= 0:
        
        print(f"{lvEnemyHP}is died")
    endgame = input("end the battle (yes or no): ")
    
    
    
    x = 0
    co = 1 
    
    
    P1fireT = "first" 
    P2fireT = "first" 
    EfireT = "first" 
saveP = input("do you want to save your gameplay ")
if saveP == "yes":
    if P1projectileUP > 0:
        P1statPoint+= 10*P1projectileUP
    if P2projectileUP > 0:
        P2statPoint+= 10*P2projectileUP
    
    if P1knightUP > 0:
        P1statPoint+= 10*P1knightUP
    if P2knightUP > 0:
        P2statPoint+= 10*P2knightUP
    
    if P1reflectUP > 0:
        P1statPoint+= 10*P1reflectUP
    if P2reflectUP > 0:
        P2statPoint+= 10*P2reflectUP
    
    if P1clericUP > 0:
        P1statPoint+= 10*P1clericUP
    if P2clericUP > 0:
        P2statPoint+= 10*P2clericUP
        
    if P1clericUP > 0:
        P1statPoint+= 10*P1clericUP
    if P2clericUP > 0:
        P2statPoint+= 10*P2clericUP
        
    saveName = input("what is the file name")
    saveName = str(saveName)+".txt"
    file.open(saveName,"w")
    userDataBase = P1userName,P1attack,P1defence,P1magic_attack,P1magic_defence,P1HP,P1lv,P1exp,P1godhood,P1score,"$",P2userName,P2attack,P2defence,P2magic_attack,P2magic_defence,P2HP,P2lv,P2exp,P2godhood,P2score
    userDataBase = str(userDataBase)
    print(userDataBase)
    file.write(userDataBase)
    file.close()
print(f"the scores are P1score:{P1score} \n P2score:{P2score}")
if P1score > P2score:
    print(f"player 1 won")
else:
    print(f"player 2 won")
quit()