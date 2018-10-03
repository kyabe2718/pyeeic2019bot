import os

import eeic_bot
import wiki
import assignment_notify

is_first = True
if is_first:
    WIKI_URL = "https://wiki.eeic.jp"
    API_URL = WIKI_URL + "/api.php"
    f = open("user_info.json")
    import json
    user_info = json.load(f)
    f.close()
    bot_username = user_info['BOT_USERNAME']
    bot_password = user_info['BOT_PASSWORD']
    api_token = user_info['API_TOKEN']

    #bot_username = os.environ['BOT_USERNAME']
    #bot_password = os.environ['BOT_PASSWORD']
    #api_token = os.environ['API_TOKEN']

    session = wiki.MediaWikiSession(API_URL, bot_username, bot_password)
    page_name = 'EEIC2019/課題一覧'

    # slackBotとassingment_notify_mgrを用意
    # botを別スレッドでスタート
    bot = eeic_bot.SlackBot(API_TOKEN=api_token)
    assignment_notify_mgr = assignment_notify.AssignmentListMgr(session, page_name)

    is_first = False


def getTommorowAssignmentMessage():
    tommorow_assignment = assignment_notify_mgr.getTommorowAssignmentList()
    assignment_str = assignment_notify.parseAssignmentList(tommorow_assignment)
    message = "明日の課題をお知らせします．\n"
    if assignment_str == "":
        message += "明日の課題はありません."
    else:
        message += assignment_str
    return message


#   明日の課題を投稿する
def postTommorowAssignment():
    bot.postMessage("#assignment", getTommorowAssignmentMessage())


def getNextWeekAssignmentMessage():
    assignment = assignment_notify_mgr.getNextWeekAssignmentList()
    assignment_str = assignment_notify.parseAssignmentList(assignment)
    message = "来週の課題をお知らせします．\n"
    if assignment_str == "":
        message += "来週の課題はありません."
    else:
        message += assignment_str
    return message


#   来週の課題を投稿する
def postNextWeekAssignment():
    bot.postMessage("#assignment", getNextWeekAssignmentMessage())

def atDeath():
    bot.postMessage("#dev_bot", "死んだ！！")

