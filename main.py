import os
import disnake
from dotenv import load_dotenv
from disnake.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient
from utility.utils import ConsoleColors

load_dotenv()

description = """The undertale RPG Beta bot."""

intents = disnake.Intents.none()
intents.members = False
intents.message_content = False

class UndertaleBot(commands.AutoShardedInteractionBot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.BotToken = os.getenv("TOKEN")
        self.invite_url = "https://discord.gg/FQYVpuNz4Q"
        self.vote_url = "https://top.gg/bot/815153881217892372"
        self.website = "https://undertalerpg.monster/"
        self.patreon_link = "https://www.patreon.com/undertaleRPG"
        self.currency = ":coin:"
        self.activity = disnake.Game("Undertale | /help ")
        self.help_command = None
        self.MongoUrl = os.getenv("MONGO_URL")
        self.error_webhook = os.getenv("ERROR_WEBHOOK")
        self.cluster = AsyncIOMotorClient(self.MongoUrl)
        self.players = None
        self.consumables = None
        self.armor = None
        self.weapons = None
        self.db = None
        self.boosters = None

    async def on_shard_connect(self, shard):
        print(
            f"{ConsoleColors.CYAN}---------- {ConsoleColors.GREEN}Shard {shard} is on {ConsoleColors.CYAN}-------------\n"
            f"{ConsoleColors.GREEN}Total Guilds: {len(self.guilds)}\n"
            f"{ConsoleColors.GREEN}Total Shards: {len(self.shards)}\n"
            f"{ConsoleColors.CYAN}--------------------------------------{ConsoleColors.ENDC}"
        )

    def load_all_cogs(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and not filename.startswith("_"):
                self.load_extension(f"cogs.{filename[:-3]}")
                print(f"{ConsoleColors.GREEN}🔁 cogs.{filename[:-3]} is loaded and ready.")
        return

    def db_load(self):
        self.cluster = AsyncIOMotorClient(self.MongoUrl)
        self.db = self.cluster["database"]
        self.consumables = self.db["consumables"]
        self.armor = self.db["armor"]
        self.weapons =self.db["weapons"]
        self.players = self.db["players"]
        self.guilds_db = self.db["guilds"]
        self.boosters = self.db["boosters"]
        print(f"{ConsoleColors.GREEN}✅ the database has loaded")
        return


bot = UndertaleBot(
    intents=intents,
    owner_ids=[536538183555481601, 1023550762816638996]
)

bot.db_load()
bot.load_all_cogs()
bot.run(bot.BotToken)