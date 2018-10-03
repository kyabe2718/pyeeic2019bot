#! /usr/bin/python3

import time
import schedule

import init
import atexit


def main():
    # スケジューラにタスクを登録
    #   10分毎にassignment_notify_mgrを更新する
    schedule.every(10).minutes.do(init.assignment_notify_mgr.updateAssignmentList)

    schedule.every().day.at("17:00").do(init.postTommorowAssignment)

    schedule.every().saturday.at("17:00").do(init.postNextWeekAssignment)

    atexit.register(init.atDeath)   # プログラム終了時に呼ばれる関数を登録
    init.bot.postMessage("#dev_bot" ,"生き返った")
    print("all initialized")

    while True:
        schedule.run_pending()
        time.sleep(10)


if __name__ == "__main__":
    main()
