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
def updateAssignmentList(message):
    init.assignment_notify_mgr.updateAssignmentList()
    message.reply('更新したよ！')


@respond_to(r'.*占.*')
@respond_to(r'.*うらなって.*')
def divine(message):
    fortune_result = [
        'キミの運勢は吉だよ',
        'キミの運勢は小吉だよ',
        'キミの運勢は中吉だよ',
        'キミの運勢は大吉だよ.今日一日ハッピーなことがたくさんあるよ！',
        'キミの運勢は凶だよ',
        'キミの運勢は大凶だよ.気をつけてね',
        '占いをしてる暇があったら勉強しようね！！',
        'ちゃんと勉強してる？',
    ]
    message.reply(random.choice(fortune_result))

@default_reply()
def default(message):
    reply_list = [
        "うーん、なにを言ってるかわからないや！",
        "ごめんね、ボクは難しいことはわからないんだ...",
        "もうちょっとわかりやすく言ってほしいな"
    ]
    message.reply(random.choice(reply_list))
    pass
