import json
import os
import discord
from numpy.core.shape_base import block
from itertools import groupby

async def open_account(user,ctx):

    id = ctx.message.guild.id

    users = await data(ctx)

    with open(f"{id}users.json", "r") as f:
        users = json.load(f)

    if str(user.id ) in users :
        return False
    else :
        users[str(user.id)] = {}
        users[str(user.id)]["name"] = user.name
        users[str(user.id)]["wallet"] = 350
        users[str(user.id)]["win"] = 0
        users[str(user.id)]["total"] = 0
        users[str(user.id)]["Rob_Guard"] = 0
        users[str(user.id)]["Cashbox_Lvl"] = 0
        users[str(user.id)]["cashbox_amount"] = 0
        users[str(user.id)]["Investigator_Public"] = 0   
        users[str(user.id)]["Investigator_Private"] = 0
        users[str(user.id)]["Hide_The_Wallet"] = 0
        users[str(user.id)]["badge"] = {}
        users[str(user.id)]["BANNED"] = False
        users[str(user.id)]["badge"][":bulb:"] = False
        users[str(user.id)]["badge"][":gorilla:"]= False
        users[str(user.id)]["badge"][":military_medal:"]= False
        users[str(user.id)]["badge"][":chess_pawn:"]= False
        users[str(user.id)]["badge"][":person_climbing:"]= False
        users[str(user.id)]["badge"][":money_with_wings:"]= False
        users[str(user.id)]["badge"][":crossed_swords:"] = False
        users[str(user.id)]["badge"][":coin:"]= False
        users[str(user.id)]["badge"][":milky_way:"]= False
        users[str(user.id)]["badge"][":earth_americas:"]= False
        users[str(user.id)]["badge"][":crown:"]= False
        users[str(user.id)]["badge"][":moyai:"]= False

    with open(f"{id}users.json", "w") as f:
        json.dump(users,f,indent=2)
    
    return True

async def data(ctx):
    id = ctx.message.guild.id

    with open(f"{id}users.json", "r") as f:
        users = json.load(f)
    
    return users

async def loto5_data(ctx):
    id = ctx.message.guild.id

    with open(f"{id}loto5.json", "r") as f:
        loto = json.load(f)
    
    return loto

async def loto3_data(ctx):
    id = ctx.message.guild.id

    with open(f"{id}loto3.json", "r") as f:
        loto = json.load(f)
    
    return loto


async def open_json(ctx):
    id = ctx.message.guild.id
    if os.path.exists(f"{id}users.json"):
        None
    else :
        with open(f"{id}users.json", "w+") as f:
            f.write("{}")
    if os.path.exists(f"{id}loto5.json"):
        None
    else :
        with open(f"{id}loto5.json", "w+") as f:
            f.write("{}")
    if os.path.exists(f"{id}loto3.json"):
        None
    else :
        with open(f"{id}loto3.json", "w+") as f:
            f.write("{}")
    


async def info(ctx,member,id):

    users = await data(ctx)

    user = ctx.author

    try:
        users[str(user.id)]["Investigator_Private"] -= 1
        with open(f"{id}users.json", "w") as f:
            json.dump(users,f,indent=2)

        wallet_amt = int(users[str(member.id)]["wallet"])

        cashbox = int(users[str(member.id)]["cashbox_amount"])

        all_badges = []

        all_abilities = {}

        banlock = {}

        for key,value in (users[str(member.id)]["badge"]).items():
            if value is True:
                all_badges.append(key)
            else:
                all_badges.append("-")
        
        for key,value in (users[str(member.id)]).items():
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
            win_rate = (users[str(member.id)]["win"] / users[str(member.id)]["total"]) * 100
        
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

        embed.set_author(name = member.name,icon_url= member.avatar_url)

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
{users[str(member.id)]["win"]} / {users[str(member.id)]["total"]}```""",inline=True,)

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


        await user.send(embed = embed)

        
    
    except:
        await ctx.send("Böyle biri yok.")


    

async def info_p(ctx,member,id):

    users = await data(ctx)

    user = ctx.author

    try:
        users[str(user.id)]["Investigator_Public"] -= 1
        with open(f"{id}users.json", "w") as f:
            json.dump(users,f,indent=2)

        wallet_amt = int(users[str(member.id)]["wallet"])

        cashbox = int(users[str(member.id)]["cashbox_amount"])

        all_badges = []

        all_abilities = {}

        banlock = {}

        for key,value in (users[str(member.id)]["badge"]).items():
            if value is True:
                all_badges.append(key)
            else:
                all_badges.append("-")
        
        for key,value in (users[str(member.id)]).items():
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
            win_rate = (users[str(member.id)]["win"] / users[str(member.id)]["total"]) * 100
        
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

        embed.set_author(name = member.name,icon_url= member.avatar_url)

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
{users[str(member.id)]["win"]} / {users[str(member.id)]["total"]}```""",inline=True,)

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

        await ctx.send(embed = embed)

    
    except:
        await ctx.send("Böyle biri yok.")

def all_equal(a):
    g = groupby(a)
    return next(g, True) and not next(g, False)
