import random 
import re
import time
score = 0
beserk = "off"
buff= 1
beff=1 
summoms = 0
summonHP = 0
lenthREMADE = 0 
statPoint = 0 
autoBattle = "no"
losses = 0
restrictSUM = "no"
sumTurn = 1
polo = 0
somoomChange = "first"
temCurrentStats = ""
summonCurrentStats = ""
lv = 1 
auto = -2
Slot =0
souls = 0
exp = 0 
x = 0
elv = 1 
polo = 0
Sturn = "first"
ESturn = "first"
SESturn = "first"
onfire = "no"
complete = "no"
scale = 1
fireT = "first"
gold = 0 
EnewHP = 1
PnewHP = 1
fairTotal = 222
turn = "player"
userName =str(input("please enter your username "))
passwords =input("passwords(first letter of your username)")
Import = input("do you want to load a save, type(yes/no) ")
if Import == "yes" or Import == "y" or Import == "Yes":
    print("\n")
    fileName = str(input("what's you saves name "))
    fileName = fileName +".txt" 
    file = open(fileName,"r")
    file = file.read()
    file = str(file)
    file = file.split("$")
    userpic = str(input("which username are you going to uses old or new. "))
    if userpic == "new":
        saveUserName = userName
    userStat = file[0]
    summonCurrentStats = file[1]

    userStat = str(userStat)
    userStat = userStat.replace("(","")
    userStat = userStat.replace(" ","")
    userStat = userStat.replace("'","")
    userStat = userStat.strip('"')
    userStat = userStat.replace(")","")
    userStat = userStat.strip(" ")
    userStat = userStat.split(",")
    if userpic == "new":
        userStat[0] = saveUserName
    time.sleep(2)
    print("\n"*2)
    
    attack = int(userStat[1])
    defence = int(userStat[2])
    magic_attack = int(userStat[3])
    magic_defence = int(userStat[4])
    HP = int(userStat[5])
    lv = int(userStat[6])
    exp = (userStat[7])
    exp = exp.replace(")","")
    exp = int(exp) 
    
    souls = userStat[8]
    souls = souls.replace("]","")
    souls = int(souls)
    
    boxStats = (userName,attack,defence,magic_attack,magic_defence,HP,lv,exp)
    boxName = ("userName","attack","defence","magic_attack","magic_defence","HP","lv","exp")
    tem = 0 
    for i in boxStats:
        if len(str(i)) > tem:
            tem = len(i) 
    print("these are the imported stats;")        
    print(f"+{'-'*(tem+18)}+")
    for i in range(len(boxStats)):
        outbox = str(f"{boxName[i]}: {boxStats[i]}")
        print(f"|{(outbox).center(tem+18)}|")
    print(f"+{'-'*(tem+18)}+")      
    print(summonCurrentStats)
    
    IMRestart = input("if the stats are correct type yes, if not type no \n")
    if IMRestart == "yes" or IMRestart == "Yes" :
        print("ok great, countinue to play")
    else:
        print("okay the progam will restart, so when you enter the code you have to restart the game from scratch ");
        quit()
    restrictSUM = "YES"
    
else:
    if passwords == "A" or passwords == "a"  and userName == "aiden" or userName == "Aiden":
        print("userName = admin")
        try:
            userName = "admin"
            attack = int(input("what is your numerical attack(intergers/ranging from 1 to ∞)"))
            defence = int(input("what is your numerical defence(intergers/ranging from 1 to ∞)  "))
            magic_attack = int(input("what is your numerical magic attack(intergers/ranging from 1 to ∞)  ")) 
            magic_defence = int(input("what is your numerical magic defence(intergers/ranging from 1 to ∞)  ")) 
            HP= int(input("what is your numerical hp(intergers/ranging from 1 to ∞)  "))
            
            userStats = (userName,attack,defence,magic_attack,magic_defence,HP)
        except:
            complete = "no"
            while complete == "no":
                userName = "admin"
                try:
                    attack = int(input("what ur attack(enter positve  interger) "))
                    defence = int(input("what ur defence (enter positve  interger)"))
                    magic_attack = int(input("what ur magic attack (enter positve  interger)"))
                    magic_defence = int(input("what ur magic defence (enter positve  interger)")) 
                    HP= int(input("what ur hp (enter positve  interger)"))
                    complete= "yes"
                except:
                    continue
            userStats = (userName,attack,defence,magic_attack,magic_defence,HP)
                
         
        print(userStats)
        
    else: 
        while ((fairTotal > 200)):
            informantion= input("do you want a description on the skills (yes/no)")
            while informantion == "yes" or informantion == "y" or informantion == "sure" or informantion == "Sure" or informantion == "yeah" or informantion == "Yeah":
                print("\n")
                print(f"the skills: \n1.lifesteal \n2.slash\n3.eternal flame\n4.necromany\n5.heal\n6.blood sacrifice\nplease wait")
                time.sleep(1)
                inType = input("what skill do you want informantion about(lifesteal/slash/eternal flame/necromany/heal/blood sacrifice")
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
                    print("eternal flame is a flame that stays on the enemy until its death, it does a decent amount of damage if you spam and don't die")
                    print("\n")
                    
                elif inType == "necromancy" or inType == "Necromancy" or inType == "four" or inType == "4" or inType == "Four" :
                    print("\n")
                    print("necromany is a skill what allows you to summon one of your killed enemy into a ally")
                    print("\n")
                elif inType == "blood sacrifice" or inType == "Blood sacrifice" or inType == "six" or inType == "6" or inType == "Six" :
                    print("\n")
                    print("blood sacrifice is a skill that deminishes the effectiveness of your stats by a base of 2 \n in exchage for buffining your summons stats by the multiplier")
                    print("\n")
                elif inType == "heal" or inType == "Heal" or inType == "five" or inType == "5" or inType == "Five":
                    print("\n")
                    print("heal is a skill that allows you to heal a choosen target by a percentage of their maxp hp,it's locked by cap ")
                    print("\n")
                informantion= input("do you want a description on more skills ")
                
            print("\n")
            a='your max stat points must add to a total of 200 or below'
            b="you have 5 different stats to create"
            c="lifesteal and fire affected by magic attack sand slash scales off by attack"
            d="the maximum roll you can recive on the dices is 20"
            e="attack chances are based on magic/attack chance"
            f="these variables need to be lower than the dices roll for you to hit the enemy"
            print(f"{a.center(100)}\n{b.center(100)}\n{c.center(100)}\n{d.center(100)}\n{e.center(100)}\n{f.center(100)}")
            print("\n")
            
            
            complete = "no"
            while complete == "no":
                
                try:
                    StatHelp = 200
                    print("you have 5 stats left")
                    attack = int(input(f"{userName} what is your attack(intergers/ranging from 1 to 199), you have {StatHelp} allocatiion points remaining"))
                    StatHelp -=  attack
                    print("you have 4 stats left")
                    defence = int(input(f"{userName} what is your defence(intergers/ranging from 1 to 199), you have {StatHelp} allocatiion points remaining"))
                    StatHelp -=  defence
                    print("you have 3 stats left")
                    magic_attack = int(input(f"{userName} what is your magic attack(intergers/ranging from 1 to 199), you have {StatHelp} allocatiion points remaining"))
                    StatHelp -=  magic_attack
                    print("you have 2 stats left")
                    magic_defence = int(input(f"{userName} what is your magic defence(intergers/ranging from 1 to 199), you have {StatHelp} allocatiion points remaining")) 
                    StatHelp -=  magic_defence
                    print("you have 1 stats left")
                    HP= int(input(f"{userName} what is your hp(intergers/ranging from 1 to 199), you have {StatHelp} allocatiion points remaining"))
                    print("you have no stats left")
                    
                    userStats = (userName,attack,defence,magic_attack,magic_defence,HP) 
                    print(userStats)

                    for i in range(1,len(userStats)):
                        if abs(int(userStats[i])) != int(userStats[i]):
                            print("don't enter negative")
                            con = int("yes")
                except:
                    continue
                complete= "yes"

            fairTotal =attack+defence+magic_attack+magic_defence+HP 
            informantion= input("do you want a description on the skills ")
            
print("\n")
endgame = "no"
PnewHP = HP
while endgame != "yes":
    goblin = "goblin",17,1,0,8,140
    dragon = "dragon",19,15,1,14,300
    idexEnemy = (goblin,dragon)
    n = random.randint(0,len(idexEnemy)-1)
    enemy = idexEnemy[n]
    lvEnemyName = enemy[0]
    lvEnemyAttack = enemy[1]
    lvEnemyDefence = enemy[2]
    lvEnemyMagic_attack = enemy[3]
    lvEnemyMagic_defence = enemy[4]
    lvEnemyHP =enemy[5]
    while exp >= 2**lv :
        if exp >= 2**lv:
            exp = exp - 2**lv
            lv = lv + 1 
            statPoint = statPoint + 1
    if autoBattle !="no" or autoBattle !="No" or autoBattle !="n" or autoBattle !="N":
        if statPoint >= 1 :
            print("you have ",statPoint,"statPoints")
            statUse = input("do you want to your stat point ")
    
            while statUse == "yes" or statUse == "Yes"  :
                statMany = int(input("how many stat points do u want to use "))
                statChoice = input("what stat do you want increased ")
                if statMany <= statPoint:
    
                    if statChoice == "attack" or statChoice ==  "Attack":
                        attack = attack + (1*statMany) 
                        print(f"(attack is increased by {1*statMany} points)")
                        statPoint = statPoint - (1*statMany)
                    elif statChoice == "defence" or statChoice ==  "defence":
                        defence = defence + (2*statMany)
                        print(f"(defence is increased by {2*statMany} point times)")
                        statPoint = statPoint - (1*statMany)
                    elif statChoice == "magic attack" or statChoice ==  "Magic attack":
                        magic_attack = magic_attack + (2*statMany)
                        magic_defence = magic_defence + (1*statMany)
                        print(f"(magic attack is increased by {2*statMany} and magic defence is increased by {1*statMany} point)",statMany,"times")
                        statPoint = statPoint - (1*statMany)
                    elif statChoice == "magic defence" or statChoice ==  "Magic defence":
                        magic_defence = magic_defence + (3*statMany)
                        print("f(magic_defence is increased by {3*statMany} point times)")
                        statPoint = statPoint - (1*statMany)
                    elif statChoice == "HP" or statChoice ==  "health" or statChoice ==  "Health" :
                        PnewHP = PnewHP + (10*statMany)
                        print(f"(your Health is increased by {10*statMany} point times)")
                        statPoint = statPoint - (1*statMany)
                    else:
                        print("invalid")
                    print("remaining stats points:",statPoint)
                    statUse = input("use more skill points ")
                    print("\n")
        #    
        boxStats = (userName,attack,defence,magic_attack,magic_defence,HP,lv,exp)
        boxName = ("userName","attack","defence","magic_attack","magic_defence","HP","lv","exp")
        tem = 0 
        for i in boxStats:
            if len(str(i)) > tem:
                tem = len(str(i)) 
        print("these are your stats;")        
        print(f"+{'-'*(tem+18)}+")
        for i in range(len(boxStats)):
            outbox = str(f"{boxName[i]}: {boxStats[i]}")
            print(f"|{(outbox).center(tem+18)}|")
        print(f"+{'-'*(tem+18)}+")    
        

        print("\n")
    print("\n")
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
    Eskills = ("slash","double_slash","mass_slash")
    skills = (f"the skills: \n1.lifesteal \n2.slash\n3.eternal flame\n4.necromany\n5.heal")
                
    print("\n")
    
    
    informSkills = ("these are the skill u can use")
    m = (informSkills,skills)
    m= (m)
    c = ("pick a skill;","\n",m)
    
    while lvEnemyHP > 0 and PnewHP > 0 :
        if turn == "player":
            sumTurn = 1
            if losses > 4:
                runDone = input("do u want to end game")
                if runDone != "no"  :
                    trap = "you fell into a ditch and died","you got ganged by monster and was eaten alive","you got robbed of everything and froze to death","the monster from before had poisoned you and you die a painful and long death","i hate deserters so die","as you gain distance from your enemy, you mis-step onto the magic trap you set before hand"
                    UT = random.randint(0,(len(trap)-1))
                    UTrap = trap[UT]
                    print("you successflly ran but",UTrap)
                    quit()
            print("\n"*2)
            if autoBattle == "no":
                askAutoBattle = str(input("do you want to auto battle(y/n)"))
            print("\n")
            #skip this section when autobattle
            if autoBattle == "no":
                if (askAutoBattle =="yes" or askAutoBattle =="Yes" or askAutoBattle =="y" or askAutoBattle =="y") and auto ==-2:
                    autoBattle = askAutoBattle   
                    auto = int(input("type the numbers of turns you want for auto battle(type -1 to battle till death)"))
                    TautoSkill = str(input("enter which skill you want to uses(one skill or multiple skills seaperated by commas to be randomised (or ALL for all))"))
                    if TautoSkill == "all" or TautoSkill == "All" or TautoSkill == "ALL":
                        TautoSkill = ("1,2,3,5,6")
            if autoBattle =="yes" or autoBattle =="Yes" or autoBattle =="y" or autoBattle =="y":
                if ((len(TautoSkill.split(",")))>1):
                    randSkill = random.randint(0,(len((TautoSkill).split(","))-1))
                    autoSkill= (TautoSkill.split(","))[randSkill]
                    print(f"the place holder of the skill ///;{randSkill}")
                    print(f"the skill identifier : {(TautoSkill.split(','))[randSkill]}")
                    
                else:
                    autoSkill= TautoSkill
                if auto > 0:
                    skillChoise = str(autoSkill)
                    auto = auto -1
                    if auto == 0:
                        autoBattle =="no"
                        auto = -2
                elif auto == -1:
                    skillChoise = str(autoSkill)
            else:
                skillChoise = str(input((f"pick a skill from the skills: \n1.lifesteal \n2.slash\n3.eternal flame\n4.necromany\n5.heal\n6.blood sacrifice")))
            """
            try:
                skillChoise = int(skillChoise)
                print("casted")
            except:
                print("cant cast")
            """
            print("\n"*2)
            dice = int(random.randint(1,20))
            percenption = (attack+magic_attack)
            print(f"players perception is {percenption}")
            print (dice,"on the dice")
            time.sleep(3)
            #total acact 
            Tmagic_Attack = ((((magic_attack)/buff) - lvEnemyMagic_defence))
            Tphysical_Attack = ((((attack)/buff) - lvEnemyDefence))
            if Tmagic_Attack < 0:
                Tmagic_Attack= 1
            if Tmagic_Attack < 0:
                Tphysical_Attack= 1
            #perception
            
            EPerception=(lvEnemyMagic_attack+lvEnemyMagic_defence)
            accuracy=int(1/(EPerception/percenption)*20)
            if accuracy >20:
                accuracy = 20
            print(f"{lvEnemyName} accuracy is {accuracy}")




            
            if skillChoise == "lifesteal" or skillChoise == "Lifesteal" or skillChoise == "1":
                if accuracy >= dice:
                    we = (Tmagic_Attack/10)/buff
                    displayVitality= "no"
                    if Sturn == "first":
                        if we > lvEnemyHP:
                            displayVitality= "yes"
                            statPoint = statPoint - 1
                        lvEnemyHP = lvEnemyHP - we
                        PnewHP = HP + we
                        print ("dice",dice)
                        turn = "enemy"
                    else :
                        if we > lvEnemyHP:
                            displayVitality= "yes"
                            
                        lvEnemyHP = lvEnemyHP - we
                        
                        PnewHP = PnewHP + we
                    Sturn = "second"
                    print("\n")
                    print(f"the effetiveness of your attacks are decreased by {buff}")
                    print("the enemy lost",we,"HP")
                    print("you gained",we,"HP")
                    if displayVitality== "yes":
                        print("the additonal vitlity is gained from the environment at the cost of enraging the environment");
                        displayVitality= "no"
                else :
                    print("player has missed")
                    losses = losses + 1
                skillChoise = "null"
                turn = "enemy"

            elif skillChoise == "slash" or skillChoise== "Slash" or skillChoise== str("2") :
                if accuracy <= dice:
                    we = (Tphysical_Attack/2)/buff
                    print(f"the effetiveness of your attacks are decreased by {buff}")
                    if Sturn == "first":
                        lvEnemyHP = lvEnemyHP - we
                    else :
                        lvEnemyHP = lvEnemyHP - we
                    Sturn = "second"
                    print("\n")
                    print("you do",we,"physical damage from a slash ")
                    print("\n")
                    turn = "enemy"
                else:
                    print("player has missed")
                    turn = "enemy"
                    losses = losses + 1
                skillChoise = "null"
                print("\n")

            elif skillChoise == "eternal flame" or skillChoise =="Eternal flame" or skillChoise == str("3"):
                if percenption <= dice:
                    if fireT == "second":
                        fdamage = int((Tmagic_Attack/10)/buff)
                        lvEnemyHP = lvEnemyHP - (fdamage)
                        print("the enemy took",fdamage * scale," fire damage")
                        if fireskill == "eternal flame" or fireskill == "Eternal flame"or fireskill == 3:
                            scale = scale +1 
                            lvEnemyHP = lvEnemyHP - (fdamage * scale)
                            print("the enemy took",fdamage * scale,"extra fire damage")
                        lvEnemyHP = lvEnemyHP - (fdamage/2)
                    elif fireT == "first":
                        fdamage = int(Tmagic_Attack/3)
                        if ESturn == "first":
                            lvEnemyHP = lvEnemyHP - fdamage
                            ESturn = "second"
                        elif ESturn == "second" :
                            lvEnemyHP = lvEnemyHP -fdamage
                        fireT = "second"
                        print("the enemy lost",fdamage,"HP")
                        fireskill = skillChoise
                        onfire = "yes"
                else:
                    losses = losses + 1
                    print("player has missed")
            elif skillChoise == "necromancy" or skillChoise =="Necromancy" or skillChoise == str("4"):
                
                if souls > 0 :
                    #the code to make summons
                    summonInput = ("you have ",souls,"souls do you want to make summons (yes or no)")
                    summoning = input(summonInput)
                    
                    
                    if summoning == "yes" or summoning == "Yes":
                        print("\n"*2)
                        if Import == "yes" or Import == "Yes":
                            try:
                                manysSummonName = summonSaveName
                                manysSummonAttack = summonSaveAttack
                                manysSummonDefense = summonSaveDefense
                                manysSummonMagic_attack = summonSaveMagic_attack
                                manysSummonMagic_Defense = summonSaveMagic_defense
                                manysSummonHP = summonSaveHP
                                dishing =manysSummonName,manysSummonAttack,manysSummonDefense,manysSummonMagic_attack,manysSummonMagic_Defense,manysSummonHP
                                dishing = str(dishing)
                                summonCurrentStats = summonCurrentStats + dishing
                                summonCurrentStats = summonCurrentStats + "@"
                                souls = souls - 1
                                restrictSUM = "YES"
                                
                            except:
                                print("you need to gain a corpse to summon")
                        else:
                            try:
                                manysSummonName = str(summonSaveName)
                                manysSummonAttack = int(summonSaveAttack)
                                manysSummonDefense = int(summonSaveDefense)
                                manysSummonMagic_attack = int(summonSaveMagic_attack)
                                manysSummonMagic_Defense = int(summonSaveMagic_defense)
                                manysSummonHP = int(summonSaveHP)
                                dishing =manysSummonName,manysSummonAttack,manysSummonDefense,manysSummonMagic_attack,manysSummonMagic_Defense,manysSummonHP
                                dishing = str(dishing)
                                for dishing in summonCurrentStats:
                                    carsdr = int("fail")
                                print("dishing: \n",dishing)
                                summonCurrentStats = str(summonCurrentStats)
                                summonCurrentStats = summonCurrentStats + dishing
                                summonCurrentStats = summonCurrentStats + "@"
                                souls = souls - 1
                                restrictSUM = "YES"
                                
                                
                            except:
                                print("you need to gain a corpse to summon")
                        
                    #the code to upgrade summons is here, its a loop
                    print("\n"*2)
                    if lenthREMADE > 0 :
                        upgradeSUmmons = input("do you want to uses souls to refine your summons?")
                        while upgradeSUmmons == "yes" or upgradeSUmmons == "Yes":
                            try:
                                print("you have",souls,"souls")
                                
                                sacrifice= input("do you want to convert statPoints into souls");
                                while sacrifice == "yes" or sacrifice == "Yes" or sacrifice == "Y" or sacrifice == "y":
                                    
                                    boxStats = (userName,attack,defence,magic_attack,magic_defence,HP,lv,exp)
                                    boxName = ("userName","attack","defence","magic_attack","magic_defence","HP","lv","exp")
                                    tem = 0 
                                    for i in boxStats:
                                        if len(str(i)) > tem:
                                            tem = len(i) 
                                    print(f"{userName} current stats;");     
                                    print(f"+{'-'*(tem+18)}+")
                                    for i in boxStats:
                                        outbox = str(f"{boxName[i]}: {boxStats[i]}")
                                        print(f"|{(outbox).center(tem+18)}|")
                                    print(f"+{'-'*(tem+18)}+")
                                    print("\n")
                                    chooseSACRstat = input("which stat do you want to sacrifice?");
                                    if chooseSACRstat == "attack" or chooseSACRstat == "Attack":
                                        mainPAIN = input("how many point are you willing to part with");
                                        attack = attack - manyPAIN
                                    if chooseSACRstat == "defence" or chooseSACRstat == "Defence":
                                        mainPAIN = input("how many point are you willing to part with");
                                        defence = defence - manyPAIN
                                    if chooseSACRstat == "magic attack" or chooseSACRstat == "Magic attack" or chooseSACRstat == "Magic Attack":
                                        mainPAIN = input("how many point are you willing to part with");
                                        magic_attack = magic_attack - manyPAIN
                                    if chooseSACRstat == "magic defence" or chooseSACRstat == "Magic defence" or chooseSACRstat == "Magic Defence":
                                        mainPAIN = input("how many point are you willing to part with");
                                        magic_defence = magic_defence - manyPAIN
                                    if chooseSACRstat == "HP" or chooseSACRstat == "health":
                                        mainPAIN = input("how many point are you willing to part with");
                                        HP = HP - manyPAIN
                                else:
                                    soooooooooo= int("car")
                            except:
                                print("wrong type of input so please try again later")
                                sacrifice= input("do you want to convert statPoints into souls")
                                while sacrifice == "yes" or sacrifice == "Yes":
                                    chooseSACRstat = input("which stat do you want to sacrifice?(health is in the ration of 10 for 1 soul))");
                                    print("current stats;")
                                    print("Name",userName)
                                    print("attack",attack)
                                    print("defence",defence) 
                                    print("magic_attack",magic_attack)  
                                    print("magic_defence",magic_defence)
                                    print("HP",HP)
                                    try:
                                        if chooseSACRstat == "attack" or chooseSACRstat == "Attack":
                                            mainPAIN = int(input("how many point are you willing to part with"));
                                            attack = attack - manyPAIN
                                        elif chooseSACRstat == "defence" or chooseSACRstat == "Defence":
                                            mainPAIN = int(input("how many point are you willing to part with"));
                                            defence = defence - manyPAIN
                                        elif chooseSACRstat == "magic attack" or chooseSACRstat == "Magic attack" or chooseSACRstat == "Magic Attack":
                                            mainPAIN = int(input("how many point are you willing to part with"));
                                            magic_attack = magic_attack - manyPAIN
                                        elif chooseSACRstat == "magic defence" or chooseSACRstat == "Magic defence" or chooseSACRstat == "Magic Defence":
                                            mainPAIN = int(input("how many point are you willing to part with"));
                                            magic_defence = magic_defence - manyPAIN
                                        elif chooseSACRstat == "HP" or chooseSACRstat == "health":
                                            mainPAIN = int(input("how many point are you willing to part with"));
                                            HP = HP - manyPAIN
                                        souls = souls + manyPAIN   
                                    except:
                                        print("")
                                    sacrifice= input("do you still want to convert statPoints into souls(y/n)")
                            
                            
                                    
                                
                            
                            soulUpgradeUse = int(input("how many souls do you want to use?"));    
                            if soulUpgradeUse <= souls:
                                nre = 0
                                print("\n"*2)
                                print(f"copy and paste from here \n{summonCurrentStats}")
                                try:
                                    print("\n"*2)
                                    summonPUpgrade = input("what summon do you want to upgrade?(enter all from the name of the summon to the @ with it included");
                                    newSummonPUpgrade = summonPUpgrade
                                    while nre != soulUpgradeUse:
                                        sumUP = random.randint(1,5)
                                        newSummonPUpgrade = newSummonPUpgrade.split(",")
                                        if sumUP == 1 :
                                            newSummonPUpgrade[1] = int(newSummonPUpgrade[1]) + 2
                                            newSummonPUpgrade[2] = int(newSummonPUpgrade[2]) + 1
                                            print("yours summons attack is increased by 2 and its defence is increased by 1")
                                        elif sumUP == 2 :
                                            newSummonPUpgrade[2] = int(newSummonPUpgrade[2]) + 4
                                            print("yours summon Defence is increased by 4")
                                        elif sumUP == 3 :
                                            newSummonPUpgrade[3] = int(newSummonPUpgrade[3]) + 3
                                            newSummonPUpgrade[4] = int(newSummonPUpgrade[4]) + 1
                                            print("yours summon Magic attack is increased by 3 and its Magic Defence is increased by 1")
                                        elif sumUP == 4 :
                                            newSummonPUpgrade[4] = int(newSummonPUpgrade[4]) + 5
                                            print("yours summon Magic Defence is increased by 3")
                                        elif sumUP == 5 :
                                            reAmpOFSHP = str(newSummonPUpgrade[5])
                                            print(reAmpOFSHP)
                                            time.sleep(2)
                                            reAmpOFSHP = reAmpOFSHP[:-1]
                                            reAmpOFSHP = int(reAmpOFSHP) + 3
                                            newSummonPUpgrade[5] = reAmpOFSHP
                                            newSummonPUpgrade[5] = str(newSummonPUpgrade[5]) + "@"
                                            print("yours summon HP is increased by 5(YOUR SUMONS HP DOESN'T MATTER they have no agroo)")
                                        nre = nre + 1
                                        souls = souls - 1 
                                    
                                    
                                      
                                    print("\n"*2)
                                    newSummonPUpgrade = str(newSummonPUpgrade)
                                    newSummonPUpgrade = str(newSummonPUpgrade)
                                    newSummonPUpgrade = newSummonPUpgrade.strip(")")
                                    newSummonPUpgrade = newSummonPUpgrade.strip("(")
                                    newSummonPUpgrade = newSummonPUpgrade.strip("(")
                                    newSummonPUpgrade = newSummonPUpgrade.strip(")")
                                    newSummonPUpgrade = newSummonPUpgrade.replace(")","")
                                    newSummonPUpgrade = newSummonPUpgrade.replace("'","")
                                    newSummonPUpgrade = newSummonPUpgrade.replace("[","")
                                    newSummonPUpgrade = newSummonPUpgrade.replace("]","")
                                    newSummonPUpgrade = newSummonPUpgrade.replace("'","")
                                    newSummonPUpgrade = newSummonPUpgrade.replace("(","")
                                    newSummonPUpgrade = newSummonPUpgrade.replace(" ","")
                                    summonCurrentStats = summonCurrentStats.replace(summonPUpgrade,newSummonPUpgrade)
                                    
                                except:
                                    print("couldn't upgrade ur summon so i will give you back your souls")
                            print("you have",souls,"souls left")
                            upgradeSUmmons = input("do you want to uses more souls to upgrade your summons?")
                        #the code to kill summons
                    print("\n"*2)
                    summonKill = input("do you want to kill your summon(killing a summon breaks the system \n as it makes the last summon the current summon)")
                    while summonKill == "yes" or summonKill == "Yes":
                        
                        try:
                            print(summonCurrentStats)
                            PKSummonKill = input("what summon do you want to kill(enter from the the summons name to the next name,it includes @")
                            
                            poSearch = "not found"
                            n = 0 
                            #checker to delete polo 
                            while poSearch != "found":
                                if summonCurrentStats[n] != PKSummonKill:
                                    n = n + 1
                                    poSearch = "not found"
                                else:
                                    poSearch = "found"
                                    #checker to delete polo end
                                    #if n >= polo :
                                    #polo = polo - 1
                                        
                                    #fix
                                    sumTurn = sumTurn - 1 
                                     
                                    
                                    summonCurrentStats.remove(PKSummonKill)
                                    print("\n")
                                    killer = "you, so painfull drowned your summon that even then enemy was stunned","you shot your summon","you disintegrate your summon ","you fed the monster from before your summon","you are now labeled a murderer","you gain distance from your enemy and you force your summon onto the magic trap you set beforehand,\n causing it to explode"
                                    randomKill = random.randint(0,(len(killer)-1))
                                    playerKill= killer[randomKill]
                                    print(playerKill)
                                    time.sleep(4)
                        except:
                            print("you need to enter a summon")
                            print(summonCurrentStats)
                        summonKill = input("do you want to kill your summon still?")
                
                else:
                    print("You don't have enough souls")
                
                try:
                        
                    print("\n \n \n summon stats automatic checkup ")
                    print(summonCurrentStats)
                    print(len(temuCurrentStats.split("@")),": is the number of summons you have")
                except:
                    print("you don't have any summons, so there is nothing in the database")
            elif skillChoise == "heal" or skillChoise == "Heal" or skillChoise == str(5):
                if accuracy <= dice:
                    heal = int(hp/2.5)
                    print(f"healing used, you healed {heal}")
                    if PnewHP > HP:
                        PnewHP = hp
                        print(f"you were unable to reach godhood, your hp is capped")
                    if Sturn == "first":
                        PnewHP = hp 
                        print ("dice",dice)
                    else :
                        PnewHP = PnewHP + heal
                else:
                    print(f"there are few existences that can fail to cast a healing skill a pig and {userName} congrats")
            #new skill that allow enable summons to go beserk with double damage and player will recieve half 
            elif skillChoise == "blood sacrifice" or skillChoise == "Blood sacrifice" or skillChoise == str(6):
                print("blood sacrifice used")
                print(f"beserk{buff}")
                print(f"statPoint {statPoint}")
                print(f"beserk is{beserk}")
                beupgrade= input("do you want to upgrade beserk for 10 statPoints or to toggle beserk(1.upgrade/2.toggle)")
                if beupgrade == "upgrade" or beupgrade == "Upgrade" or beupgrade == "u" or beupgrade == 1:
                    if statPoint>=10:
                        statPoint-=10
                        beff+=1
                    print(f"the effectiveness of berserk is now {buff}")
                    
                elif beupgrade == "toggle" or beupgrade == "Toggle" or beupgrade == "t" or beupgrade == 2:
                    if beserk == "on":
                        buff=beff
                        beserk = "off"
                    else:
                        buff=1
                        beserk = "on"
                else:
                    print("wasted turn")
            else:
                print("\n"*3)
                print(skillChoise,"is not a skill")
                print("you miss your turn due to your inability to spell a word correctly🤓")
                print("please correctly type the skill you want to use next time")
                            
            print("\n")
            if onfire != "no":
                lvEnemyHP = lvEnemyHP - ((magic_attack/15)*scale)
                fdamage = ((magic_attack/15)*scale)
                print("the enemy took",fdamage,"passive fire damage")
            turn = "enemy"
            print("the enemy hp  is currently on ",lvEnemyHP)
            print("your hp  is currently on ",PnewHP)
            print("\n")
        elif turn == "enemy" :
            percenption = (attack+magic_attack)
            EPerception=(lvEnemyMagic_attack+lvEnemyAttack)
            accuracy=int(1/(percenption/EPerception)*20)
            
            if accuracy >20:
                accuracy = 20
            print(f"{lvEnemyName} accuracy is {accuracy}")
            lot = 0
            fo = random.randint(0,len(Eskills)-1)
            Ehit = Eskills[fo]
            if Ehit == "slash":
                if accuracy <= dice:
                    we = (lvEnemyAttack/2)*buff
                    if ESturn == "first":
                        PnewHP = HP - we
                        print(PnewHP)
                    else :
                        PnewHP = PnewHP - we
                    ESturn = "second"
                    print("\n")
                    lot = lot + 1
                    print(lot,"the player took",we,"damage")
                    print("\n")
                    turn = "summon"
                else:
                    print("\n")
                    lot = lot + 1
                    print(lot,"the enemy miss their attack")
                    print("\n")
                    turn = "summon"
                skillChoise = "null"
                turn = "summon"
                print("\n")
            elif Ehit == "double_slash":
                if accuracy <= dice:
                    we = (lvEnemyAttack)*buff
                    if ESturn == "first":
                        PnewHP = HP - we
                        print(PnewHP)
                    else :
                        PnewHP = PnewHP - we
                    ESturn = "second"
                    print("\n")
                    lot = lot + 1
                    print(lot,"the player took",we,"damage from a double slash")
                    print("\n")
                    turn = "summon"
                else:
                    print("\n")
                    lot = lot + 1
                    print(lot,"the enemy miss their attack")
                    print("\n")
                    turn = "summon"
                skillChoise = "null"
                turn = "summon"
            elif Ehit == "mass_slash" :
                if accuracy <= dice:
                    we = (lvEnemyAttack*2)*buff
                    if ESturn == "first":
                        PnewHP = HP - we
                        print(PnewHP)
                    else :
                        PnewHP = PnewHP - we
                    ESturn = "second"
                    print("\n")
                    lot = lot + 1
                    print(lot,"the player took",we,"damage from a miracle slash")
                    print("\n")
                    turn = "summon"
                else:
                    print("\n")
                    lot = lot + 1
                    print(lot,"the enemy miss their attack")
                    print("\n")
                    turn = "summon"
                skillChoise = "null"
                turn = "summon"
                print("\n")
            print(f"your hp  is currently on {PnewHP} and max hp of {HP}" )
            time.sleep(2)
            
        elif turn == "summon":
            if Import == "yes" or Import == "Yes":
                summonCurrentStats = summonCurrentStats.strip(")")
                summonCurrentStats = summonCurrentStats.strip("(")
                summonCurrentStats = summonCurrentStats.replace("'","")
                temCurrentStats = summonCurrentStats.split("@")
                temCurrentStats = temCurrentStats[polo]
                temCurrentStats = temCurrentStats.split(",")
                summonName = str(temCurrentStats[0])
                summonAttack = int(temCurrentStats[1])
                summonDefense = int(temCurrentStats[2])
                summonMagic_attack = int(temCurrentStats[3])
                summonMagic_Defense = int(temCurrentStats[4])
                summonHP = int(temCurrentStats[5]) 

                lenthIMPORT = len((summonCurrentStats.split("@")))
                lenthIMPORT = lenthIMPORT - 1
                #nono = polo + 1
                #try:
                #lenthIMPORT = len(fixSummons)
                #if nono != lenthIMPORT:
                #polo = polo + 1
                #except:
                #if nono != lenthREMADE :
                #polo = polo + 1
                
            else:
                if restrictSUM == "YES" :
                    summonCurrentStats = str(summonCurrentStats)
                    summonCurrentStats = summonCurrentStats.strip(")")
                    summonCurrentStats = summonCurrentStats.strip("(")
                    summonCurrentStats = summonCurrentStats.strip("(")
                    summonCurrentStats = summonCurrentStats.strip(")")
                    summonCurrentStats = summonCurrentStats.replace(")","")
                    summonCurrentStats = summonCurrentStats.replace("'","")
                    summonCurrentStats = summonCurrentStats.replace("[","")
                    summonCurrentStats = summonCurrentStats.replace("]","")
                    summonCurrentStats = summonCurrentStats.replace("'","")
                    summonCurrentStats = summonCurrentStats.replace("(","")
                    summonCurrentStats = summonCurrentStats.replace(" ","")
                    
                    try:
                        temuCurrentStats = ((summonCurrentStats.split("@")).remove(" "))
                    except:
                        temuCurrentStats = (summonCurrentStats.split("@"))
                    
                    print(f"temuCurrentStats all summons{temuCurrentStats}")
                    
                    domuCurrentStats = temuCurrentStats[polo]
                    print("polo",polo)
                    print("domuCurrentStats",domuCurrentStats)
                    domuCurrentStats = domuCurrentStats.split(",")
                    
                    summonName = (domuCurrentStats[0])
                    summonAttack = int(domuCurrentStats[1])
                    summonDefense = int(domuCurrentStats[2])
                    summonMagic_attack = int(domuCurrentStats[3])
                    summonMagic_Defense = int(domuCurrentStats[4])
                    summonHP = int(float(domuCurrentStats[5]))
                    nono = polo + 1
                    
                    
                    lenthIMPORT = len((summonCurrentStats.split("@")))
                    lenthIMPORT = lenthIMPORT - 1

                    print("cheker daily")
                    print("summonName")
                    print("summonAttack")
                    print("summonDefense")
                    print("summonMagic_attack")
                    print("summonMagic_Defense")
                    print("summonHP")

            

            

            

                    
                    #if  > 0 : 
                    #lenthREMADE = lenthREMADE - 1
                    #nono = polo + 1
                    #try:
                    #lenthIMPORT = len(fixSummons)
                    #if nono != lenthIMPORT:
                    #polo = polo + 1
                    #except:
                    #if nono != lenthREMADE :
                    #polo = polo + 1
                        
                    
                    
            
            
            
            if summonHP > 0:
                summonPercenption = (summonAttack+summonMagic_attack)
                EPerception=(lvEnemyMagic_attack+lvEnemyMagic_defence)
                accuracy=int(1/(EPerception/percenption)*20)
                if accuracy >20:
                    accuracy = 20
                print(f"{lvEnemyName} accuracy is {accuracy}")
                
                print(f"your summons attacks recieve a buff/multiplier of {buff}")
                Sfo = random.randint(0,len(Eskills)-1)
                SEhit = Eskills[fo]
                TSEmagic_Attack = (((summonMagic_attack*buff)- lvEnemyMagic_defence))*1
                TSEphysical_Attack = (((summonAttack*buff) - lvEnemyMagic_attack))*1
                if TSEmagic_Attack < 0:
                    TSEmagic_Attack= 1
                if TSEphysical_Attack < 0:
                    TSEphysical_Attack= 1
                
                Sdice = int(random.randint(1,20))
                if SEhit == "slash":
                    if summonPercenption <= Sdice:
                        Swe = (TSEphysical_Attack/2)*buff
                        if SESturn == "first":
                            lvEnemyHP = lvEnemyHP - Swe
                        else :
                            lvEnemyHP = lvEnemyHP - Swe
                        SESturn = "second"
                        print("\n")
                        Slot = Slot + 1
                        print(Slot,"the ENEMY took",Swe,"damage from your summon slash attack")
                        print("\n")
                        turn = "player"
                    else:
                        print("\n")
                        Slot = Slot + 1
                        print(Slot,"your summon miss its attack")
                        print("\n")
                        turn = "player"
                    turn = "player"
                    print("\n")
                elif SEhit == "double_slash":
                    if summonPercenption <= Sdice:
                        Swe = TSEphysical_Attack*buff
                        if SESturn == "first":
                            lvEnemyHP = lvEnemyHP - Swe
                        else :
                            lvEnemyHP = lvEnemyHP - Swe
                        SESturn = "second"
                        print("\n")
                        Slot = Slot + 1
                        print(f"{Slot},the enemy took {Swe} damage from your summon's double slash")
                        print("\n")
                        turn = "player"
                    else:
                        print("\n")
                        Slot = Slot + 1
                        print(Slot,"your summon miss it's attack")
                        print("\n")
                        turn = "player"
                    skillChoise = "null"
                    turn = "player"
                elif SEhit == "mass_slash" :
                    if summonPercenption <= dice:
                        Swe = (TSEphysical_Attack*2)*buff
                        if SESturn == "first":
                            lvEnemyHP = lvEnemyHP - Swe
                        else :
                            lvEnemyHP = lvEnemyHP - Swe
                        SESturn = "second"
                        print("\n")
                        Slot = Slot + 1
                        print(f"{Slot},the enemy took {Swe} damage from your summon miracle slash")
                        print("\n")
                        turn = "player"
                    else:
                        print("\n")
                        Slot = Slot + 1
                        print(Slot,"the summon miss their attack")
                        print("\n")
                        turn = "player"
                    skillChoise = "null"
                    turn = "player"
                    print("\n")
                time.sleep(2)
            
            try:
                if restrictSUM == "YES":
                    if sumTurn != lenthIMPORT:
                        print(lenthIMPORT,"is lengthimport")
                        print("sumTurn",sumTurn)
                        
                        sumTurn = sumTurn + 1
                        polo = polo + 1 
                        turn = "summon"
                    else:
                        turn = "player"
                        slot = 0 
                        polo = 0
                        sumTurn = 1
            except:
                print("error on 746 or non more summons, overflow")
            turn = "player"
    print("\n")
    if lvEnemyHP <= 0:
        
        print(userName,"you won the battle against a",enemy[0])
        if  enemy[0] == "goblin":
            score +=1 
            exp = exp + (40*lv)
            souls = souls + 1
        elif enemy[0] == "dragon":
            score +=10
            exp = exp + (180*lv)
            souls = souls + 1
            
        summonSaveName = lvEnemyName
        summonSaveAttack = lvEnemyAttack
        summonSaveDefense = lvEnemyDefence
        summonSaveMagic_attack = lvEnemyMagic_attack
        summonSaveMagic_defense = lvEnemyMagic_defence
        summonSaveHP = SMaxHP
        time.sleep(2)
        print("\n"*5)
        print("this is stats of the current corpse you have(u cant have multiple corpes due to ur inability to carry them")
        print(summonSaveName,"summonSaveName")
        print(summonSaveAttack,"summonSaveAttack")
        print(summonSaveDefense,"summonSaveDefense")
        print(summonSaveMagic_attack,"summonSaveMagic_attack")
        print(summonSaveMagic_defense,"summonSaveMagic_defense")
        print(summonSaveHP,"summonSaveHP")
        print("\n"*5)
    elif PnewHP <= 0:
        print("game over")
        print(userName,"you f-fool how could u die to a inferior ",enemy[0])
        quit()
    if autoBattle == "yes" or autoBattle == "Yes" or autoBattle == "y" or autoBattle == "Y":
        endgame = "no"
    else:
        endgame = input("end the battle (yes or no): ")
    print("")
    
    polo = 0 
    sumTurn = 1
    x = 0
    co = 1 
    polo = 0
    losses = 0
    turn == "player"
    onfire = "no"
    fireskill = "null"
    scale = 1
    fireT = "first" 
saveP = input("do you want to save your character ")
if saveP == "yes":
    saveName = input("enter your save name ")
    saveName = str(saveName +".txt")
    file = open(saveName,"w")
    userDataBase = userName,attack,defence,magic_attack,magic_defence,PnewHP,lv,exp,souls
    userDataBase = str(userDataBase)
    print(userDataBase)
    file.write(userDataBase)
    file.write("$")
    file.write(summonCurrentStats)
    file.close()
print(f"your score is {score}")
quit()