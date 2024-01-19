import asyncio
import os
from interactions import Client, Intents, listen, slash_command, SlashContext

if os.path.exists(".env"):
    from dotenv import load_dotenv

    load_dotenv()

# intents = Intents.new(all=True)
intents = Intents.DEFAULT
bot = Client(intents=intents)
# intents are what events we want to receive from discord, `DEFAULT` is usually fine

bot_token = os.environ.get("BOT_TOKEN")
guild_id = "1043068096954515487"


@listen()  # this decorator tells snek that it needs to listen for the corresponding event, and run this coroutine
async def on_ready():
    # This event is called when the bot is ready to respond to commands
    print("Ready")
    print(f"This bot is owned by {bot.owner}")


@listen()
async def on_message_create(event):
    # This event is called when a message is sent in a channel the bot can see
    print(f"message received: {event.message.content}")


@slash_command(name="my_command", description="My first command :)")
async def my_command_function(ctx: SlashContext):
    await ctx.send("Hello World")


@slash_command(name="my_long_command", description="My second command :)")
async def my_long_command_function(ctx: SlashContext):
    # need to defer it, otherwise, it fails
    await ctx.defer()

    # do stuff for a bit
    await asyncio.sleep(600)

    await ctx.send("Hello World")


bot.start(bot_token)
