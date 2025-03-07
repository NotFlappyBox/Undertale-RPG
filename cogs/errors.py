import disnake 
import requests
from disnake.ext import commands

from utility.utils import ConsoleColors

class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_slash_command_error(self, inter, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = disnake.Embed(
                title="This command is on cooldown!",
                description=f"Try again in **{error.retry_after:.2f}** seconds",
                color=0x0077ff
            )
            return await inter.send(embed=em, ephemeral=True)
        
        url = inter.bot.error_webhook

        embed = {
            "description": f"{error}",
            "title": "An error has occured",
            "color": 0x0077ff,
            "timestamp": ""
        }
        
        data = {
            "embeds": [embed]
        }
        result = requests.post(url, json=data)
        if 200 <= result.status_code < 300:
            print(f"Webhook sent {result.status_code}")
        else:
            print(f"{ConsoleColors.WARNING}Not sent with {result.status_code}, response:\n{result.json()}")



def setup(bot):
    bot.add_cog(Errors(bot))