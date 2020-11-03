import os
import json
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
            '{asctime} - [{levelname}] {message} ({lineno})', style='{')
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
            response = self.get_rules_str('data/rules_global.json')
            member = message.author
            await member.send(response)

    async def on_message_delete(self, msg):
        self.log.info(f'User {msg.author} deleted message [{msg.id}]: "{msg.content}"')
        print(msg.embeds)
        if len(msg.embeds) > 0:
            self.log.info(f'[{msg.id}] contained embeds: {msg.embeds}')
        if len(msg.attachments) > 0:
            self.log.info(f'[{msg.id}] contained attachments: {msg.attachments}')

    async def on_disconnect(self):
        self.log.info('disconnected')

    def get_rules_str(self, rulesfile):
        data = self.load_json_data(rulesfile)
        lines = data.get('rules')
        response = '\n'.join(lines)
        return response

    def load_json_data(self, filepath):
        try:
            with open(filepath, 'r') as jsonfile:
                data = json.load(jsonfile)
                return data
        except FileNotFoundError as err:
            self.log.error(f'JSON file not found: {err}')


def main():
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    client = Philobot()

    client.run(token)


if __name__ == '__main__':
    main()
