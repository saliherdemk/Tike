import numpy as np
import random


element = [":new_moon:",":waning_crescent_moon:",":last_quarter_moon:",":full_moon:" ]
element1 = [":one:",":two:",":three:",":four:",":five:",":six:"]
element2 = [":pirate_flag:",":dollar:",":moneybag:",":trident:",":fleur_de_lis:",":black_joker:",":gift:"]
element3 = [":soccer:",":basketball:",":football:",":baseball:"]

cars = [[":red_car:",":taxi:",":blue_car:"],[":red_car:",":blue_car:",":taxi:"],[":taxi:",":blue_car:",":red_car:"],[":taxi:",":red_car:",":blue_car:"],[":blue_car:",":taxi:",":red_car:"],[":blue_car:",":red_car:",":taxi:"]]

daily_earn = []
solo = []
solo1 = []
solo2 = []
solo3 = []


#Earn daily
for i in range(1,501):
    daily_earn.append(100)

for i in range(1,81):
    daily_earn.append(175)

for i in range(1,71):
    daily_earn.append(200)

for i in range(1,51):
    daily_earn.append(250)

for i in range(1,41):
    daily_earn.append(275)
    daily_earn.append(290)
    daily_earn.append(300)

for i in range(1,31):
    daily_earn.append(325)
    daily_earn.append(350)
    daily_earn.append(400)

for i in range(1,21):
    daily_earn.append(500)

for i in range(1,11):
    daily_earn.append(575)
    daily_earn.append(600)
    daily_earn.append(625)
    daily_earn.append(650)
    daily_earn.append(675)

for i in range(1,8):
    daily_earn.append(750)

for i in range(1,6):
    daily_earn.append(800)
    daily_earn.append(850)

for i in range(1,2):
    daily_earn.append(1000)

daily_earn.append(100000)



#SOLO
for i in range(1,41):
    solo.append("{} | {} | {}".format(":new_moon:",":new_moon:",":new_moon:"))

for i in range(1,26):
    solo.append("{} | {} | {}".format(":waning_crescent_moon:",":waning_crescent_moon:",":waning_crescent_moon:"))

for i in range(1,11):
    solo.append("{} | {} | {}".format(":last_quarter_moon:",":last_quarter_moon:",":last_quarter_moon:"))

for i in range(1,6):
    solo.append("{} | {} | {}".format(":full_moon:",":full_moon:",":full_moon:"))

for i in range(1,21):
    solo.append("{} | {} | {}".format(element[random.randint(0,3)],element[random.randint(0,3)],element[random.randint(0,3)]))


#SOLO 1
for i in range(1,34):
    solo1.append("{} | {} | {}".format(":one:",":one:",":one:"))

for i in range(1,15):
    solo1.append("{} | {} | {}".format(":two:",":two:",":two:"))

for i in range(1,9):
    solo1.append("{} | {} | {}".format(":three:",":three:",":three:"))

for i in range(1,6):
    solo1.append("{} | {} | {}".format(":four:",":four:",":four:"))

for i in range(1,5):
    solo1.append("{} | {} | {}".format(":five:",":five:",":five:"))

for i in range(1,2):
    solo1.append("{} | {} | {}".format(":six:",":six:",":six:"))

for i in range(1,36):
    solo1.append("{} | {} | {}".format(element1[random.randint(0,5)],element1[random.randint(0,5)],element1[random.randint(0,5)]))


#SOLO 2
for i in range(1,17):
    solo2.append("{} | {} | {}".format(":pirate_flag:",":pirate_flag:",":pirate_flag:"))

for i in range(1,13):
    solo2.append("{} | {} | {}".format(":dollar:",":dollar:",":dollar:"))

for i in range(1,9):
    solo2.append("{} | {} | {}".format(":moneybag:",":moneybag:",":moneybag:"))

for i in range(1,7):
    solo2.append("{} | {} | {}".format(":trident:",":trident:",":trident:"))

for i in range(1,5):
    solo2.append("{} | {} | {}".format(":fleur_de_lis:",":fleur_de_lis:",":fleur_de_lis:"))

for i in range(1,4):
    solo2.append("{} | {} | {}".format(":black_joker:",":black_joker:",":black_joker:"))

solo2.append(":gift: | :gift: | :gift:")

for i in range(1,51):
    solo2.append("{} | {} | {}".format(element2[random.randint(0,6)],element2[random.randint(0,6)],element2[random.randint(0,6)]))

#Solo 3 
for i in range(1,6):
    solo3.append("{} | {} | {}".format(":soccer:",":soccer:",":soccer:"))

for i in range(1,6):
    solo3.append("{} | {} | {}".format(":basketball:",":basketball:",":basketball:"))

for i in range(1,6):
    solo3.append("{} | {} | {}".format(":football:",":football:",":football:"))

for i in range(1,6):
    solo3.append("{} | {} | {}".format(":baseball:",":baseball:",":baseball:"))
for i in range(1,81):
    solo3.append("{} | {} | {}".format(element3[random.randint(0,3)],element3[random.randint(0,3)],element3[random.randint(0,3)]))

#Results
def np_lists():
    np_solo = np.array(solo)
    np_solo1 = np.array(solo1)
    np_solo2 = np.array(solo2)
    np_solo3 = np.array(solo3)
    np_cars = np.array(cars)
    return np_solo,np_solo1,np_solo2,np_solo3,np_cars
    
def objects():
    return element,element1,element2,element3,daily_earn
