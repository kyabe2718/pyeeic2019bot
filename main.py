#! /usr/bin/python3

import time
import schedule
import os

import eeic_bot
import wiki
import assignment_notify


def main():
    WIKI_URL = "https://wiki.eeic.jp"
    API_URL = WIKI_URL + "/api.php"
    bot_username = os.environ['BOT_USERNAME']
    bot_password = os.environ['BOT_PASSWORD']
    session = wiki.MediaWikiSession(API_URL, bot_username, bot_password)
    page_name = 'EEIC2018/課題一覧'

    # slackBotとassingment_notify_mgrを用意
    # botを別スレッドでスタート
    api_token = os.environ['API_TOKEN']
    bot = eeic_bot.SlackBot(API_TOKEN=api_token)
    assignment_notify_mgr = assignment_notify.AssignmentListMgr(session, page_name)

    # スケジューラにタスクを登録
    #   10分毎にassignment_notify_mgrを更新する
    schedule.every(10).minutes.do(assignment_notify_mgr.updateAssignmentList)

    #   毎日17時に明日の課題を投稿する
    def postTommorowAssignment():
        tommorow_assignment = assignment_notify_mgr.getTommorowAssignmentList()
        assignment_str = assignment_notify.parseAssignmentList(tommorow_assignment)
        message = "明日の課題をお知らせします．\n"
        if assignment_str == "":
            message += "明日の課題はありません."
        else:
            message += assignment_str
        bot.postMessage("#dev_bot", message)

    schedule.every().day.at("17:00").do(postTommorowAssignment)

    #   毎週土曜日17時に来週の課題を投稿する
    def postNextWeekAssignment():
        assignment = assignment_notify_mgr.getNextWeekAssignmentList()
        assignment_str = assignment_notify.parseAssignmentList(assignment)
        message = "来週の課題をお知らせします．\n"
        if assignment_str == "":
            message += "来週の課題はありません."
        else:
            message += assignment_str
        bot.postMessage("#dev_bot", message)

    schedule.every().saturday.at("17:00").do(postNextWeekAssignment)

    print("all initialized")

    while True:
        schedule.run_pending()
        time.sleep(10)


if __name__ == "__main__":
    main()
