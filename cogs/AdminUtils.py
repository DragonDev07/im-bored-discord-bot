import discord
from discord.ext import commands

class AdminUtils(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Log that the Cog has been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("The 'AdminUtils' cog has been loaded")

    # Propagate the error to the global error handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await self.bot.on_command_error(ctx, error)

    # Command to kick a member
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"Kicked User {member} for reason {reason}")
        print(f"The 'kick' command has been run on {member} by {ctx.message.author} for reason {reason}")
    
    # Command to ban a member
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"User {member} has been yeeted (banned) for reason {reason}")
        print(f"The 'ban' command has been run on {member} by {ctx.message.author} for reason {reason}")

    # Command to clear x amount of messages in a channel
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Cleared the last {amount} messages")
        print(f"The 'clear' command was run by {ctx.message.author} for amount {amount}")

    # Command to get the info of a given user
    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def userinfo(self, ctx, user: discord.User = None):
        if user is None:
            await ctx.send("Please provide a user!")
            return

        embed = discord.Embed(title ="Userinfo", description = f"The info of {user.name}", color = discord.Colour.blue())
        embed.add_field(name = user, value = f"-User\'s name: {user.name}\n -User\'s ID {user.id}\n -User\'s discrim: {user.discriminator}\n -User\'s Avatar Hash: {user.avatar}")
        await ctx.send(embed = embed)
        print(f"The 'userinfo' command was just run by {ctx.message.author} to get info on {user}")
    
async def setup(client):
    await client.add_cog(AdminUtils(client))