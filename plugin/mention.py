# coding: utf-8

from slackbot.bot import respond_to  # @bot_nameで反応する
from slackbot.bot import listen_to  # チャンネル内発言に反応する
from slackbot.bot import default_reply  #
import init
import random


@respond_to('こんにちは')
def hello_func(message):
    message.reply('こんにちは！')


@respond_to(r'.*明日.*課題.*')
def TommorowAssignment(message):
    message.reply(init.getTommorowAssignmentMessage())


@respond_to(r'.*来週.*課題.*')
def NextWeekAssignment(message):
    message.reply(init.getNextWeekAssignmentMessage())


@respond_to(r'.*更新.*いつ.*')
@respond_to(r'.*いつ.*更新.*')
def lastUpdateTime(message):
    last_update_time = init.assignment_notify_mgr.last_update_time
    message.reply('最後に更新したのは' + str(last_update_time) + 'だよ！')


@respond_to(r'.*課題.*更新.*')
@respond_to(r'.*更新.*課題.*')
def updateAssignmentList(message):
    init.assignment_notify_mgr.updateAssignmentList()
    message.reply('更新したよ！')


@respond_to(r'.*占.*')
@respond_to(r'.*うらなって.*')
def divine(message):
    fortune_result = [
        'キミの成績は:huka:だよ．ちゃんと勉強してる？',
        'キミの成績は:ka:だよ',
        'キミの成績は:ryo:だよ',
        'キミの成績は:yu:だよ．:pro:',
        'キミの成績は:yuujo:だよ．:gachi-pro::clap::clap:',
    ]
    message.reply(random.choice(fortune_result))

@default_reply()
def default(message):
    reply_list = [
        "うーん、なにを言ってるかわからないや！",
        "ごめんね、ボクは難しいことはわからないんだ...",
        "もうちょっとわかりやすく言ってほしいな",
        "難しいことを理解してほしかったら自然言語処理を実装して",
    ]
    message.reply(random.choice(reply_list))
