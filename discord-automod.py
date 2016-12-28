import discord

jb_busters = discord.Client()
banned_keywords = ["cydia", "substrate"]

@jb_busters.event
async def on_message(message):
    for keyword in banned_keywords:
        if keyword.lower() in message.contents.lower():
            jb_busters.send_message(message.channel, "Pls don't jailbreak iOS 10 yet")
            
def ban_keyword(word: str):
    pass
        
if __name__ == "__main__":
    try:
        import os
        DISCORD_SNOWFLAKE_ENVIRONMENT_KEY = "JBBUSTERS_DISCORD_SNOWFLAKE"
        jb_busters.run(os.environ[DISCORD_SNOWFLAKE_ENVIRONMENT_KEY])
    except KeyError:
        print(f"Please set {DISCORD_SNOWFLAKE_ENVIRONMENT_KEY} in the environment to the key given to you by Discord")