import time

import disnake
from disnake.ext import commands

class ConsoleColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDER = '\033[4m'


def in_battle():
    async def predicate(inter):
        if str(inter.author.id) in inter.bot.fights:
            embed = disnake.Embed(
                title="You have a fight dialogue open",
                description=f"> [Click here]({inter.bot.fights[str(inter.author.id)].msg.jump_url})",
                color=disnake.Color.random()
            )
            await inter.send(embed=embed)
            return False
        return True

    return commands.check(predicate)


def in_shop():
    async def predicate(inter):
        if str(inter.author.id) in inter.bot.shops:
            embed = disnake.Embed(
                title="You have a shop dialogue open",
                description=f"> [Click here]({inter.bot.shops[str(inter.author.id)].msg.jump_url})",
                color=disnake.Color.random()
            )
            await inter.send(embed=embed)
            return False
        return True

    return commands.check(predicate)


async def create_player_info(ctx, mem):
    dat = await ctx.bot.players.find_one({"_id": mem.id})
    if dat is None:
        new_account = {
            # unique idx
            "_id": mem.id,
            "registered_on": int(time.time()),

            # statistics
            "level": 1,
            "resets": 0,
            "health": 20,

            "multi_g": 1,
            "multi_xp": 1,
            "tokens": 0,
            "damage": 0,

            "exp": 0,
            "gold": 200,
            "armor": "bandage",
            "inventory": [],
            "weapon": "stick",
            "location": "ruins",

            # blocks
            "daily_block": 0,
            "supporter_block": 0,
            "booster_block": 0,
            "rest_block": 0,

            # boss booleans
            "ruins_boss": False,
            "snowdin_boss": False,
            "waterfall_boss": False,
            "hotland_boss": False,
            "core_boss": False,
            "the barrier_boss": False,
            "last corridor_boss": False,

            # counters
            "ruins_kills": 0,
            "snowdin_kills": 0,
            "waterfall_kills": 0,
            "hotland_kills": 0,
            "core_kills": 0,

            "kills": 0,
            "deaths": 0,
            "spares": 0,

            # crates data
            "standard crate": 1,
            "determination crate": 0,
            "soul crate": 0,
            "void crate": 0,
            "event crate": 0
        }

        await ctx.bot.players.insert_one(new_account)
    else:
        return


def occurrence(stored, value):
    try:
        stored[value] = stored[value] + 1
    except KeyError:
        stored[value] = 1
        return