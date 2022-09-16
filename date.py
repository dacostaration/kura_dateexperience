# Application:  A Date To Remember
# Author:       RDC
# ------------
# TEST CODE
# create a concatenated string from 0 to 19 (e.g. "012..1819")
# nums = [str(n) for n in range(20)]
# print("".join(nums))

# Date Design
# Objective:    Have the program accumulate points by 
# Must haves:   
# 1. user must be greeted
# 2. user must be presented with a menu [food + drink]
# 3. user must be served drinks
# 4. user must be served food
# 5. user must be presented with the bill

import time
import random
from tkinter import Y 

testScore:True          #....used to print info to the console when testing the application
w="[waiter]: "
badWaiterLimit=0        #....this is the number of tries before the waiter loses patience and does something bad to terminate your visit
cost=0.00
surveysTaken=0
surveyScore=0
experienceRating=0
receipt={
    'appetizer':{},
    'main':{},
    'side':{},
    'desert':{},
    'drinks':{}
}
questionSequence=['greet','seating_ask','menu_ask_drink','order_drink','serve_drink','inquiry',
            'menu_ask_appetizer', 'menu_ask_main', 'menu_ask_side', 'oder_food', 'inquiry','menu_ask_drink','order_drink','inquiry',
            'serve_food', 'inquiry', 'menu_ask_desert', 'order_desert', 'serve_desert', 'inquiry', 'bill', 'bye']
lastQuest=""
set_seating=""
set_drinks=""
set_food_appetizer=""
set_food_main=""
set_food_desert=""

def timeRand(min,max):
    mins = random.randint(min, max)
    return mins

def validate(qtype, qtype2, ans):
    #print("qtype:"+qtype+", qtype2:"+qtype2+", ans:"+ans)
    itm=waiter(qtype,qtype2) 
    c=itm[ans]
    #print("cost:"+c)
    return c


def waiter(qtype, qtype2):
    # match (qtype):    <-- this is Python 10 [current version = 3.9.7]
    #print("qtype:"+qtype)
    #print("qtype2:"+qtype2)
    w="\n[waiter]: "
    if qtype == "greet":
        q = ['Good evening!', 'Welcome to The Monty Pyton!', 'Hello there! Welcome to PyDot!']
        return random.choice(q)
    elif qtype == 'seating':
        if qtype2 == 'options':
            return ['inside','outside']
        else:
            s = {'inside':{'bar','booth','table'}, 'outside':{'deck','balcony'}}
            return s[qtype2]
        
    elif qtype == "menu_ask":
        #return 'Would you like to see the menu? [y/n]'
        return 'Would you like to see the '+qtype2+' menu? [y/n]: '
    elif qtype == "menu_drinks":
        if qtype2 == 'options':
             return ['beer','scotch','rum','cocktail','water']
        else:
            m = {'beer':{"heineken":9.99,"guinness":9.99,"budweiser":5.99,"saporo":12.00,
                    "stella artois":11.00,"corona":9.00,"dos equis":10.00,"modelo":10.00},
                'scotch':{"johnny walker blue":45.00,"johnny walker double black":30.00,"glenfiddich":22.00,"the glenlivet":24.00},
                'rum':{"malibu":7.00,"10 to 1":12.00,"appleton estate":15.00,"angostura 1919":17.00,"bacardi":12.00},
                'cocktail':{"long island ice tea":12.00,"mojito":14.00,"caipirinha":15.00,"scotch and coconut":11.00},
                'water':{"flat":2.00,"sparkling":4.00}
                }
            return m[qtype2]
    elif qtype == 'menu_food':
        m = {'appetizer':{"crab cakes":14.00,"clam chowder":13.00,"tomato bisque":9.00,"skip":0},
                "main":{"lobster":24.00,"shrimp":21.00,"scallops":22.00,"steak":23.00,"vegetarian steak":99.00}, 
                "side":{"rice":5.00,"potatoes":8.00,"fries":4.00,"mushrooms":4.00,"asparagus":3.00,"corn":7.00},
                "desert":{"vanilla ice-cream":10.00,"raspberry sorbet":12.00,"skip":0}}
        return m[qtype2]
    elif qtype == "order_drinks":
        return w+""
    elif qtype == "order_food":
        return w+""
    elif qtype == "serve_drinks":
        return w+""
    elif qtype == "serve_food":
        return w+""
    elif qtype == "bill":
        return w+""

    # If an exact match is not confirmed, this last case will be used if provided
    else:
        return w+"Something's wrong with the internet"

def showDateResult():
    global experienceRating, surveysTaken
    expThreshold=random.choice(['Easy Going','Expensive Taste','High Maintenance'])
    if expThreshold == 'Easy Going':
        descriptor='is'
        threshold=surveysTaken*2      # your date's experience threshold = 2 x max surveys taken
        dollarthreshold=9*4         # [cheap date] only $5 * the number of available courses [appetizer, main, side, desert]
    elif expThreshold == 'Expensive Taste':
        descriptor='has'
        threshold=surveysTaken*3      # your date's experience threshold = 3 x max surveys taken
        dollarthreshold=15*4         # [medium expensive date] only $5 * the number of available courses [appetizer, main, side, desert]
    else: # High Maintenance
        descriptor='is'
        threshold=surveysTaken*4      # your date's experience threshold = 4 x max surveys taken
        dollarthreshold=25*4         # [expensive date] only $5 * the number of available courses [appetizer, main, side, desert]
        
    print(">> Your overall experience rating was ["+str(experienceRating)+"]")
    print(">> Looks like your date "+descriptor+" "+expThreshold)
    if cost < dollarthreshold: 
        dateRes='bad'
        print(">> However, your low spend made them feel super cheap!")
        if experienceRating >= threshold: 
            print(">> They did have a good experience though.")     #.....experience outweighs money any day!
            dateRes='good'
        else:
            print(">> They also didn't seem to have a good time.")
            dateRes='bad'
    else:
        dateRes='good'
        print(">> To them, they were treated as if money was no object!")
        if experienceRating >= threshold: 
            print(">> They also had a great experience.")     
            dateRes='good'
        else:
            print(">> They did not have seem to have a good time though.")  #.....experience outweighs money any day!
            dateRes='bad'

    if dateRes == 'bad':
        datePhrase = random.choice([">> Sorry to say...it ain't happenin' again!","No second date in your future it seems.", "Your future looks lonely!"])
    else: 
        datePhrase = random.choice([">> Lucky Duck! You scored a second date!","Well, well, well...you did swell! You'll be seeing each other again.", "Well done! A second date is certain!"])
    print(">> "+datePhrase)
        

def badWaiterSnap():
    bws=random.choice(["What's taking so long??","Would you like to order today?","Is this gonna take all night?","Wow! Good thing I'm not busy, huh?",
                "Sheesh! *whistle while you work*","*sigh*", "*Eyes Rolling*","Oh, hey! You're still here?"])
    print(w+bws)

def badWaiterTermination():
    bwt=random.choice(["You are sooo slllloooowwww! I can't serve you!", "Geeeze! Say something! I'm outta here!", 
        "Would you like to choose today? NEXT!"])
    phrase=random.choice(["went ballistic", "lost his marbles", "blew up", "went crazy on you", "is having a bad day", "lost his $#!#"])
    phrase2=random.choice(["terminated your date","slapped you in the face","stole your date","called the cops on you", "kicked you in the shin"])
    print(w+bwt+"\n>> Oops! It seems like your waiter "+phrase+" and "+phrase2+"!\nBetter luck next time...")
    quit()

def waiterInquiry():
    inq=random.choice(["How is everything giong so far? [1,2,3,4,5]: ", "Are you having a good time? [1,2,3,4,5]: ",
        "How are you enjoying our service? [1,2,3,4,5]: ", "How satisfied would you say you are with our service? [1,2,3,4,5]: ",
        "How well have we catered to you thus far? [1,2,3,4,5]: "])
    return inq

def updateExperience(newScore):
    global surveysTaken, surveyScore, experienceRating
    surveysTaken+=1
    surveyScore+=int(newScore)
    experienceRating+=round((surveyScore/surveysTaken),2)

def runFoodSequence(course): 
    global cost
    # this badWaiterLimit is not based on Number of Times a question is answered incorrectly
    # but rather on the time being taken to answer
    badWaiterLimit=random.randint(7,12)   

    dc=2    # assume 2 people are dining
    dops=waiter('menu_food',course)
    dcc = 0
    badfood=False
    ditem=""
    while dcc < int(dc): 
        # set an arbitrary amount of time that the user "took to decide"...this could trigger the "bad waiter" behavior
        timetodecide=random.randint(1,12)
        #dcc+=1
        if badfood==False: 
            # show drink types:
            if dcc < 1: opener=random.choice(["OK! ","Alrighty! "])
            else: opener=random.choice(["Remember, we have: ","Again, we have: ","Once more, we have: "])
            print("\n"+w+opener+"We have: ")
            print(dops)

            # dcc+=1
            ditem=input("\n"+w+"what sort of "+course+" would you like for person #"+str(dcc+1)+"?: ")
        else:
            if ditem != "": print(w+"Sorry! We don't have any "+ditem+"\n")
            else: print(w+"Sorry...I didn't catch that...\n")
            time.sleep(1)
            # show drink types:
            opener=random.choice(["Remember, we have: ","Again, we have: ","Once more, we have: "])
            print("\n"+w+opener)
            print(dops)
            ditem=input("\n"+w+"Which would you would like for diner #"+str(dcc+1)+"?: ")

        if timetodecide >= badWaiterLimit: 
            print(f">> Oops! You took {timetodecide} minutes to make a decision!")
            prand=random.choice(["the patience of a Tazmanian Devil","the attention span of a mayfly","the focus of a goldfish"])
            print("\n>> Not bad but..your waiter has "+prand+"...\n")
            badWaiterSnap()
            
        if ditem in dops:
            dcc+=1
            badfood=False
            if ditem != 'skip':
                ditemcost=dops[ditem]  #....cost of drink [ditem]
                # drink=dtype+":"+ditem+":"+str(ditemcost)
                print("fooditem:::"+ditem+":"+str(ditemcost))
                if ditem in receipt[course]:
                    receipt[course][ditem]+=ditemcost
                else:
                    receipt[course][ditem]=ditemcost
                cost+=ditemcost
        else:
            badfood=True
            continue    


def runDrinkSequence():
    global cost
    badWaiterLimit=random.randint(2,5)
    seemenu=""
    seemenuset=False      
    seemenucount=0
    if badWaiterLimit < 3: print(f">> Watch out! Your waiter has a patience meter of [{badWaiterLimit}]. Answer quickly!")
    while (seemenucount <= badWaiterLimit) and (seemenu not in ["y","n"]):
    #while (seemenucount <= badWaiterLimit) and (seemenuset == False):
        if badWaiterLimit-seemenucount == 1:    # print(f"{w} I'll give you ONE more chance...")
            mt=input(w+"Need some more time? [y/n]: ")
            if mt.lower() == "y": 
                seemenucount = 0
                print(f"{w}Ok...I'll be back in 2 seconds...")
                time.sleep(2)
                continue
            else:
                print(f"{w}I'll give you ONE more chance...")

        seemenu=input(w+waiter('menu_ask','drink'))
        seemenucount+=1
        if len(seemenu) > 0:
            if seemenu.lower() == 'y': seemenuset = True 
            elif seemenu.lower() == 'n': seemenuset = True
            #sm=("TRUE" if seemenuset == True else "FALSE")
            #print(f"sm: {sm}")
        #else: print(">> seemenu empty...")
        #print(f"seemenu:{seemenu}, seemenucount:{seemenucount}, badWaiterLimit:{badWaiterLimit}\n")

    if (seemenucount == badWaiterLimit) and (seemenuset == False): badWaiterTermination()

    if(seemenu == 'y'):
        dops=waiter('menu_drinks','options')  
        #dops_s=', '.join(dops)
        dc=input(w+"How many drinks would you like to order? ")
        if int(dc) > 0:
            dcc = 0
            # print("\n"+w+"Ok! We have: ")
            # print(dops)
            baddrink=False
            ditem=""
            while dcc < int(dc): 
                rundlist=False
                #ditem=""
                if baddrink==False: 
                    # show drink types:
                    if dcc < 1: opener=random.choice(["OK! ","Alrighty! "])
                    else: opener=random.choice(["Remember, we have: ","Again, we have: ","Once more, we have: "])
                    print("\n"+w+opener+"We have: ")
                    print(dops)

                    dcc+=1
                    dtype=input("\n"+w+"what sort of drink would you like for #"+str(dcc)+"?: ")
                    #dtype=input(dops_s)
                    if dtype in dops:
                        dlist=waiter('menu_drinks',dtype)
                        print("\n"+w+"Do you have a preference? ")
                        print(dlist)
                        ditem=input()
                        rundlist=True
                    else:
                        ditem=""
                        baddrink=True
                else:
                    if ditem != "": print(w+"Sorry! We don't have any "+ditem+"\n")
                    else: print(w+"Sorry...I didn't catch that...\n")
                    time.sleep(1)
                    # show drink types:
                    opener=random.choice(["Remember, we have: ","Again, we have: ","Once more, we have: "])
                    print("\n"+w+opener)
                    print(dops)
                    dtype=input("\n"+w+"Which would you would like for #"+str(dcc)+"?: ")
                    #dtype=input(dops_s)
                    if dtype in dops:
                        dlist=waiter('menu_drinks',dtype)
                        print("\n"+w+"Do you have any preference? ")
                        print(dlist)
                        ditem=input()
                        rundlist=True
                    else:
                        ditem=""
                        baddrink=True
                # Finally, if the user has picked a valid drink, let's add it to the receipt
                if rundlist:
                    if ditem in dlist:
                        baddrink=False
                        ditemcost=dlist[ditem]  #....cost of drink [ditem]
                        drink=dtype+":"+ditem+":"+str(ditemcost)
                        print("drink:::"+drink)
                        receipt['drinks'][ditem]=ditemcost
                        cost+=ditemcost
                    else:
                        baddrink=True
                        continue
        else:
            print(w+"0 drinks it is...let's move along...")

# Let us try to follow the "questionSequence"
# >> questionSequence=['greet','seating_ask','menu_ask_drink','order_drink','serve_drink','inquiry',
#       'menu_ask_main', 'menu_ask_side', 'oder_food', 'inquiry','menu_ask_drink','order_drink','inquiry',
#       'serve_food', 'inquiry', 'menu_ask_desert', 'order_desert', 'inquiry', 'bill', 'bye']
# >> lastQuest
# --------------------------------------------------------------------------------------------------------------------

for qt in questionSequence:
    if qt == 'greet':
        print(waiter('greet',""))
        time.sleep(2)
    elif qt == 'seating_ask':
        sops=waiter('seating','options')
        q=w+"Would you like to sit "
        qc=0
        for sop in sops:
            q+=(sop if qc==0 else " or "+sop)
            qc+=1
        set_seating=input(q+'? ')
        lastQuest=q
    elif qt == 'menu_ask_drink':
        runDrinkSequence()            
    elif qt == 'order_drink':
        if len(receipt['drinks']) > 0:
            #print(w+"Your drinks should be out in a few minutes!")
            waittime=timeRand(5,20)     #....you will wait anywhere from 5 to 20 minutes
            time.sleep(1)
            timewaster=random.choice(["You look around","You spend some time chatting","You talk about how your day has been","You shoot the breeze", "You stare at each other"])
            print("..."+timewaster+"...")
            time.sleep(2)
            print("..."+str(waittime)+" minutes go by before your server comes back...")
    elif qt == 'serve_drink':
        if len(receipt['drinks']) > 0:
            print("\n"+w+"Here are your drinks...")
            print(">> Waiter prsents you with: ")
            print(receipt['drinks'])
            #print("\n")
    elif qt == 'inquiry':
        print("\n")
        inq=waiterInquiry()
        myscore=input(w+inq)
        updateExperience(myscore)
        print("\n"+w+"Thank you!")
        #if testScore: 
        print(">>> currentExperience:"+str(experienceRating)+"\n")      #.............used when debugging
    elif qt == 'menu_ask_appetizer':
        runFoodSequence('appetizer')
    elif qt == 'menu_ask_main':
        runFoodSequence('main')
    elif qt == 'menu_ask_side':
        runFoodSequence('side')
    elif qt == 'oder_food':
        # did visitors order any food? 
        alen=len(receipt["appetizer"])
        mlen=len(receipt["main"])
        slen=len(receipt["side"])
        flen=alen+mlen+slen
        if flen > 0:
            print(w+"Give me a moment to place this order. I will update you shortly.")
            randtime=random.randint(7,12) 
            print(w+"Your food should be out in a few minutes!")
            if len(receipt["appetizer"]) > 0:
                print("\n>> ...you only wait a few moments when here comes your waiter...appetizers in hand!")
                time.sleep(1)
                print(w+"Here you go. Enjoy!\n")
                time.sleep(2)

            waittime=timeRand(5,20)     #....you will wait anywhere from 5 to 20 minutes
            if waittime > 10: extra="The kitchen is pretty busy but I promise it will be just a few moments more =)"
            else: extra=""
            time.sleep(1)
            timewaster=random.choice(["You look around","You spend some time chatting","You talk about how your day has been","You shoot the breeze", "You stare at each other"])
            print("..."+timewaster+"...")
            time.sleep(2)
            if extra != "": print(w+extra)
            time.sleep(2)
    # elif qt == 'inquiry':
    # elif qt == 'menu_ask_drink':
    # elif qt == 'order_drink':
    # elif qt == 'inquiry':
    elif qt == 'serve_food':
        if len(receipt['main']) > 0:
            print("\n"+w+"Here is your food!...")
        
        print(">> Waiter prsents you with: ")
        if len(receipt["main"]) > 0:
            print(receipt['main'])
        if len(receipt["side"]) > 0:
            print(receipt['side'])
        
        print("\n"+w+"I hope you enjoy your meal. I'll be checking in on you periodically...")
        time.sleep(1)
        timewaster=random.choice(["You dig in","You enjoy some good food and conversation"])
        print("..."+timewaster+"...")
        time.sleep(2)

    #elif qt == 'inquiry':
    elif qt == 'menu_ask_desert':
        runFoodSequence('desert')
    elif qt == 'order_desert':
        if len(receipt['desert']) > 0:
            print(w+"Let me place your desert order. Be back soon.")
            time.sleep(2)
            print("\n>> ...you only wait a few minutes when...")
            # randtime=random.randint(7,12) 
            # print(w+" should be out in a few minutes!")
    elif qt == 'serve_desert':
        if len(receipt["desert"]) > 0:
            print(w+"Here's your desert!")
    #elif qt == 'inquiry':
    elif qt == 'bill':
        print(w+"I sincerely hope you've enjoyed your evening with us. Here's your bill...")
        print("\n#----------------------------------------------------------------#")
        print('#   TOTAL: $ '+str(cost))
        print(receipt)
        print("#----------------------------------------------------------------#")
    elif qt == 'bye':
        print("\n"+w+"Ciao! See you again some other time...")
        print("\n#----------------------------------------------------------------#")
        # print("#   Based on your overall experience rating of ["+str(experienceRating)+"]")
        showDateResult()
        print("\n#----------------------------------------------------------------#")
    else:
        print(f">> Prompt type: {qt}")

quit()

# # greet customer
# print(waiter("greet",""))
# time.sleep(2)

# # ask if they would like to see the menu
# q=waiter("menu_ask","drink")    # drink, breakfast, lunch, dinner
# seemenu=input(q)


# if(seemenu == "y"):
#     t1="menu_food"
#     t2="appetizer"
#     q = waiter(t1,t2)
#     print(f"\n{w}Please choose your {t2}:\n{q}")
#     choice=input()
#     if(choice == "skip"):
#         print(f"\n{w}No {t2}? No problem...")
#         time.sleep(1)
#         print(f"\n{w}Moving on...")
#         time.sleep(1)
#     else:
#         cc=validate(t1,t2,choice)
#         cost+=cc
#         print("Note: $"+str(cc)+" has been added to your bill...[total: $"+str(cost)+"]\n")

#     #print(f"\")
# else:
#     print("\n{w}Sorry we couldn't help you. Perhaps we will see you again another time...\n\n\n")

