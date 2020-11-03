import os
import logging
import logging.handlers

import discord

from dotenv import load_dotenv

LOGPATH = 'logs/philobot.log'


class Philobot(discord.Client):
    try:
        log = logging.getLogger('philobot')
        log.setLevel(logging.INFO)
        fmtr = logging.Formatter(
            '{asctime} - [{levelname}] {name}: {message} ({lineno})', style='{')
        trfh = logging.handlers.TimedRotatingFileHandler(LOGPATH, 'W0', 1)
        shd = logging.StreamHandler()
        trfh.setFormatter(fmtr)
        log.addHandler(trfh)
        log.addHandler(shd)
    except FileNotFoundError as err:
        print(f'No file error: {err}. Create /logs directory')

    def __init__(self):
        super().__init__()

    async def on_ready(self):
        msg = f'{self.user} Raring to go!'
        self.log.info(msg)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == '!rules':
            response = 'rules text coming soon'
            await message.channel.send(response)

    async def on_disconnect(self):
        self.log.info('disconnected')


def main():
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    client = Philobot()

    client.run(token)


if __name__ == '__main__':
    main()
