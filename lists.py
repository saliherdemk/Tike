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
for i in range(1,701):
    daily_earn.append(100)

for i in range(1,51):
    daily_earn.append(110)

for i in range(1,51):
    daily_earn.append(125)

for i in range(1,21):
    daily_earn.append(130)

for i in range(1,21):
    daily_earn.append(150)

for i in range(1,21):
    daily_earn.append(175)

for i in range(1,21):
    daily_earn.append(190)

for i in range(1,21):
    daily_earn.append(200)

for i in range(1,11):
    daily_earn.append(245)
    daily_earn.append(250)
    daily_earn.append(255)
    daily_earn.append(260)
    daily_earn.append(270)
    daily_earn.append(280)
    daily_earn.append(290)
    daily_earn.append(300)

for i in range(1,8):
    daily_earn.append(400)

for i in range(1,6):
    daily_earn.append(450)
    daily_earn.append(470)

for i in range(1,2):
    daily_earn.append(750)

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
for i in range(1,31):
    solo1.append("{} | {} | {}".format(":one:",":one:",":one:"))

for i in range(1,16):
    solo1.append("{} | {} | {}".format(":two:",":two:",":two:"))

for i in range(1,6):
    solo1.append("{} | {} | {}".format(":three:",":three:",":three:"))

for i in range(1,6):
    solo1.append("{} | {} | {}".format(":four:",":four:",":four:"))

for i in range(1,4):
    solo1.append("{} | {} | {}".format("five","five","five"))

for i in range(1,3):
    solo1.append("{} | {} | {}".format("six","six","six"))

for i in range(1,41):
    solo1.append("{} | {} | {}".format(element1[random.randint(0,5)],element1[random.randint(0,5)],element1[random.randint(0,5)]))


#SOLO 2
for i in range(1,18):
    solo2.append("{} | {} | {}".format(":pirate_flag:",":pirate_flag:",":pirate_flag:"))

for i in range(1,8):
    solo2.append("{} | {} | {}".format(":dollar:",":dollar:",":dollar:"))

for i in range(1,7):
    solo2.append("{} | {} | {}".format(":moneybag:",":moneybag:",":moneybag:"))

for i in range(1,5):
    solo2.append("{} | {} | {}".format(":trident:",":trident:",":trident:"))

for i in range(1,4):
    solo2.append("{} | {} | {}".format(":fleur_de_lis:",":fleur_de_lis:",":fleur_de_lis:"))

for i in range(1,3):
    solo2.append("{} | {} | {}".format(":black_joker:",":black_joker:",":black_joker:"))

solo2.append(":gift: | :gift: | :gift:")

for i in range(1,61):
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
