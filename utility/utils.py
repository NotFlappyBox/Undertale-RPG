import time
from disnake.ext import commands

class ConsoleColors:
    HEADER  = '\033[95m'
    BLUE    = '\033[94m'
    CYAN    = '\033[96m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[1;33m'
    LRED    = '\033[1;31m'
    WARNING = '\033[93m'
    FAIL    = '\033[91m'
    ENDC    = '\033[0m'
    BOLD    = '\033[1m'
    UNDER   = '\033[4m'

async def create_player_info(inter, mem):
    dat = await inter.bot.players.find_one({"_id": mem.id})
    if dat is None:
        new_account = {
            # unique idx
            "_id": mem.id,
            "registered_on": int(time.time()),
            "badges": [],

            # statistics
            "level": 1,
            "resets": 0,
            "health": 20,

            "multi_g": 1,
            "multi_xp": 1,
            "attack": 10,
            "defence": 5,

            "exp": 0,
            "gold": 200,
            "armor": "bandage",
            "inventory": ["monster_candy"],
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
            "the_barrier_boss": False,
            "last_corridor_boss": False,

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
            "determination crate": 1,
            "soul crate": 0,
            "void crate": 0,
            "event crate": 0,

            #fight stats
            "in_fight": False,
            "fight_monster": "",
            "fight_hp": 0,
            "fight_def": 0,
            "fight_atk": 0,
        }

        await inter.bot.players.insert_one(new_account)
    else:
        return


def occurrence(stored, value):
    try:
        stored[value] = stored[value] + 1
    except KeyError:
        stored[value] = 1
        return