import os
import discord

from dotenv import load_dotenv


class Philobot(discord.Client):
    async def on_ready(self):
        print(f'{self.user} Raring to go!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == '!rules':
            response = 'rules text coming soon'
            await message.channel.send(response)


def main():
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    client = Philobot()

    client.run(token)


if __name__ == '__main__':
    main()
