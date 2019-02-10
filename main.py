#! /usr/bin/python3

import time
import schedule
import atexit
import signal
import subprocess
import sys
import datetime

dev_channel_name = "#8-dev_bot"

def main():
    res = subprocess.check_output(['curl', 'inet-ip.info'])
    print("global ip is ", res.decode('utf-8'))

    import init

    # スケジューラにタスクを登録
    #   10分毎にassignment_notify_mgrを更新する

    schedule.every(10).minutes.do(init.assignment_notify_mgr.updateAssignmentList)

    schedule.every().day.at("17:00").do(init.postTommorowAssignment)

    schedule.every().saturday.at("12:00").do(init.postNextWeekAssignment)

    def atExit():
        print("atExit is called")
        init.bot.postMessage(dev_channel_name, "正常終了！！\n" + str(datetime.datetime.now()))
        print("send message and exit")
        sys.exit()

    atexit.register(atExit)  # プログラム終了時に呼ばれる関数を登録

    def handler(signum, frame):
        print("handler is called")
        init.bot.postMessage(dev_channel_name, "signal handler signum: " + str(signum) + "\nnow time: " + str(datetime.datetime.now()))
        print("send message and exit")
        sys.exit()

    signal.signal(signal.SIGTERM, handler)
    signal.signal(signal.SIGINT, handler)

    init.bot.postMessage(dev_channel_name,
            "start.\nglobal ip is " + res.decode('utf-8') + "\nnow time: " + str(datetime.datetime.now()))
    print("all initialized\n")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
