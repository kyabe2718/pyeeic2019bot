#! /usr/bin/python3

import time
import schedule
import atexit
import signal
import subprocess
import sys

def handler(signum, frame):
    init.bot.postMessage('#dev_bot', "signalに殺された！！ signum: "+ str(signum)
    sys.exit(0)


def main():

    res = subprocess.check_output(['curl', 'inet-ip.info'])
    print("global ip is ", res.decode('utf-8'))

    import init

    # スケジューラにタスクを登録
    #   10分毎にassignment_notify_mgrを更新する

    schedule.every(10).minutes.do(init.assignment_notify_mgr.updateAssignmentList)

    schedule.every().day.at("17:00").do(init.postTommorowAssignment)

    schedule.every().saturday.at("17:00").do(init.postNextWeekAssignment)

    atexit.register(lambda : init.bot.postMessage('#dev_bot', "正常終了！！"))   # プログラム終了時に呼ばれる関数を登録
    signal.signal(signal.SIGTERM, handler )
    signal.signal(signal.SIGINT, handler )

    init.bot.postMessage("#dev_bot" ,"生き返った！！\nglobal ip is " + res.decode('utf-8'))
    print("all initialized\n")


    while True:
        schedule.run_pending()
        time.sleep(10)


if __name__ == "__main__":
    main()
