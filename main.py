#! /usr/bin/python3

import time
import schedule

import eeic_bot
import wiki
import assignment_notify


def main():
    import json
    file = open('user_info.json')
    user_info = json.load(file)
    file.close()
    WIKI_URL = "https://wiki.eeic.jp"
    API_URL = WIKI_URL + "/api.php"
    session = wiki.MediaWikiSession(API_URL, user_info['wiki']['bot_username'], user_info['wiki']['bot_password'])
    page_name = 'EEIC2018/課題一覧'

    # slackBotとassingment_notify_mgrを用意
    # botを別スレッドでスタート
    bot = eeic_bot.SlackBot(API_TOKEN=user_info['slack']['API_TOKEN'])
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