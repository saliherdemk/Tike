import random
from textwrap import indent
import discord
from discord.ext import  commands
import json
import asyncio
import time
import lists
import os
from functions import open_account,data,loto5_data,open_json,info,info_p,all_equal,loto3_data

Bot = commands.Bot(command_prefix='ot!', help_command=None)

all_list = lists.np_lists()
all_object = lists.objects()

#SLOT 1
@Bot.command(pass_context = True)
@commands.cooldown(6, 86400, commands.BucketType.member)
async def slot1(ctx,money = 0):

    id = ctx.message.guild.id

    await open_account(ctx.author,ctx)

    a = all_list[0][random.randint(0,100)]

    users = await data(ctx)

    user = ctx.author

    if users[str(user.id)]["BANNED"] :
        await ctx.send("Banlısın!")
    
    else :
        

        if money == 50 :
            
            if users[str(user.id)]["wallet"] < money:
                await ctx.send("""```css
[Not enough coin.]```""")
            else:
                await ctx.send("""```css
Your daily allowance is over.
If you still want to play, pay [50] coins . Continue? (yes or no)```""")

                try:
                    message = await Bot.wait_for("message",check= lambda m : m.author == ctx.author and m.channel, timeout = 30.0)

                except asyncio.TimeoutError:
                    await ctx.channel.send("Time's up!")
                
                else:
                    if message.content == "yes" or message.content == "YES" :
                        
                        users[str(user.id)]["wallet"] -= money
                        users[str(user.id)]["total"] += 1 

                        with open(f"{id}users.json", "w") as f:
                            json.dump(users,f,indent=2)
                    
                        emoji_result = None

                        earned = 0

                        a = all_list[0][random.randint(0,101)]

                        

                        if a == ":new_moon: | :new_moon: | :new_moon:":
                            emoji_result = ":star2: Congratulations! :star2:"
                            
                            earned = 20

                            users[str(user.id)]["wallet"] += 20
                            users[str(user.id)]["win"] += 1

                            with open(f"{id}users.json", "w") as f:
                                json.dump(users,f,indent=2)


                        elif a == ":waning_crescent_moon: | :waning_crescent_moon: | :waning_crescent_moon:":
                            emoji_result = ":star2: Congratulations! :star2:"
                            
                            earned = 25

                            users[str(user.id)]["wallet"] += 25
                            users[str(user.id)]["win"] += 1

                            with open(f"{id}users.json", "w") as f:
                                json.dump(users,f,indent=2)

                        elif a == ":last_quarter_moon: | :last_quarter_moon: | :last_quarter_moon:":
                            emoji_result = ":star2: Congratulations! :star2:"
                            
                            earned = 50

                            users[str(user.id)]["wallet"] += 50
                            users[str(user.id)]["win"] += 1

                            with open(f"{id}users.json", "w") as f:
                                json.dump(users,f,indent=2)

                        elif a == ":full_moon: | :full_moon: | :full_moon:":
                            emoji_result = ":star2: Congratulations! :star2:"
                            
                            earned = 100

                            users[str(user.id)]["wallet"] += 100
                            users[str(user.id)]["win"] += 1

                            with open(f"{id}users.json", "w") as f:
                                json.dump(users,f,indent=2)

                        else :
                            emoji_result = ":anger: Why someone pay for this?"
                        
                        if earned != 0 :
                            result = """```bash
"{}, you earned a bunch of {} coins! Your profit: {} "```""".format(user.name ,  earned ,  earned - 50)
                        else :
                            result = """```css
[{}, you earned a bunch of {} coins! ] Your profit: {} ```""".format(user.name ,  earned ,  earned - 50)
                        
                        embed =discord.Embed(description ="""```ini
[Tier 1] Slot is spinning....     ```
⠀ {} | {} | {}

⌠ {} ⌡   ~~~~  {}

⠀ {} | {} | {}  

{}""".format(all_object[0][random.randint(0,3)],all_object[0][random.randint(0,3)],all_object[0][random.randint(0,3)],a,emoji_result ,all_object[0][random.randint(0,3)],all_object[0][random.randint(0,3)],all_object[0][random.randint(0,3)],result))
                        await ctx.send(embed = embed)
                    
                    else :
                        None

        else :
            users[str(user.id)]["wallet"] -= money
            
            users[str(user.id)]["total"] += 1 

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f,indent=2)

            emoji_result = None

            earned = 0

            

            if a == ":new_moon: | :new_moon: | :new_moon:":
                emoji_result = ":star2: Congratulations! :star2:"
                
                earned = 20

                users[str(user.id)]["wallet"] += 20
                users[str(user.id)]["win"] += 1

                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)

            elif a == ":waning_crescent_moon: | :waning_crescent_moon: | :waning_crescent_moon:":
                emoji_result = ":star2: Congratulations! :star2:"
                
                earned = 25

                users[str(user.id)]["wallet"] += 25
                users[str(user.id)]["win"] += 1

                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)

            elif a == ":last_quarter_moon: | :last_quarter_moon: | :last_quarter_moon:":
                emoji_result = ":star2: Congratulations! :star2:"
            
                earned = 50

                users[str(user.id)]["wallet"] += 50
                users[str(user.id)]["win"] += 1

                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)

            elif a == ":full_moon: | :full_moon: | :full_moon:":
                emoji_result = ":star2: Congratulations! :star2:"
                
                earned = 100


                users[str(user.id)]["wallet"] += 100
                users[str(user.id)]["win"] += 1

                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)

            else :
                emoji_result = ":anger: Don't worry. Try another one"
            
            if earned != 0 :
                result = """```bash
"{}, you earned a bunch of {} coins!"```""".format(user.name , earned)
            else :
                result = """```css
[{}, you earned a bunch of {} coins!]```""".format(user.name , earned)

            embed = discord.Embed(description ="""```ini
[Tier 1] Slot is spinning....
```
⠀ {} | {} | {}

⌠ {} ⌡   ~~~~  {}

⠀ {} | {} | {}
                
{}                    """.format(all_object[0][random.randint(0,3)],all_object[0][random.randint(0,3)],all_object[0][random.randint(0,3)],a,emoji_result ,all_object[0][random.randint(0,3)],all_object[0][random.randint(0,3)],all_object[0][random.randint(0,3)],result) )
            
            await ctx.send(embed = embed)
        
        







#SLOT 2
@Bot.command(pass_context = True)
@commands.cooldown(1, 5, commands.BucketType.member)
async def slot2(ctx):

    id = ctx.message.guild.id

    await open_account(ctx.author,ctx)

    users = await data(ctx)

    user = ctx.author

    if users[str(user.id)]["BANNED"] :
        await ctx.send("Banlısın!")
    
    else :

        if users[str(user.id)]["wallet"] < 100 :
            await ctx.send("""```css
[Not enough coin.]```""")
        else :

            users[str(user.id)]["wallet"] -= 100
            users[str(user.id)]["total"] += 1 

            with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)

            a = all_list[1][random.randint(0,100)]
            
            emoji_result = None
            earned = 0

            if a == ":one: | :one: | :one:":
                emoji_result = ":star2: Congratulations! :star2:"

                earned = 90

                users[str(user.id)]["wallet"] += 90
                users[str(user.id)]["win"] += 1

                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)

            elif a == ":two: | :two: | :two:":
                emoji_result = ":star2: Congratulations! :star2:"

                earned = 200

                users[str(user.id)]["wallet"] += 200
                users[str(user.id)]["win"] += 1

                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)

            elif a == ":three: | :three: | :three:":
                emoji_result = ":star2: Congratulations! :star2:"

                earned = 250

                users[str(user.id)]["wallet"] += 250
                users[str(user.id)]["win"] += 1

                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)

            elif a == ":four: | :four: | :four:":
                emoji_result = ":star2: Congratulations! :star2:"

                earned = 275

                users[str(user.id)]["wallet"] += 275
                users[str(user.id)]["win"] += 1

                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)
            
            elif a == ":five: | :five: | :five:":
                emoji_result = ":star2: Congratulations! :star2:"

                earned = 300

                users[str(user.id)]["wallet"] += 300
                users[str(user.id)]["win"] += 1

                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)

            elif a == ":six: | :six: | :six:":
                emoji_result = ":star2: Congratulations! :star2:"

                earned = 375

                users[str(user.id)]["wallet"] += 375
                users[str(user.id)]["win"] += 1

                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)

            else :
                emoji_result = ":anger: May the luck be with you next time..."
            
            if earned != 0 :
                result = """```bash
"{}, you earned a bunch of {} coins! Your profit: {} "```""".format(user.name ,  earned ,  earned - 100)
            else :
                result = """```css
[{}, you earned a bunch of {} coins! ] Your profit: {} ```""".format(user.name ,  earned ,  earned - 100)

            embed = discord.Embed(description = """```BASH
"Tier 2" Slot is spinning for 100 coins....     ```
⠀ {} | {} | {}

⌠ {} ⌡   ~~~~  {}

⠀ {} | {} | {}
{}                    """.format(all_object[1][random.randint(0,5)],all_object[1][random.randint(0,5)],all_object[1][random.randint(0,5)],a,emoji_result ,all_object[1][random.randint(0,5)],all_object[1][random.randint(0,5)],all_object[1][random.randint(0,5)],result))
            
            await ctx.send(embed = embed)



#SLOT 3
@Bot.command(pass_context = True)
@commands.cooldown(1, 5, commands.BucketType.member)
async def slot3(ctx):

    id = ctx.message.guild.id

    await open_account(ctx.author,ctx)

    users = await data(ctx)

    user = ctx.author

    if users[str(user.id)]["BANNED"] :
        await ctx.send("Banlısın!")
    
    else :

        if users[str(user.id)]["wallet"] < 250 :
            await ctx.send("""```css
[Not enough coin.]```""")
        else :
            users[str(user.id)]["wallet"] -= 250
            users[str(user.id)]["total"] += 1 

            with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)

            a = all_list[2][random.randint(0,100)]
            
            emoji_result = None

            earned = 0

            if a == ":pirate_flag: | :pirate_flag: | :pirate_flag:":
                emoji_result = ":star2: Congratulations! :star2:"
                
                earned = 240

                users[str(user.id)]["wallet"] += 240
                users[str(user.id)]["win"] += 1

                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)

            elif a == ":dollar: | :dollar: | :dollar:":
                emoji_result = ":star2: Congratulations! :star2:"
                
                earned = 325

                users[str(user.id)]["wallet"] += 325
                users[str(user.id)]["win"] += 1

                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)

            elif a == ":moneybag: | :moneybag: | :moneybag:":
                emoji_result = ":star2: Congratulations! :star2:"
                
                earned = 400

                users[str(user.id)]["wallet"] += 400
                users[str(user.id)]["win"] += 1

                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)

            elif a == ":trident: | :trident: | :trident:":
                emoji_result = ":star2: Congratulations! :star2:"
                
                earned = 500

                users[str(user.id)]["wallet"] += 500
                users[str(user.id)]["win"] += 1

                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)
            
            elif a == ":fleur_de_lis: | :fleur_de_lis: | :fleur_de_lis:":
                emoji_result = ":star2: Congratulations! :star2:"
                
                earned = 600

                users[str(user.id)]["wallet"] += 600
                users[str(user.id)]["win"] += 1

                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)

            elif a == ":black_joker: | :black_joker: | :black_joker:":
                emoji_result = ":star2: Congratulations! :star2:"
                
                earned = 800

                users[str(user.id)]["wallet"] += 800
                users[str(user.id)]["win"] += 1

                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)
                
            elif a == ":gift: | :gift: | :gift:":
                emoji_result = ":star2: Congratulations! :star2:"
            
                earned = 1250

                users[str(user.id)]["wallet"] += 1250
                users[str(user.id)]["win"] += 1

                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)

            else :
                emoji_result = ":anger: Try again, braveheart!"
            
            if earned != 0 :
                result = """```bash
"{}, you earned a bunch of {} coins! Your profit: {} "```""".format(user.name ,  earned ,  earned - 250)
            else :

                result = """```css
[{}, you earned a bunch of {} coins! ] Your profit: {} ```""".format(user.name ,  earned ,  earned - 250)


            embed = discord.Embed(description = """```css
[Tier 3] Slot is spinning for 250 coins....      ```
⠀ {} | {} | {}

⌠ {} ⌡   ~~~~  {}

⠀ {} | {} | {}
{}                    """.format(all_object[2][random.randint(0,6)],all_object[2][random.randint(0,6)],all_object[2][random.randint(0,6)],a,emoji_result ,all_object[2][random.randint(0,6)],all_object[2][random.randint(0,6)],all_object[2][random.randint(0,6)],result))

            await ctx.send(embed = embed)


#Slot 4
@Bot.command(pass_context = True)
@commands.cooldown(1, 5, commands.BucketType.member)
async def slot4(ctx,money = 0):

    id = ctx.message.guild.id

    await open_account(ctx.author,ctx)

    users = await data(ctx)

    user = ctx.author

    if users[str(user.id)]["BANNED"] :
        await ctx.send("Banlısın!")
    
    else :

        if money == 0:
            await ctx.send("You have to put some coins on this slot.")
        elif money < 0 :
            await ctx.send("WHATCHA TRYNA DO??")

        elif money > users[str(user.id)]["wallet"]:
            await ctx.send("""```css
[Not enough coin.]```""")
        

        else :
            a = all_list[3][random.randint(0,100)]
            users[str(user.id)]["wallet"] -= money
            users[str(user.id)]["total"] += 1 

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f,indent=2)

            emoji_result = None

            earned = 0

            if a == ":soccer: | :soccer: | :soccer:" or a == ":basketball: | :basketball: | :basketball:" or a == ":football: | :football: | :football:" or a == ":baseball: | :baseball: | :baseball:":
                emoji_result = ":star2: Congratulations! :star2:"
                
                earned = money * 2

                users[str(user.id)]["wallet"] += money * 2
                users[str(user.id)]["win"] += 1

                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)

            else :
                emoji_result = ":anger: Better be next time..."
            
            if earned != 0 :
                result = """```bash
"{}, you earned a bunch of {} coins! Your profit: {} "```""".format(user.name , earned , earned - money)
            else :

                result = """```css
[{}, you earned a bunch of {} coins! ] Your profit: {} ```""".format(user.name , earned , earned - money)

            embed = discord.Embed(description = """```apache
Tier 4 Slot is spinning for {} coins....     ```

⠀ {} | {} | {}

⌠ {} ⌡   ~~~~  {}

⠀ {} | {} | {}
{}                    """.format(money,all_object[3][random.randint(0,3)],all_object[3][random.randint(0,3)],all_object[3][random.randint(0,3)],a,emoji_result ,all_object[3][random.randint(0,3)],all_object[3][random.randint(0,3)],all_object[3][random.randint(0,3)],result))

            await ctx.send(embed = embed)


# Race Bet

@Bot.command(pass_context = True)
@commands.cooldown(3, 86400, commands.BucketType.member)
async def racebet(ctx,money = 0):

    id = ctx.message.guild.id

    await open_account(ctx.author,ctx)

    users = await data(ctx)

    user = ctx.author

    if users[str(user.id)]["BANNED"] :
        await ctx.send("Banlısın!")
    
    else :
    
        if money < 0:
            await ctx.send("WHATCHA TRYNA DO??")
        
        else :

            if money > users[str(user.id)]["wallet"]:
                await ctx.send("""```css
[Not enough coin.]```""")
            else:
                delete1 =await ctx.send("{}            {}            {}         ".format(all_list[4][0][0],all_list[4][0][1],all_list[4][0][2]))
                delete2  = await ctx.send("""```Choose your car. [red , yellow , blue]```""")

                chose = None

                try:
                    message = await Bot.wait_for("message",check= lambda m : m.author == ctx.author and m.channel, timeout = 30.0)

                except asyncio.TimeoutError:
                    await ctx.channel.send("Time's up!")
                
                else:
                    
                    if str(message.content).lower() == "red":
                        chose = ":red_car:"
                        await delete1.delete()
                        await delete2.delete()
                    elif str(message.content).lower() == "yellow":
                        chose = ":taxi:"
                        await delete1.delete()
                        await delete2.delete()
                    elif str(message.content).lower() == "blue":
                        chose = ":blue_car:"
                        await delete1.delete()
                        await delete2.delete()
                    else :
                        liste = [":red_car:",":taxi:",":blue_car:"]
                        randomly = liste[random.randint(0,2)]
                        chose = randomly
                        await ctx.send(f"Randomly {randomly} has been chosen.")
                        
                    money = int(money)

                    users[str(user.id)]["wallet"] -= money
                    users[str(user.id)]["total"] += 1
                    with open(f"{id}users.json", "w") as f:
                        json.dump(users,f,indent=2)
                    
                    one = all_list[4][random.randint(0,5)]
                    two = all_list[4][random.randint(0,5)]
                    three = all_list[4][random.randint(0,5)]

                    liste = [one,two,three]

                    absolute = liste[random.randint(0,2)]

                    final = random.randint(0,2)

                    b = discord.Embed(title ="3")
                    c = discord.Embed(title ="2")
                    d = discord.Embed(title ="1")
                    e = discord.Embed(title ="Start!")
                    em =  await ctx.send(embed = b)
                    time.sleep(0.5)
                    await em.edit(embed = c)
                    time.sleep(0.5)
                    await em.edit(embed = d)
                    time.sleep(0.5)
                    await em.edit(embed = e)

                    f = discord.Embed(title ="Start!",description="""
        ─────────── :checkered_flag: 
⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀{} 
───────────
⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀{} 
───────────
⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀{} 
─────────── :checkered_flag: 
                    """.format(absolute[0],absolute[1],absolute[2]))
                    await em.edit(embed = f)
                    time.sleep(0.5)

                    g = discord.Embed(title ="Start!",description = """
        ───────────
⠀ ⠀ ⠀ ⠀{} 
───────────
⠀ ⠀⠀ ⠀⠀ ⠀⠀ {} 
───────────
⠀ ⠀⠀ ⠀⠀ ⠀{} 
───────────
                    """.format(absolute[0],absolute[1],absolute[2]))
                    await em.edit(embed = g)
                    time.sleep(0.5)

                    h = discord.Embed(title ="Start!",description = """
        ───────────
⠀ ⠀⠀ ⠀⠀ {} 
───────────
⠀ ⠀⠀ ⠀⠀{} 
───────────
⠀ ⠀⠀ ⠀⠀ ⠀⠀ {} 
───────────
                    """.format(absolute[0],absolute[1],absolute[2]))
                    
                    await em.edit(embed = h)

                    time.sleep(0.5)
                    ie = discord.Embed(title ="Start!",description = """
        ───────────
⠀ ⠀⠀ ⠀⠀ ⠀⠀ {} 
───────────
⠀ ⠀⠀ ⠀{} 
───────────
⠀⠀ ⠀⠀⠀ ⠀⠀{} 
───────────
                """.format(absolute[0],absolute[1],absolute[2]))

                    await em.edit(embed = ie)

                    time.sleep(0.5)
                if final == 0 :
                    if absolute[0] == chose:
                        result = "You won!"
                        enough = """```bash
"{}, you earned a bunch of {} coins! Your profit: {} "```""".format(user.name , money * 2 , money * 2 - money)
                        users[str(user.id)]["wallet"] += money * 2
                        users[str(user.id)]["win"] += 1
                        with open(f"{id}users.json", "w") as f:
                            json.dump(users,f,indent=2)
                        
                    else:
                        result = "You lost!"
                        enough = """```css
[{}, you earned nothing!] Your profit: -{}```""".format(user.name , money)
                    i = discord.Embed(title =f"{result}",description = """
        ──:checkered_flag:────────
{} 
───────────
⠀ ⠀⠀ ⠀⠀ {} 
───────────
⠀⠀ ⠀{} 
──:checkered_flag:────────
{}""".format(absolute[0],absolute[1],absolute[2],enough))
                    await em.edit(embed = i)
                    


                elif final == 1 :
                    if absolute[1] == chose:
                        result = "You won!"
                        users[str(user.id)]["wallet"] += money * 2
                        users[str(user.id)]["win"] += 1
                        with open(f"{id}users.json", "w") as f:
                            json.dump(users,f,indent=2)
                        enough = """```bash
"{}, you earned a bunch of {} coins! Your profit: {} "```""".format(user.name , money * 2 , money * 2 - money)
                    else:
                        result = "You lost!"
                        enough = """```css
[{}, you earned nothing!] Your profit: -{}```""".format(user.name , money)
                    j = discord.Embed(title =f"{result}",description = """
        ──:checkered_flag:────────
⠀⠀ {} 
───────────
{} 
───────────
⠀⠀ ⠀{} 
──:checkered_flag:────────
{}""".format(absolute[0],absolute[1],absolute[2],enough))
                    await em.edit(embed = j)
                    

                else :
                    if absolute[2] == chose:
                        result = "You won!"
                        users[str(user.id)]["wallet"] += money * 2
                        users[str(user.id)]["win"] += 1
                        with open(f"{id}users.json", "w") as f:
                            json.dump(users,f,indent=2)
                        enough = """```bash
"{}, you earned a bunch of {} coins! Your profit: {}"```""".format(user.name , money * 2 , money * 2 - money)
                    else:
                        result = "You lost!"
                        enough = """```css
[{}, you earned nothing!] Your profit: -{}```""".format(user.name , money)
                    k = discord.Embed(title =f"{result}",description = """
        ──:checkered_flag:────────
⠀⠀ ⠀⠀⠀ {} 
───────────
⠀⠀ ⠀{} 
───────────
{} 
──:checkered_flag:────────
{}        """.format(absolute[0],absolute[1],absolute[2],enough))
                    await em.edit(embed = k)
                
# Price List

@Bot.command(pass_context = True)
@commands.cooldown(1, 5, commands.BucketType.member)
async def price(ctx):
    embed = discord.Embed(color = discord.Color.green(),title = "Tike | Price",description = """
**Tier 1 Slot**: 50 Coins (6 spin free per day)

**Tier 2 Slot**: 100 Coins

**Tier 3 Slot**: 250 Coins

**Tier 4 Slot**: Double your coins.

**Car race**: Double your coins. (3 race per day)

**Lotto Ticket**: 200 Coins """)
    await ctx.send(embed = embed)

@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.member)
async def help(ctx):

    await open_json(ctx)
    
    embed = discord.Embed(color = discord.Color.green(),title = "Tike | Help",description = """
**Welcome to Tike Bot!
Thank you for choosing us! :heart: **

Looks like you need some help.( ಠ ͜ʖಠ)
Here is the list of all commands;

**`o!profile`**: The profile for your coins and win rate.
**`o!earn`**: Get free coins per 3 hours.
**`o!slot1`**: Tier 1 Slot.
**`o!slot2`**: Tier 2 Slot.
**`o!slot3`**: Tier 3 Slot.
**`o!slot4 [Price]`**: Tier 4 Slot.
**`o!price`**: Price list of all the games.
**`o!racebet [Price]`**: Bet on a car race.
**`o!lotto5`**: Buy a ticket for 200 coins with other 4 users. Winner gets 1000 coins.
**`o!send [Username]`**: You can transfer your money to the every user you want.
**`o!prob`**: Win probabilities.
**`o!rob [Username]`**: Steal %30 of someone's coins with %50 luck. 
You must have 1000 coins for be able to rob.
If you fail you lose 50% of your coins to your target user. 1 rob try per day.

**Contact**:

[Official Server](https://discord.gg/vFCRRmd8)  |  [Invite](https://discord.com/oauth2/authorize?client_id=818200360819884062&scope=bot&permissions=1073769472)




 """)
    await ctx.send(embed = embed)

# Prob List

@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.member)
async def prob(ctx):
    embed = discord.Embed(color = discord.Color.green(),title = "Tike | Prob",description ="""
**Tier 1 Slot**⠀ ⠀⠀ ⠀     ⠀ ⠀⠀**Tier 2 Slot**    
%40 - 20 Coins⠀ ⠀⠀ ⠀%33 - 90 Coins
%25 - 25 Coins⠀ ⠀⠀ ⠀      %14 - 200 Coins
%10 - 50 Coins⠀ ⠀⠀ ⠀      %8 - 250 Coins
%5 - 100 Coins⠀ ⠀⠀ ⠀      %5 - 275 Coins
 ⠀ ⠀⠀ ⠀      ⠀ ⠀⠀ ⠀      ⠀ ⠀⠀ ⠀%4 - 300 Coins
 ⠀ ⠀⠀ ⠀      ⠀ ⠀⠀ ⠀      ⠀ ⠀⠀ ⠀%1 - 375 Coins
    
**Tier 3 Slot**⠀ ⠀⠀ ⠀ ⠀ ⠀⠀**Tier 4 Slot**⠀ ⠀⠀ ⠀      
%16 - 240 Coins⠀ ⠀⠀ ⠀%20 - Win
%12 - 325 Coins⠀ ⠀⠀ ⠀ **Car Race**
%8 - 400 Coins⠀ ⠀⠀ ⠀ %33,3 - Win
%6 - 500 Coins⠀ ⠀⠀ ⠀ **Lotto**
%4 - 600 Coins⠀ ⠀⠀ ⠀ %20 - Win
%3 - 800 Coins⠀ ⠀⠀ ⠀ **Earn** 
%1 - 1250 Coins⠀ ⠀⠀ ⠀ %50 - 100 ~~ %0,1 - 100000 Coins (Big Prize)     
""")
    await ctx.send(embed = embed)


# Shot Profile

@Bot.command(pass_context = True)
@commands.cooldown(1, 5, commands.BucketType.member)
async def profile(ctx):

    await open_json(ctx)

    await open_account(ctx.author,ctx)

    user = ctx.author

    users = await data(ctx)

    wallet_amt = int(users[str(user.id)]["wallet"])

    cashbox = int(users[str(user.id)]["cashbox_amount"])

    all_badges = []

    all_abilities = {}

    banlock = {}

    for key,value in (users[str(user.id)]["badge"]).items():
        if value is True:
            all_badges.append(key)
        else:
            all_badges.append("-")
    
    for key,value in (users[str(user.id)]).items():
        if key == "badge" or key == "cashbox_amount" or key == "name" or key == "wallet" or key == "win" or key == "total":
            pass

        elif key == "BANNED" or key =="In_Jail":
            if value is True:
                banlock[key] = value

        else:
            if value != 0 :
                all_abilities[key] = value
            else:
                continue

    try:
        win_rate = (users[str(user.id)]["win"] / users[str(user.id)]["total"]) * 100
       
    except:
        win_rate = 0

    string = json.dumps(all_abilities)
    string = string.replace("{" ," ")
    string = string.replace("}","")
    string = string.replace('"',"")
    string = string.replace("_"," ")
    last = string.replace(",","\n")

    banlock_string = json.dumps(banlock)
    banlock_string = banlock_string.replace("{" ,"")
    banlock_string = banlock_string.replace("}","")
    banlock_string = banlock_string.replace('"',"")
    banlock_string = banlock_string.replace("_"," ")
    banlock_string = banlock_string.replace(":","")
    banlock_string = banlock_string.replace("true","")
    banlock_last = banlock_string.replace(",","\n-")

    if len(banlock) == 0 :
        banlock_last = "Free"
        alert2 = "yaml"
        minus = ""
       
    else:
        minus = "-"
        alert2 = "diff"


    if last == " ":
        last = "No Abilities"
    
    embed = discord.Embed(color = discord.Color.blue())

    embed.set_author(name = user.name,icon_url= user.avatar_url)

    alert = None

    if int(win_rate) < 50 :
        alert = "css"
        a = "["
        b = "]"
    else:
        alert = "yaml"
        a = ""
        b = ""
    
    embed.add_field(name="Wallet",value=f""" ```yaml
{wallet_amt} Coins```""",inline=True)

    embed.add_field(name="Win Rate",value=f"""```{alert}
{a}{win_rate:.2f}%{b}
{users[str(user.id)]["win"]} / {users[str(user.id)]["total"]}```""",inline=True,)

    embed.add_field(name="Cashbox",value=f"""```fix
{cashbox}```""",inline=True)

    embed.add_field(name="Abilities",value=f"""```fix
{last}```""",inline=True)

    embed.add_field(name="\u200b",value="\u200b",inline= True)

    embed.add_field(name = "Playability" ,value=f"""```{alert2}
{minus} {banlock_last}```""",inline= True)

    embed.add_field(name="\u200b",value="""
{}⠀ ⠀{}⠀ ⠀{}⠀ ⠀{}⠀ ⠀{}⠀ ⠀{}⠀ ⠀{}⠀ ⠀{}⠀ ⠀{}⠀ ⠀{}⠀ ⠀{}⠀ ⠀{}""".format(all_badges[0],all_badges[1],all_badges[2],all_badges[3],all_badges[4],all_badges[5],all_badges[6],all_badges[7],all_badges[8],all_badges[9],all_badges[10],all_badges[11]),inline=False)

    embed.set_footer(text="""Shop is available!  o!shop""")

    if all_equal(all_badges):
        embed.remove_field(6)

    await ctx.send(embed=embed)

@Bot.command(pass_context = True)
@commands.cooldown(1, 5, commands.BucketType.member)
async def hideprofile(ctx):

    await open_json(ctx)

    await open_account(ctx.author,ctx)

    id = ctx.message.guild.id

    user = ctx.author

    users = await data(ctx)

    if int(users[str(user.id)]["Hide_The_Wallet"]) != 0 :

        users[str(user.id)]["Hide_The_Wallet"] -= 1 
        with open(f"{id}users.json", "w") as f:
            json.dump(users,f,indent=2)

        wallet_amt = int(users[str(user.id)]["wallet"])

        cashbox = int(users[str(user.id)]["cashbox_amount"])

        all_badges = []

        all_abilities = {}

        banlock = {}

        for key,value in (users[str(user.id)]["badge"]).items():
            if value is True:
                all_badges.append(key)
            else:
                all_badges.append("-")
        
        for key,value in (users[str(user.id)]).items():
            if key == "badge" or key == "cashbox_amount" or key == "name" or key == "wallet" or key == "win" or key == "total" :
                pass

            elif key == "BANNED" or key =="In_Jail":
                if value is True:
                    banlock[key] = value

            else:
                if value != 0 :
                    all_abilities[key] = value
                else:
                    continue

        try:
            win_rate = (users[str(user.id)]["win"] / users[str(user.id)]["total"]) * 100
        
        except:
            win_rate = 0

        string = json.dumps(all_abilities)
        string = string.replace("{" ," ")
        string = string.replace("}","")
        string = string.replace('"',"")
        string = string.replace("_"," ")
        last = string.replace(",","\n")

        banlock_string = json.dumps(banlock)
        banlock_string = banlock_string.replace("{" ,"")
        banlock_string = banlock_string.replace("}","")
        banlock_string = banlock_string.replace('"',"")
        banlock_string = banlock_string.replace("_"," ")
        banlock_string = banlock_string.replace(":","")
        banlock_string = banlock_string.replace("true","")
        banlock_last = banlock_string.replace(",","\n-")

        if len(banlock) == 0 :
            banlock_last = "Free"
            alert2 = "yaml"
            minus = ""
        
        else:
            minus = "-"
            alert2 = "diff"


        if last == " ":
            last = "No Abilities"
        
        embed = discord.Embed(color = discord.Color.green())

        embed.set_author(name = user.name,icon_url= user.avatar_url)

        alert = None

        if int(win_rate) < 50 :
            alert = "css"
            a = "["
            b = "]"
        else:
            alert = "yaml"
            a = ""
            b = ""
        
        embed.add_field(name="Wallet",value=f""" ```yaml
{wallet_amt} Coins```""",inline=True)

        embed.add_field(name="Win Rate",value=f"""```{alert}
{a}{win_rate:.2f}%{b}
{users[str(user.id)]["win"]} / {users[str(user.id)]["total"]}```""",inline=True,)

        embed.add_field(name="Cashbox",value=f"""```fix
{cashbox}```""",inline=True)

        embed.add_field(name="Abilities",value=f"""```fix
{last}```""",inline=True)

        embed.add_field(name="\u200b",value="\u200b",inline= True)

        embed.add_field(name = "Playability" ,value=f"""```{alert2}
{minus} {banlock_last}```""",inline= True)

        embed.add_field(name="\u200b",value="""
{}⠀ ⠀{}⠀ ⠀{}⠀ ⠀{}⠀ ⠀{}⠀ ⠀{}⠀ ⠀{}⠀ ⠀{}⠀ ⠀{}⠀ ⠀{}⠀ ⠀{}⠀ ⠀{}""".format(all_badges[0],all_badges[1],all_badges[2],all_badges[3],all_badges[4],all_badges[5],all_badges[6],all_badges[7],all_badges[8],all_badges[9],all_badges[10],all_badges[11]),inline=False)

        if all_equal(all_badges):
            embed.remove_field(6)

        await user.send(embed=embed)

    else :
        await ctx.send("Önce marketten alman lazım.")


# Earn

@Bot.command()
@commands.cooldown(1, 10800, commands.BucketType.member)
async def earn(ctx):

    id = ctx.message.guild.id

    await open_json(ctx)

    await open_account(ctx.author,ctx)

    users = await data(ctx)

    user = ctx.author

    if users[str(user.id)]["BANNED"] :
        await ctx.send("Banlısın!")
    
    else :

        earn = all_object[4][random.randint(0,1000)]

        await ctx.send(f"""```bash
"You earned {earn} coins!"
```""")

        users[str(user.id)]["wallet"] += earn

        with open(f"{id}users.json", "w") as f:
            json.dump(users,f,indent=2)
        
# Send Money

@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.member)
async def send(ctx,member:discord.Member, money = None ):

    id = ctx.message.guild.id

    await open_json(ctx)
    
    await open_account(ctx.author,ctx)

    await open_account(member,ctx)
    
    users = await data(ctx)

    user = ctx.author

    if users[str(user.id)]["BANNED"] :
        await ctx.send("Banlısın!")
    
    else :
        money = int(money)

        if money == None:
            await ctx.send("You must decide how many coins you want to send.")
        
        elif money < 0 :
            await ctx.send("WHATCHA TRYNA DO??")

        
        elif money > users[str(user.id)]["wallet"] :
            await ctx.send("""```css
[Even you got no that many coins.]```""")
        
        else :

            if member.id == 818200360819884062:
                users[str(user.id)]["wallet"] -= money
                users[str(member.id)]["wallet"] += money
                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)
                await ctx.send("""```bash
"Don't you have any friends? lol" 
```
:money_mouth:""".format(member.display_name,money,ctx.author.name))
                
            
            else :
                users[str(user.id)]["wallet"] -= money
                users[str(member.id)]["wallet"] += money
                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)
                await ctx.send("""```bash
"{}, got {} coins from {} "
```""".format(member.display_name,money,ctx.author.name))
    
# Rob Someone

@Bot.command()
@commands.cooldown(1, 86400, commands.BucketType.member)
async def rob(ctx,member:discord.Member):

    id = ctx.message.guild.id

    await open_json(ctx)

    await open_account(ctx.author,ctx)

    await open_account(member,ctx)
    
    users = await data(ctx)

    user = ctx.author

    if users[str(user.id)]["wallet"] < 1000:
        await ctx.send("""```css
[You must have 1000 coins to try rob someone!]
```""")
        rob.reset_cooldown(ctx)
    else :

        if member.id == 818200360819884062:
            await ctx.send(":eyes:")
            chance = random.randint(0,1)

            if chance == 0 :
                stolen = int((users[str(member.id)]["wallet"] * 3) / 10)
                users[str(user.id)]["wallet"] += stolen
                users[str(member.id)]["wallet"] -= stolen
                
                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)

                await ctx.send("""```fix
You stole the coins and running for your life!
```""")
                time.sleep(3)
                await ctx.send(f"""```bash
"{stolen} coins has stolen!" 
```
:face_with_symbols_over_mouth:""")
                
                

            else:
                
                users[str(user.id)]["wallet"] -= int(users[str(user.id)]["wallet"]) / 2
                users[str(member.id)]["wallet"] += int(users[str(user.id)]["wallet"])                                       
                with open(f"{id}users.json", "w") as f:
                            json.dump(users,f,indent=2)

                await ctx.send("""```css
[You could not make it and lost {} coins to your target.] 
```
:money_mouth: """.format(int(users[str(user.id)]["wallet"]),member.name))

        else :

            chance = random.randint(0,1)

            if chance == 0 :
                if int(users[str(member.id)]["Rob_Guard"]) != 0:
                    users[str(member.id)]["Rob_Guard"] -= 1

                    gone = (users[str(user.id)]["wallet"]) / 10

                    users[str(user.id)]["wallet"] -= gone

                    try :
                        users[str(818200360819884062)]["wallet"] += gone
                    except:
                        None

                    with open(f"{id}users.json", "w") as f:
                        json.dump(users,f,indent=2)
                    
                    await ctx.send(f"""```css
[{member.display_name} had a Rob Guard. You lost {int(gone)} coin.]
```""")
                else:

                
                    stolen = int((users[str(member.id)]["wallet"] * 3) / 10)

                    users[str(user.id)]["wallet"] += stolen
                    users[str(member.id)]["wallet"] -= stolen
                    with open(f"{id}users.json", "w") as f:
                        json.dump(users,f,indent=2)

                    await ctx.send("""```fix
You stole the coins and running for your life!
```""")
                    time.sleep(3)
                    await ctx.send(f"""```bash
"{stolen} coins has stolen!"
```""")
            else:
                users[str(user.id)]["wallet"] -= int(users[str(user.id)]["wallet"]) / 2
                users[str(member.id)]["wallet"] += int(users[str(user.id)]["wallet"])                                       
                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)

                await ctx.send("""```css
[You could not make it and lost {} coins to your target.]
```""".format(int(users[str(user.id)]["wallet"]),member.name))
    

# Lotto for 5 people

@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.member)
async def lotto5(ctx):

    id = ctx.message.guild.id

    await open_json(ctx)

    await open_account(ctx.author,ctx)

    users = await data(ctx)

    loto = await loto5_data(ctx)

    user = ctx.author

    if users[str(user.id)]["BANNED"] :
        await ctx.send("Banlısın!")
    
    else :

        if str(user.id) in list(loto.keys()):
            await ctx.send("""```fix
You already joined! 
```""")
        elif 200 > users[str(user.id)]["wallet"]:
            await ctx.send("""```css
[Not enough coin.]
```""")
        
        else :

            users[str(user.id)]["wallet"] -= 200

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f,indent=2)

            loto[str(user.id)] = {}
            loto[str(user.id)]["name"] = user.name

            with open(f"{id}loto5.json", "w") as f:
                json.dump(loto,f,indent=2)
        
        if len(list(loto.keys())) == 5 :
            lucky_index = random.randint(0,4)
            lucky_id = list(loto.keys())[lucky_index]

            embed = discord.Embed(description = """```fix
The winner is being selected!
```""")

            bb = discord.Embed(description="""```bash
"{}, has won 1000 coins!"
```""".format(loto[str(lucky_id)]["name"]))

            ab = await ctx.send(embed = embed)
            time.sleep(0.5)
            await ab.edit(embed = bb)

            users[str(lucky_id)]["wallet"] += 1000
            os.remove(f"{id}loto5.json")

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f,indent=2)

        else:
            await ctx.send("""```fix
{} has joined. Lotto will start when it's 5.
```""".format(len(list(loto.keys()))))

# Lotto for 3 people

@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.member)
async def lotto3(ctx):

    id = ctx.message.guild.id

    await open_json(ctx)

    await open_account(ctx.author,ctx)

    users = await data(ctx)

    loto = await loto3_data(ctx)

    user = ctx.author

    if users[str(user.id)]["BANNED"] :
        await ctx.send("Banlısın!")
    
    else :

    

        if str(user.id) in list(loto.keys()):
            await ctx.send("""```fix
You already joined! 
```""")
        elif 200 > users[str(user.id)]["wallet"]:
            await ctx.send("""```css
[Not enough coin.]
```""")
        
        else :

            users[str(user.id)]["wallet"] -= 200

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f,indent=2)

            loto[str(user.id)] = {}
            loto[str(user.id)]["name"] = user.name

            with open(f"{id}loto3.json", "w") as f:
                json.dump(loto,f,indent=2)
        
        if len(list(loto.keys())) == 3 :
            lucky_index = random.randint(0,2)
            lucky_id = list(loto.keys())[lucky_index]

            embed = discord.Embed(description = """```fix
The winner is being selected!
```""")

            bb = discord.Embed(description="""```bash
"{}, has won 600 coins!"
```""".format(loto[str(lucky_id)]["name"]))

            ab = await ctx.send(embed = embed)
            time.sleep(0.5)
            await ab.edit(embed = bb)

            users[str(lucky_id)]["wallet"] += 600
            os.remove(f"{id}loto3.json")

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f,indent=2)

        else:
            await ctx.send("""```fix
{} has joined. Lotto will start when it's 3.
```""".format(len(list(loto.keys()))))

# Shop

@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.member)
async def shop(ctx):
    embed = discord.Embed(color = discord.Color.green(),title = "Tike | Shop",description = """
**Abilities** ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀⠀ ⠀ **Badges**

:cyclone: 1. Rob Guard (1400C) ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀:bulb: 10. Bulb (100C)
:cyclone: 2. Cashbox Lvl.1 (5000C)⠀⠀⠀⠀⠀⠀⠀⠀⠀:gorilla: 11. Monke (500C)
:cyclone: 3. Cashbox Lvl.2 (9000C) ⠀⠀⠀⠀⠀⠀⠀⠀ :military_medal: 12. Medal (1000C)
:cyclone: 4. Cashbox Lvl.3 (15.000C) ⠀⠀⠀⠀⠀⠀⠀ :chess_pawn: 13. Pawn (3000C)
:cyclone: 5. Investigator Private (1000C) ⠀⠀⠀⠀⠀ :person_climbing: 14. Hustler (5000C)
:cyclone: 6. Investigator Public (500C)⠀⠀⠀⠀⠀⠀⠀:money_with_wings: 15. Bettor (8000C)
:cyclone: 7. Hide The Wallet (500C) ⠀⠀⠀⠀⠀⠀⠀⠀:crossed_swords: 16. Warrior (9000C)
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ :coin: 17. Cryptic (10.000C)
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ :milky_way: 18. Miami (11.000C)
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ :earth_americas: 19. Global (15.000C)
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ :crown: 20. King (20.000C)
Example: o!buy 1 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ :moyai: 21. Grandmaster (30.000C)
""")
    await ctx.send(embed = embed)

# Buy Something

@Bot.command()
@commands.cooldown(1, 3, commands.BucketType.member)
async def buy(ctx , itemid = None ):

    id = ctx.message.guild.id

    await open_account(ctx.author,ctx)

    users = await data(ctx)

    user = ctx.author

    if users[str(user.id)]["BANNED"] :
        await ctx.send("Banlısın!")
    
    else :

        itemid = int(itemid)

        if itemid == None:
            await ctx.send("Ne alacağını yazsana olum.")
        
        elif itemid == 1 :
            if users[str(user.id)]["wallet"] < 1400:
                await ctx.send("para yok")
            else:
                users[str(user.id)]["wallet"] -= 1400
                users[str(user.id)]["Rob_Guard"] += 1

                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)
                await ctx.send("Rob guard Aldın.")
        
        elif itemid == 2 :
            if users[str(user.id)]["Cashbox_Lvl"] == 0 :
                if users[str(user.id)]["wallet"] < 5000:
                    await ctx.send("Paran yok.")
                else:
                    users[str(user.id)]["wallet"] -= 5000
                    users[str(user.id)]["Cashbox_Lvl"] += 1
                    with open(f"{id}users.json", "w") as f:
                        json.dump(users,f,indent=2)
                    await ctx.send("LVL 1 cashbox aldın")
            else :
                await ctx.send("Cashboxını sadece yükseltebilirsin.")
        
        elif itemid == 3 :
            if users[str(user.id)]["Cashbox_Lvl"] == 1 :
                if users[str(user.id)]["wallet"] < 9000:
                    await ctx.send("Paran yok.")
                else :
                    users[str(user.id)]["wallet"] -= 9000
                    users[str(user.id)]["Cashbox_Lvl"] += 1
                    with open(f"{id}users.json", "w") as f:
                        json.dump(users,f,indent=2)
                    await ctx.send("Cashbox lvl2 ye yükseltildi")
            else :
                await ctx.send("Cashboxını sadece yükseltebilirsin.")
            
        elif itemid == 4 :
            if users[str(user.id)]["Cashbox_Lvl"] == 2 :
                if users[str(user.id)]["wallet"] < 15000:
                    await ctx.send("Paran yok.")
                else :
                    users[str(user.id)]["wallet"] -= 15000
                    users[str(user.id)]["Cashbox_Lvl"] += 1
                    with open(f"{id}users.json", "w") as f:
                        json.dump(users,f,indent=2)
                    await ctx.send("Cashbox lvl3 e yükseltildi")
        
            else :
                await ctx.send("Cashboxını sadece yükseltebilirsin.")
        
        elif itemid == 5:
            if users[str(user.id)]["wallet"] < 1000:
                    await ctx.send("Paran yok.")
            else:
                users[str(user.id)]["wallet"] -= 1000
                users[str(user.id)]["Investigator_Private"] += 1
                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)
                await ctx.send("Investigator  aldin")
        
        elif itemid == 6 :
            if users[str(user.id)]["wallet"] < 500:
                await ctx.send("Paran yok.")
            else:
                users[str(user.id)]["wallet"] -= 500
                users[str(user.id)]["Investigator_Public"] += 1
                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)
                await ctx.send("Investigator_Public aldin")
        
        elif itemid == 7 :
            if users[str(user.id)]["wallet"] < 500:
                await ctx.send("Paran yok.")
            else:
                users[str(user.id)]["wallet"] -= 500
                users[str(user.id)]["Hide_The_Wallet"] += 1
                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)
                await ctx.send("hide wallet aldın")
        
        elif itemid == 10 :
            if users[str(user.id)]["wallet"] < 100:
                await ctx.send("Paran yok.")
            else:
                if users[str(user.id)]["badge"][":bulb:"] == True:
                    await ctx.send("Zaten var")
                else:
                    users[str(user.id)]["wallet"] -= 100
                    users[str(user.id)]["badge"][":bulb:"] = True
                    with open(f"{id}users.json", "w") as f:
                        json.dump(users,f,indent=2)
                    await ctx.send("Bulb aldın")
        
        elif itemid == 11 :
            if users[str(user.id)]["wallet"] < 500:
                await ctx.send("Paran yok.")
            else:
                if users[str(user.id)]["badge"][":gorilla:"] == True:
                    await ctx.send("Zaten var.")
                else:
                    users[str(user.id)]["wallet"] -= 500
                    users[str(user.id)]["badge"][":gorilla:"] = True
                    with open(f"{id}users.json", "w") as f:
                        json.dump(users,f,indent=2)
                    await ctx.send("Monke Aldın.")
        
        elif itemid == 12 :
            if users[str(user.id)]["wallet"] < 1000:
                await ctx.send("Paran yok.")
            else:
                if users[str(user.id)]["badge"][":military_medal:"] == True:
                    await ctx.send("Zaten var.")
                else:
                    users[str(user.id)]["wallet"] -= 1000
                    users[str(user.id)]["badge"][":military_medal:"] = True
                    with open(f"{id}users.json", "w") as f:
                        json.dump(users,f,indent=2)
                    await ctx.send(":military_medal:")
        
        elif itemid == 13 :
            if users[str(user.id)]["wallet"] < 3000:
                await ctx.send("Paran yok.")
            else:
                if users[str(user.id)]["badge"][":chess_pawn:"] == True:
                    await ctx.send("Zaten var.")
                else:
                    users[str(user.id)]["wallet"] -= 100
                    users[str(user.id)]["badge"][":chess_pawn:"] = True
                    with open(f"{id}users.json", "w") as f:
                        json.dump(users,f,indent=2)
                    await ctx.send("Pawn aldın")
        
        elif itemid == 14 :
            if users[str(user.id)]["wallet"] < 5000:
                await ctx.send("Paran yok.")
            else:
                if users[str(user.id)]["badge"][":person_climbing:"] == True:
                    await ctx.send("Zaten var.")
                else:
                    users[str(user.id)]["wallet"] -= 100
                    users[str(user.id)]["badge"][":person_climbing:"] = True
                    with open(f"{id}users.json", "w") as f:
                        json.dump(users,f,indent=2)
                    await ctx.send("Hustler aldın")
        
        elif itemid == 15 :
            if users[str(user.id)]["wallet"] < 8000:
                await ctx.send("Paran yok.")
            else:
                if users[str(user.id)]["badge"][":money_with_wings:"] == True:
                    await ctx.send("Zaten var.")
                else:
                    users[str(user.id)]["wallet"] -= 100
                    users[str(user.id)]["badge"][":money_with_wings:"] = True
                    with open(f"{id}users.json", "w") as f:
                        json.dump(users,f,indent=2)
                    await ctx.send("Bettor aldın")
        
        elif itemid == 16 :
            if users[str(user.id)]["wallet"] < 9000:
                await ctx.send("Paran yok.")
            else:
                if users[str(user.id)]["badge"][":crossed_swords:"] == True:
                    await ctx.send("zaten var")
                else:
                    users[str(user.id)]["wallet"] -= 100
                    users[str(user.id)]["badge"][":crossed_swords:"] = True
                    with open(f"{id}users.json", "w") as f:
                        json.dump(users,f,indent=2)
                    await ctx.send("Warrior aldın")
        
        
        elif itemid == 17 :
            if users[str(user.id)]["wallet"] < 10000:
                await ctx.send("Paran yok.")
            else:
                if users[str(user.id)]["badge"][":coin:"] == True:
                    await ctx.send("zaten var")
                else:
                    users[str(user.id)]["wallet"] -= 100
                    users[str(user.id)]["badge"][":coin:"] = True
                    with open(f"{id}users.json", "w") as f:
                        json.dump(users,f,indent=2)
                    await ctx.send("Cryptic aldın")
        
        elif itemid == 18 :
            if users[str(user.id)]["wallet"] < 11000:
                await ctx.send("Paran yok.")
            else:
                if users[str(user.id)]["badge"][":milky_way:"] == True:
                    await ctx.send("zaten var")
                else:
                    users[str(user.id)]["wallet"] -= 100
                    users[str(user.id)]["badge"][":milky_way:"] = True
                    with open(f"{id}users.json", "w") as f:
                        json.dump(users,f,indent=2)
                    await ctx.send("Miami aldın")
        
        elif itemid == 19 :
            if users[str(user.id)]["wallet"] < 15000:
                await ctx.send("Paran yok.")
            else:
                if users[str(user.id)]["badge"][":earth_americas:"] == True:
                    await ctx.send("Zaten var")
                else:
                    users[str(user.id)]["wallet"] -= 100
                    users[str(user.id)]["badge"][":earth_americas:"] = True
                    with open(f"{id}users.json", "w") as f:
                        json.dump(users,f,indent=2)
                    await ctx.send("Global aldın")
        
        elif itemid == 20 :
            if users[str(user.id)]["wallet"] < 20000:
                await ctx.send("Paran yok.")
            else:
                if users[str(user.id)]["badge"][":crown:"] == True:
                    await ctx.send("Zaten var")
                else:
                    users[str(user.id)]["wallet"] -= 100
                    users[str(user.id)]["badge"][":crown:"] = True
                    with open(f"{id}users.json", "w") as f:
                        json.dump(users,f,indent=2)
                    await ctx.send("King aldın")
        
        elif itemid == 21 :
            if users[str(user.id)]["wallet"] < 30000:
                await ctx.send("Paran yok.")
            else:
                if users[str(user.id)]["badge"][":moyai:"] == True:
                    await ctx.send("Zaten var")
                else:
                    users[str(user.id)]["wallet"] -= 100
                    users[str(user.id)]["badge"][":moyai:"] = True
                    with open(f"{id}users.json", "w") as f:
                        json.dump(users,f,indent=2)
                    await ctx.send("Grandmaster aldın")
        
        else :
            await ctx.send("Böyle bir item yok.")
            

@Bot.command()
@commands.cooldown(1, 10800, commands.BucketType.member)
async def cashbox(ctx,money = 0):

    users = await data(ctx)

    user = ctx.author

    if users[str(user.id)]["BANNED"] :
        await ctx.send("Banlısın!")
    
    else :

        if money == 0 :
            await ctx.send("Yatırmak istediğin tutarı gir.")
        elif money < 0 :
            await ctx.send("?")
        else :
            id = ctx.message.guild.id

            await open_account(ctx.author,ctx)

            Cashbox_Lvl = int(users[str(user.id)]["Cashbox_Lvl"])

            if money > int(users[str(user.id)]["wallet"]):
                await ctx.send("paran yok")
            
            else :
                if Cashbox_Lvl == 0 :
                    await ctx.send("Cashboxın yok")
                elif Cashbox_Lvl == 1 :
                    if money + int(users[str(user.id)]["cashbox_amount"]) > 12000 :
                        await ctx.send("lvl1 cashbox 12k tutabilir.")
                    
                    else :
                        users[str(user.id)]["cashbox_amount"] += money
                        users[str(user.id)]["wallet"] -= money
                        with open(f"{id}users.json", "w") as f:
                            json.dump(users,f,indent=2)
                        await ctx.send(f"{money} cashboxa aktarıldı.")
                elif Cashbox_Lvl == 2 :
                    if money + int(users[str(user.id)]["cashbox_amount"]) > 20000 :
                        await ctx.send("lvl2 cashbox 20k tutabilir.")
                    
                    else :
                        users[str(user.id)]["cashbox_amount"] += money
                        users[str(user.id)]["wallet"] -= money
                        with open(f"{id}users.json", "w") as f:
                            json.dump(users,f,indent=2)
                        await ctx.send(f"{money} cashboxa aktarıldı.")
                elif Cashbox_Lvl == 3 :
                    if money + int(users[str(user.id)]["cashbox_amount"]) > 50000 :
                        await ctx.send("lvl3 cashbox 50k tutabilir.")
                    
                    else :
                        users[str(user.id)]["cashbox_amount"] += money
                        users[str(user.id)]["wallet"] -= money
                        with open(f"{id}users.json", "w") as f:
                            json.dump(users,f,indent=2)
                        await ctx.send(f"{money} cashboxa aktarıldı.")
                else :
                    await ctx.send("Sorun var.")

@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.member)
async def withdraw(ctx,money = 0):

    users = await data(ctx)

    user = ctx.author

    if users[str(user.id)]["BANNED"] :
        await ctx.send("Banlısın!")
    
    else :

        if money == 0 :
            await ctx.send("Cekmek istediğin parayı gir")
        elif money < 0 :
            await ctx.send("?")
        else :
            id = ctx.message.guild.id

            await open_account(ctx.author,ctx)

            

            if money > int(users[str(user.id)]["cashbox_amount"]):
                await ctx.send("Para yok.")
            else :
                users[str(user.id)]["cashbox_amount"] -= money
                users[str(user.id)]["wallet"] += money
                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f,indent=2)
                await ctx.send(f"{money} hesabına aktarıldı.")


@Bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.member)
async def investigator(ctx,member:discord.Member = None):

    id = ctx.message.guild.id

    users = await data(ctx)

    user = ctx.author

    if users[str(user.id)]["BANNED"] :
        await ctx.send("Banlısın!")
    
    else :

        if users[str(user.id)]["Investigator_Private"] > 0:

            if member == None:
                await ctx.send("Kimi Investigatorlemek istiyorsun")
            else:
                await info(ctx,member,id)
            
        else :
            await ctx.send("Önce marketten alman lazım")

@Bot.command(pass_context=True)
@commands.cooldown(1, 3, commands.BucketType.member)
async def investigatorp(ctx,member:discord.Member = None):

    id = ctx.message.guild.id

    users = await data(ctx)

    user = ctx.author

    if users[str(user.id)]["BANNED"] :
        await ctx.send("Banlısın!")
    
    else :

        if users[str(user.id)]["Investigator_Public"] > 0:

            if member == None:
                await ctx.send("Kimi Investigatorlemek istiyorsun")
            else:
                await info_p(ctx,member,id)
                
        
        else :
            await ctx.send("Önce marketten alman lazım")


@send.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('No such user here.')

@send.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Hold up, gentleman!",description=f"Take a breath for {(error.retry_after):.2f} secs.", color=discord.Color.red())
        delayed = await ctx.send(embed=em)
        time.sleep(error.retry_after)
        await delayed.delete()

@earn.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"You got your coins already!",description=f"Try again after {int((error.retry_after // 3600))} hours and {((error.retry_after % 3600) // 60):.2f} minutes. ", color=discord.Color.red())
        await ctx.send(embed=em)
    
@slot1.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await slot1(ctx,money=50)
        em = discord.Embed(title=f"You greedy!",description=f"After {int((error.retry_after // 3600))} hours and {((error.retry_after % 3600) // 60):.2f} minutes, you will get 10 more Tier 1 Slot spin try. ", color=discord.Color.red())
        await ctx.send(embed=em)

@racebet.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Out Of Gas!",description=f"Next 3 races after {int((error.retry_after // 3600))} hours and {((error.retry_after % 3600) // 60):.2f} minutes.", color=discord.Color.red())
        await ctx.send(embed=em)

@rob.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Hush!",description=f"""You better be stay at home tonight. Wait for **{int((error.retry_after // 3600))} ** hours and **{((error.retry_after % 3600) // 60):.2f} ** minutes. 
        If you couldn't write the user's name first time, you'll lose your allowance to rob. **This is serious.**""", color=discord.Color.red())
        await ctx.send(embed=em)

@slot2.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Slow Down!",description=f"Take a breath for {(error.retry_after):.2f} secs.", color=discord.Color.red())
        delayed = await ctx.send(embed=em)
        time.sleep(error.retry_after)
        await delayed.delete()
    
@slot3.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Slow Down!",description=f"Take a breath for {(error.retry_after):.2f} secs.", color=discord.Color.red())
        delayed = await ctx.send(embed=em)
        time.sleep(error.retry_after)
        await delayed.delete()

@slot4.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Slow Down!",description=f"Take a breath for {(error.retry_after):.2f} secs.", color=discord.Color.red())
        delayed = await ctx.send(embed=em)
        time.sleep(error.retry_after)
        await delayed.delete()

@price.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Slow Down!",description=f"Take a breath for {(error.retry_after):.2f} secs.", color=discord.Color.red())
        delayed = await ctx.send(embed=em)
        time.sleep(error.retry_after)
        await delayed.delete()

@help.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Slow Down!",description=f"Take a breath for {(error.retry_after):.2f} secs.", color=discord.Color.red())
        delayed = await ctx.send(embed=em)
        time.sleep(error.retry_after)
        await delayed.delete()

@prob.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Slow Down!",description=f"Take a breath for {(error.retry_after):.2f} secs.", color=discord.Color.red())
        delayed = await ctx.send(embed=em)
        time.sleep(error.retry_after)
        await delayed.delete()

@profile.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Slow Down!",description=f"Take a breath for {(error.retry_after):.2f} secs.", color=discord.Color.red())
        delayed = await ctx.send(embed=em)
        time.sleep(error.retry_after)
        await delayed.delete()

@hideprofile.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Slow Down!",description=f"Take a breath for {(error.retry_after):.2f} secs.", color=discord.Color.red())
        delayed = await ctx.send(embed=em)
        time.sleep(error.retry_after)
        await delayed.delete()

@send.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Slow Down!",description=f"Take a breath for {(error.retry_after):.2f} secs.", color=discord.Color.red())
        delayed = await ctx.send(embed=em)
        time.sleep(error.retry_after)
        await delayed.delete()

@lotto5.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Slow Down!",description=f"Take a breath for {(error.retry_after):.2f} secs.", color=discord.Color.red())
        delayed = await ctx.send(embed=em)
        time.sleep(error.retry_after)
        await delayed.delete()

@lotto3.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Slow Down!",description=f"Take a breath for {(error.retry_after):.2f} secs.", color=discord.Color.red())
        delayed = await ctx.send(embed=em)
        time.sleep(error.retry_after)
        await delayed.delete()

@shop.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Slow Down!",description=f"Take a breath for {(error.retry_after):.2f} secs.", color=discord.Color.red())
        delayed = await ctx.send(embed=em)
        time.sleep(error.retry_after)
        await delayed.delete()

@buy.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Slow Down!",description=f"Take a breath for {(error.retry_after):.2f} secs.", color=discord.Color.red())
        delayed = await ctx.send(embed=em)
        time.sleep(error.retry_after)
        await delayed.delete()

@cashbox.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Slow Down!",description=f"Try again after {int((error.retry_after // 3600))} hours and {((error.retry_after % 3600) // 60):.2f} minutes. ", color=discord.Color.red())
        delayed = await ctx.send(embed=em)
        time.sleep(error.retry_after)
        await delayed.delete()

@withdraw.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Slow Down!",description=f"Take a breath for {(error.retry_after):.2f} secs.", color=discord.Color.red())
        delayed = await ctx.send(embed=em)
        time.sleep(error.retry_after)
        await delayed.delete()

@investigator.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Slow Down!",description=f"Take a breath for {(error.retry_after):.2f} secs.", color=discord.Color.red())
        delayed = await ctx.send(embed=em)
        time.sleep(error.retry_after)
        await delayed.delete()

@investigatorp.error
async def command_name_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Slow Down!",description=f"Take a breath for {(error.retry_after):.2f} secs.", color=discord.Color.red())
        delayed = await ctx.send(embed=em)
        time.sleep(error.retry_after)
        await delayed.delete()


@Bot.event
async def on_ready():
    activity = discord.Game(name="o!help", type=3)
    await Bot.change_presence(activity=activity)


Bot.run("ODI1NzQwOTEyNDQ5MjkwMjYx.YGCVJw.vm1iWO-EYpmZ5WPmuta-LZTbibM")