# coding: utf-8

from slackbot.bot import respond_to  # @bot_nameで反応する
from slackbot.bot import listen_to  # チャンネル内発言に反応する
from slackbot.bot import default_reply  #


@respond_to('こんにちは')
def hello_func(message):
    message.reply('こんにちは')


