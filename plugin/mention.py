# coding: utf-8

from slackbot.bot import respond_to  # @bot_nameで反応する
from slackbot.bot import listen_to  # チャンネル内発言に反応する
from slackbot.bot import default_reply  #
import init
import random


@respond_to('こんにちは')
def hello_func(message):
    message.reply('こんにちは')


@respond_to(r'.*明日.*課題.*')
def TommorowAssignment(message):
    message.reply(init.getTommorowAssignmentMessage())


@respond_to(r'.*来週.*課題.*')
def NextWeekAssignment(message):
    message.reply(init.getNextWeekAssignmentMessage())

@respond_to(r'更新')
def updateAssignmentList(message):
    init.assignment_notify_mgr.updateAssignmentList()

@respond_to(r'.*占って.*')
@respond_to(r'.*うらなって.*')
def divine(message):
    num = random.randint(1, 7)
    result = ""
    if num == 1:
        result = 'あなたの運勢は凶です.'
    elif num == 2:
        result = 'あなたの運勢は小吉です.'
    elif num == 3:
        result = 'あなたの運勢は吉です.'
    elif num == 4:
        result = 'あなたの運勢は中吉です.'
    elif num == 5:
        result = 'あなたの運勢は大吉です.'
    elif num == 6:
        result = 'あなたの運勢は大凶です.'
    else:
        result = '占ってるひまがあったら勉強しましょう'
    message.reply(result)
