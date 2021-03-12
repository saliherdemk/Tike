import random
import discord
from discord.ext import  commands
import json
import asyncio
from discord.ext.commands.core import command
import time
import lists
import os

Bot = commands.Bot(command_prefix='o!', help_command=None)

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
                        json.dump(users,f)
                
                    emoji_result = None

                    earned = 0

                    a = all_list[0][random.randint(0,101)]

                    

                    if a == ":new_moon: | :new_moon: | :new_moon:":
                        emoji_result = ":star2: Congratulations! :star2:"
                        
                        earned = 20

                        users[str(user.id)]["wallet"] += 20
                        users[str(user.id)]["win"] += 1

                        with open(f"{id}users.json", "w") as f:
                            json.dump(users,f)


                    elif a == ":waning_crescent_moon: | :waning_crescent_moon: | :waning_crescent_moon:":
                        emoji_result = ":star2: Congratulations! :star2:"
                        
                        earned = 25

                        users[str(user.id)]["wallet"] += 25
                        users[str(user.id)]["win"] += 1

                        with open(f"{id}users.json", "w") as f:
                            json.dump(users,f)

                    elif a == ":last_quarter_moon: | :last_quarter_moon: | :last_quarter_moon:":
                        emoji_result = ":star2: Congratulations! :star2:"
                        
                        earned = 50

                        users[str(user.id)]["wallet"] += 50
                        users[str(user.id)]["win"] += 1

                        with open(f"{id}users.json", "w") as f:
                            json.dump(users,f)

                    elif a == ":full_moon: | :full_moon: | :full_moon:":
                        emoji_result = ":star2: Congratulations! :star2:"
                        
                        earned = 100

                        users[str(user.id)]["wallet"] += 100
                        users[str(user.id)]["win"] += 1

                        with open(f"{id}users.json", "w") as f:
                            json.dump(users,f)

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
            json.dump(users,f)

        emoji_result = None

        earned = 0

        

        if a == ":new_moon: | :new_moon: | :new_moon:":
            emoji_result = ":star2: Congratulations! :star2:"
            
            earned = 20

            users[str(user.id)]["wallet"] += 20
            users[str(user.id)]["win"] += 1

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f)

        elif a == ":waning_crescent_moon: | :waning_crescent_moon: | :waning_crescent_moon:":
            emoji_result = ":star2: Congratulations! :star2:"
            
            earned = 25

            users[str(user.id)]["wallet"] += 25
            users[str(user.id)]["win"] += 1

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f)

        elif a == ":last_quarter_moon: | :last_quarter_moon: | :last_quarter_moon:":
            emoji_result = ":star2: Congratulations! :star2:"
           
            earned = 50

            users[str(user.id)]["wallet"] += 50
            users[str(user.id)]["win"] += 1

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f)

        elif a == ":full_moon: | :full_moon: | :full_moon:":
            emoji_result = ":star2: Congratulations! :star2:"
            
            earned = 100


            users[str(user.id)]["wallet"] += 100
            users[str(user.id)]["win"] += 1

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f)

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

    if users[str(user.id)]["wallet"] < 100 :
        await ctx.send("""```css
[Not enough coin.]```""")
    else :

        users[str(user.id)]["wallet"] -= 100
        users[str(user.id)]["total"] += 1 

        with open(f"{id}users.json", "w") as f:
                json.dump(users,f)

        a = all_list[1][random.randint(0,100)]
        
        emoji_result = None
        earned = 0

        if a == ":one: | :one: | :one:":
            emoji_result = ":star2: Congratulations! :star2:"

            earned = 50

            users[str(user.id)]["wallet"] += 50
            users[str(user.id)]["win"] += 1

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f)

        elif a == ":two: | :two: | :two:":
            emoji_result = ":star2: Congratulations! :star2:"

            earned = 100

            users[str(user.id)]["wallet"] += 100
            users[str(user.id)]["win"] += 1

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f)

        elif a == ":three: | :three: | :three:":
            emoji_result = ":star2: Congratulations! :star2:"

            earned = 160

            users[str(user.id)]["wallet"] += 160
            users[str(user.id)]["win"] += 1

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f)

        elif a == ":four: | :four: | :four:":
            emoji_result = ":star2: Congratulations! :star2:"

            earned = 200

            users[str(user.id)]["wallet"] += 200
            users[str(user.id)]["win"] += 1

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f)
        
        elif a == ":five: | :five: | :five:":
            emoji_result = ":star2: Congratulations! :star2:"

            earned = 250

            users[str(user.id)]["wallet"] += 250
            users[str(user.id)]["win"] += 1

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f)

        elif a == ":six: | :six: | :six:":
            emoji_result = ":star2: Congratulations! :star2:"

            earned = 350

            users[str(user.id)]["wallet"] += 350
            users[str(user.id)]["win"] += 1

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f)

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

    if users[str(user.id)]["wallet"] < 250 :
        await ctx.send("""```css
[Not enough coin.]```""")
    else :
        users[str(user.id)]["wallet"] -= 250
        users[str(user.id)]["total"] += 1 

        with open(f"{id}users.json", "w") as f:
                json.dump(users,f)

        a = all_list[2][random.randint(0,100)]
        
        emoji_result = None

        earned = 0

        if a == ":pirate_flag: | :pirate_flag: | :pirate_flag:":
            emoji_result = ":star2: Congratulations! :star2:"
            
            earned = 225

            users[str(user.id)]["wallet"] += 225
            users[str(user.id)]["win"] += 1

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f)

        elif a == ":dollar: | :dollar: | :dollar:":
            emoji_result = ":star2: Congratulations! :star2:"
            
            earned = 325

            users[str(user.id)]["wallet"] += 325
            users[str(user.id)]["win"] += 1

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f)

        elif a == ":moneybag: | :moneybag: | :moneybag:":
            emoji_result = ":star2: Congratulations! :star2:"
            
            earned = 400

            users[str(user.id)]["wallet"] += 400
            users[str(user.id)]["win"] += 1

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f)

        elif a == ":trident: | :trident: | :trident:":
            emoji_result = ":star2: Congratulations! :star2:"
            
            earned = 500

            users[str(user.id)]["wallet"] += 500
            users[str(user.id)]["win"] += 1

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f)
        
        elif a == ":fleur_de_lis: | :fleur_de_lis: | :fleur_de_lis:":
            emoji_result = ":star2: Congratulations! :star2:"
            
            earned = 500

            users[str(user.id)]["wallet"] += 500
            users[str(user.id)]["win"] += 1

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f)

        elif a == ":black_joker: | :black_joker: | :black_joker:":
            emoji_result = ":star2: Congratulations! :star2:"
            
            earned = 800

            users[str(user.id)]["wallet"] += 800
            users[str(user.id)]["win"] += 1

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f)
            
        elif a == ":gift: | :gift: | :gift:":
            emoji_result = ":star2: Congratulations! :star2:"
           
            earned = 1250

            users[str(user.id)]["wallet"] += 1250
            users[str(user.id)]["win"] += 1

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f)

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
            json.dump(users,f)

        emoji_result = None

        earned = 0

        if a == ":soccer: | :soccer: | :soccer:" or a == ":basketball: | :basketball: | :basketball:" or a == ":football: | :football: | :football:" or a == ":baseball: | :baseball: | :baseball:":
            emoji_result = ":star2: Congratulations! :star2:"
            
            earned = money * 2

            users[str(user.id)]["wallet"] += money * 2
            users[str(user.id)]["win"] += 1

            with open(f"{id}users.json", "w") as f:
                json.dump(users,f)

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



@Bot.command(pass_context = True)
@commands.cooldown(3, 86400, commands.BucketType.member)
async def racebet(ctx,money = 0):

    id = ctx.message.guild.id

    await open_account(ctx.author,ctx)

    users = await data(ctx)

    user = ctx.author
    
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
                    chose = "::taxi::"
                    await delete1.delete()
                    await delete2.delete()
                else :
                    liste = [":red_car:",":taxi:",":taxi:"]
                    randomly = liste[random.randint(0,2)]
                    chose = randomly
                    await ctx.send(f"Randomly {randomly} has been chosen.")
                    
                money = int(money)

                users[str(user.id)]["wallet"] -= money
                users[str(user.id)]["total"] += 1
                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f)
                
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
                        json.dump(users,f)
                    
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
                        json.dump(users,f)
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
                        json.dump(users,f)
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
                
        

        


@Bot.command(pass_context = True)
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

@Bot.command()
async def prob(ctx):
    embed = discord.Embed(color = discord.Color.green(),title = "Tike | Prob",description ="""
**Tier 1 Slot**⠀ ⠀⠀ ⠀     ⠀ ⠀⠀**Tier 2 Slot**    
%40 - 20 Coins⠀ ⠀⠀ ⠀%30 - 50 Coins
%25 - 25 Coins⠀ ⠀⠀ ⠀      %13 - 100 Coins
%10 - 50 Coins⠀ ⠀⠀ ⠀      %7 - 160 Coins
%5 - 100 Coins⠀ ⠀⠀ ⠀      %5 - 200 Coins
 ⠀ ⠀⠀ ⠀      ⠀ ⠀⠀ ⠀      ⠀ ⠀⠀ ⠀%3 - 250 Coins
 ⠀ ⠀⠀ ⠀      ⠀ ⠀⠀ ⠀      ⠀ ⠀⠀ ⠀%2 - 350 Coins
    
**Tier 3 Slot**⠀ ⠀⠀ ⠀ ⠀ ⠀⠀**Tier 4 Slot**⠀ ⠀⠀ ⠀      
%21 - 200 Coins⠀ ⠀⠀ ⠀%20 - Win
%8 - 325 Coins⠀ ⠀⠀ ⠀ **Car Race**
%6 - 400 Coins⠀ ⠀⠀ ⠀ %33,3 - Win
%5 - 500 Coins⠀ ⠀⠀ ⠀ **Lotto**
%5 - 500 Coins⠀ ⠀⠀ ⠀ %20 - Win
%4 - 800 Coins⠀ ⠀⠀ ⠀ **Earn** 
%1 - 1250 Coins⠀ ⠀⠀ ⠀ %70 - 100 ~~ %0,1 - 100000 Coins (Big Prize)     
""")
    await ctx.send(embed = embed)


@Bot.command(pass_context = True)
async def profile(ctx):

    await open_json(ctx)

    await open_account(ctx.author,ctx)

    user = ctx.author

    users = await data(ctx)

    wallet_amt = int(users[str(user.id)]["wallet"])

    try:
        win_rate = (users[str(user.id)]["win"] / users[str(user.id)]["total"]) * 100
       
    except:
        win_rate = 0
    
    embed = discord.Embed(color = discord.Color.green(),title = f"""Bag of coins: {wallet_amt} *Coins* """ ,description = f"""Win Rate: {win_rate:.2f} %""")
    
    embed.set_author(name = user.name,icon_url= user.avatar_url )

    await ctx.send(embed=embed)


@Bot.command()
@commands.cooldown(1, 10800, commands.BucketType.member)
async def earn(ctx):

    id = ctx.message.guild.id

    await open_json(ctx)

    await open_account(ctx.author,ctx)

    users = await data(ctx)

    user = ctx.author

    earn = all_object[4][random.randint(0,1000)]

    await ctx.send(f"""```bash
"You earned {earn} coins!"
```""")

    users[str(user.id)]["wallet"] += earn

    with open(f"{id}users.json", "w") as f:
        json.dump(users,f)
        
@Bot.command()
@commands.cooldown(1, 5, commands.BucketType.member)
async def send(ctx,member:discord.Member, money = None ):

    id = ctx.message.guild.id

    await open_json(ctx)
    
    await open_account(ctx.author,ctx)

    await open_account(member,ctx)
    
    users = await data(ctx)

    user = ctx.author
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
                json.dump(users,f)
            await ctx.send("""```bash
"Don't you have any friends? lol" 
```
:money_mouth:""".format(member.display_name,money,ctx.author.name))
            
        
        else :
            users[str(user.id)]["wallet"] -= money
            users[str(member.id)]["wallet"] += money
            with open(f"{id}users.json", "w") as f:
                json.dump(users,f)
            await ctx.send("""```bash
"{}, got {} coins from {} "
```""".format(member.display_name,money,ctx.author.name))
    

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
                users[str(user.id)]["wallet"] += int(users[str(member.id)]["wallet"] * 3 / 10)
                users[str(member.id)]["wallet"] -= int(users[str(member.id)]["wallet"] * 3 / 10)
                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f)
                await ctx.send("""```fix
You stole the coins and running for your life!
```""")
                time.sleep(3)
                await ctx.send(f"""```bash
"{int(users[str(member.id)]["wallet"] * 3 / 10)} coins has stolen!" 
```
:face_with_symbols_over_mouth:""")
            else:
                users[str(user.id)]["wallet"] -= int(users[str(user.id)]["wallet"]) / 2
                users[str(member.id)]["wallet"] += int(users[str(user.id)]["wallet"])                                       
                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f)
                await ctx.send("""```css
[You could not make it and lost {} coins to your target.] 
```
:money_mouth: """.format(int(users[str(user.id)]["wallet"]),member.name))

        else :

            chance = random.randint(0,1)

            if chance == 0 :
                users[str(user.id)]["wallet"] += int(users[str(member.id)]["wallet"] * 3 / 10)
                users[str(member.id)]["wallet"] -= int(users[str(member.id)]["wallet"] * 3 / 10)
                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f)
                await ctx.send("""```fix
You stole the coins and running for your life!
```""")
                time.sleep(3)
                await ctx.send(f"""```bash
"{int(users[str(member.id)]["wallet"] * 3 / 10)} coins has stolen!"
```""")
            else:
                users[str(user.id)]["wallet"] -= int(users[str(user.id)]["wallet"]) / 2
                users[str(member.id)]["wallet"] += int(users[str(user.id)]["wallet"])                                       
                with open(f"{id}users.json", "w") as f:
                    json.dump(users,f)
                await ctx.send("""```css
[You could not make it and lost {} coins to your target.]
```""".format(int(users[str(user.id)]["wallet"]),member.name))


@Bot.command()
async def lotto5(ctx):

    id = ctx.message.guild.id

    await open_json(ctx)

    await open_account(ctx.author,ctx)

    users = await data(ctx)

    loto = await loto_data(ctx)

    user = ctx.author

    

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
            json.dump(users,f)

        loto[str(user.id)] = {}
        loto[str(user.id)]["money"] = 200
        loto[str(user.id)]["name"] = user.name

        with open(f"{id}loto.json", "w") as f:
            json.dump(loto,f)
    
    if len(list(loto.keys())) == 5 :
        lucky_index = random.randint(1,5)
        lucky_id = list(loto.keys())[lucky_index]

        embed = discord.Embed(description = """```fix
The winner is being selected!
```""")

        bb = discord.Embed("""```bash
"{}, has won 1000 coins!"
```""".format(loto[str(lucky_id)]["name"]))

        ab = await ctx.send(embed = embed)
        time.sleep(0.5)
        await ab.edit(embed = bb)

        loto[str(lucky_id)]["money"] += 1000
        os.remove(f"{id}loto.json")

        with open(f"{id}loto.json", "w") as f:
            json.dump(loto,f)

        with open(f"{id}users.json", "w") as f:
            json.dump(users,f)

    else:
        await ctx.send("""```fix
{} has joined. Lotto will start when it's 5.
```""".format(len(list(loto.keys()))))
                

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

    
@Bot.event
async def on_ready():
    activity = discord.Game(name="o!help", type=3)
    await Bot.change_presence(activity=activity)

async def open_account(user,ctx):

    id = ctx.message.guild.id

    users = await data(ctx)

    with open(f"{id}users.json", "r") as f:
        users = json.load(f)

    if str(user.id ) in users :
        return False
    else :
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 350
        users[str(user.id)]["win"] = 0
        users[str(user.id)]["total"] = 0
    
    with open(f"{id}users.json", "w") as f:
        json.dump(users,f)
    
    return True

async def data(ctx):
    id = ctx.message.guild.id

    with open(f"{id}users.json", "r") as f:
        users = json.load(f)
    
    return users

async def loto_data(ctx):
    id = ctx.message.guild.id

    with open(f"{id}loto.json", "r") as f:
        loto = json.load(f)
    
    return loto

async def open_json(ctx):
    id = ctx.message.guild.id
    if os.path.exists(f"{id}users.json"):
        None
    else :
        with open(f"{id}users.json", "w+") as f:
            f.write("{}")
    if os.path.exists(f"{id}loto.json"):
        None
    else :
        with open(f"{id}loto.json", "w+") as f:
            f.write("{}")





Bot.run("TOKEN")