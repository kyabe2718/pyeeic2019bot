# coding: utf-8

from slackbot.bot import respond_to  # @bot_nameで反応する
from slackbot.bot import listen_to  # チャンネル内発言に反応する
from slackbot.bot import default_reply  #
import init
import random
import pprint
import assignment_notify
import subprocess


@respond_to('こんにちは')
def hello_func(message):
    message.reply('こんにちは！')


@respond_to(r'.*明日.*課題.*')
def TommorowAssignment(message):
    print("明日の課題を聞かれました")
    msg = init.getTommorowAssignmentMessage()
    if msg == "":
        message.reply("明日の課題は無いよ")
    else:
        message.reply(msg)


@respond_to(r'.*来週.*課題.*')
def NextWeekAssignment(message):
    print("来週の課題を聞かれました")
    msg = init.getNextWeekAssignmentMessage()
    if msg == "":
        message.reply("来週の課題は無いよ")
    else:
        message.reply(msg)


@respond_to(r'.*今後.*課題.*')
def NextWeekAssignment(message):
    print("今後の課題を聞かれました")
    msg = init.getNotDeadlineAssignmentMessage()
    if msg == "":
        message.reply("今後の課題は無いよ")
    else:
        message.reply(msg)


@respond_to(r'.*課題.*一覧.*')
def all_assignment(message):
    print("課題の一覧を聞かれました")
    msg = assignment_notify.parseAssignmentList(init.assignment_notify_mgr.assignment_list.list)
    if msg == "":
        message.reply("課題は無いよ")
    else:
        message.reply(msg)


@respond_to(r'.*更新.*いつ.*')
@respond_to(r'.*いつ.*更新.*')
def lastUpdateTime(message):
    last_update_time = init.assignment_notify_mgr.last_update_time
    message.reply('最後に更新したのは' + str(last_update_time) + 'だよ！')


@respond_to(r'.*課題.*更新.*')
@respond_to(r'.*更新.*課題.*')
def updateAssignmentList(message):
    new_assignment = init.assignment_notify_mgr.updateAssignmentList()
    msg = "更新したよ！\n"
    if len(new_assignment) == 0:
        msg += "新しく追加された課題は無いよ"
    else:
        msg += "新しく追加された課題は以下だよ\n"
        msg += assignment_notify.parseAssignmentList(new_assignment)
    message.reply(msg)


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

@respond_to(r'whoareyou')
def my_data(message):
    res1 = subprocess.check_output(['curl', 'inet-ip.info'])
    res2 = subprocess.check_output(['pwd'])
    message.reply(res1.decode('utf-8') + "\n" + res2.decode('utf-8'))
    pass

@default_reply()
def default(message):
    reply_list = [
        "うーん、なにを言ってるかわからないや！",
        "ごめんね、ボクは難しいことはわからないんだ...",
        "もうちょっとわかりやすく言ってほしいな",
        "難しいことを理解してほしかったら自然言語処理を実装して",
    ]
    message.reply(random.choice(reply_list))

