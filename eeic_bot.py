#! /usr/bin/python3
# coding: utf-8

from slackclient import SlackClient
from slackbot.bot import Bot
import threading


class SlackBot:
    def __init__(self, API_TOKEN):
        self.client = SlackClient(API_TOKEN)
        self.channel_list = self.getChannelList()
        self.bot = Bot()
        self.auto_replybot_thread = threading.Thread(target=self.bot.run, daemon=False)
        self.auto_replybot_thread.start()

    def getChannelList(self):
        channels = self.client.api_call("channels.list")
        if channels['ok']:
            return channels['channels']
        else:
            return None

    def postMessage(self, channel_id, message: str):
        ret = self.client.api_call(
            "chat.postMessage",
            channel=channel_id,
            text=message,
            as_user=True
        )
        return ret
