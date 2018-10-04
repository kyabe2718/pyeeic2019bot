#! /bin/usr/python3

import re
from datetime import timezone, timedelta, datetime, date

import wiki

# タイムゾーンの生成
JST = timezone(timedelta(hours=+9), 'JST')


def getToday(time_zone: timezone):
    now = datetime.now(tz=time_zone)
    return date(year=now.year, month=now.month, day=now.day)


class AssignmentList:
    def __init__(self, assginment_page_content: str):
        self.list = self.getAllAssignmentList(assginment_page_content)

    def getAllAssignmentList(self, assignment_page_content: str):
        """
        ret = {
            '教科名1' : [
                {'assignment_title': '課題名', 'deadline_day': 'xxxx-xx-xx', 'deadline_detail': '締め切りの詳細'},
                {'assignment_title': '課題名2', 'deadline_day': 'yyyy-yy-yy', 'deadline_detail': '締め切りの詳細2'}
            ],
            '教科名2' : [
                {'assignment_title': '課題名', 'deadline_day': 'xxxx-xx-xx', 'deadline_detail': '締め切りの詳細'},
            ]
        }
        """
        subject_pattern = re.compile(r'^\s*==\s*([^=]*?)\s*==\s*$')
        assignment_pattern = re.compile(r'^\s*===\s*([^=]*?)\s*===\s*$')
        deadline_day_pattern = re.compile(r'^\s*\*\s*期日:\s*(\d{4}-\d{1,2}-\d{1,2})\s*$')
        deadline_detail_pattern = re.compile(r'^\s*\*\s*期限:\s*(.*)$')
        data = {}
        lines = assignment_page_content.splitlines()
        subject = ''
        assignment = {}
        for line in lines:
            """
            一行ずつ見ていく
            最初に教科名が来るはずなので教科名を保存しておき（subject），
            課題名(assignment_title), 締め切り(deadline_day, deadline_detail)をkeyにするdictを
            data[subject]に追加
            戻値は教科名をkeyとしたdict.
            各valueはassignment_title, deadline_day, deadline_detailをkeyにもつdict
            deadline_dayはyear-month-dayの形にのみマッチする
            """
            subject_match = subject_pattern.match(line)
            assignment_match = assignment_pattern.match(line)
            deadline_day_match = deadline_day_pattern.match(line)
            deadline_detail_match = deadline_detail_pattern.match(line)
            is_something_written = (line != '')
            if not is_something_written:
                continue
            if subject == '' and not subject_match:
                # まだ教科名が来ていないなら，何もせず次の行へ
                continue
            if subject_match:
                if 'assignment_title' in assignment.keys() and 'assignment_title' in assignment.keys() and 'assignment_title' in assignment.keys():
                    # assignmentの条件が揃った状態で次の科目に来たら,課題を登録する
                    data[subject].append(assignment)
                    assignment = {}
                subject = subject_match.group(1)
                if subject not in data.keys():
                    data[subject] = []
            elif assignment_match:
                if 'assignment_title' in assignment.keys() and 'assignment_title' in assignment.keys() and 'assignment_title' in assignment.keys():
                    # assignmentの条件が揃った状態で次の課題に来たら,課題を登録する
                    data[subject].append(assignment)
                    assignment = {}
                assignment['assignment_title'] = assignment_match.group(1)
            elif deadline_day_match:
                dt = datetime.strptime(deadline_day_match.group(1), '%Y-%m-%d')
                assignment['deadline_day'] = date(dt.year, dt.month, dt.day)
            elif deadline_detail_match:
                assignment['deadline_detail'] = deadline_detail_match.group(1)
            elif is_something_written:
                if 'something_written' not in assignment.keys():
                    assignment['something_written'] = line
                else:
                    assignment['something_written'] += line
        # assignmentの条件が揃った状態で一番最後に来たら,課題を登録する
        if 'assignment_title' in assignment.keys() and 'assignment_title' in assignment.keys() and 'assignment_title' in assignment.keys():
            data[subject].append(assignment)
        return data

    def getAssignmentListSinceUntil(self, since: date, until: date):
        ret = {}
        for subject in self.list:
            for assignment in self.list[subject]:
                if since <= assignment['deadline_day'] <= until:
                    if subject not in ret:
                        ret[subject] = [assignment]
                    else:
                        ret[subject].append(assignment)
        return ret


class AssignmentListMgr:
    def __init__(self, wiki_session: wiki.MediaWikiSession, page_name: str):
        self.wiki_session = wiki_session
        self.page_name = page_name
        content = self.wiki_session.getPageContent(self.page_name)
        self.assignment_list = AssignmentList(content)
        self.last_update_time = datetime.now(tz=JST)

    def updateAssignmentList(self):
        content = self.wiki_session.getPageContent(self.page_name)
        self.assignment_list = AssignmentList(content)
        self.last_update_time = datetime.now(tz=JST)

    def getNotDeadlineAssignmentList(self):
        # 今日から一年後まで
        return self.assignment_list.getAssignmentListSinceUntil(
            since=getToday(JST), until=getToday(JST) + timedelta(weeks=52))

    def getTommorowAssignmentList(self):
        # 明日提出の課題一覧
        return self.assignment_list.getAssignmentListSinceUntil(
            since=getToday(JST) + timedelta(days=1), until=getToday(JST) + timedelta(days=1))

    def getNextWeekAssignmentList(self):
        # 来週提出の課題一覧
        return self.assignment_list.getAssignmentListSinceUntil(
            since=getToday(JST) + timedelta(days=1), until=getToday(JST) + timedelta(weeks=1))


def parseAssignmentList(assignment_list):
    s = ""
    for subject in assignment_list:
        s += "*" + subject + "*\n"
        for index, assignment in enumerate(assignment_list[subject]):
            s += str(index + 1) + ". " + assignment['assignment_title'] + "\n"
            s += "   期日 " + str(assignment['deadline_day']) + "\n"
            s += "   期限 " + assignment['deadline_detail'] + "\n"
            if 'something_written' in assignment.keys():
                s += "   補足 " + assignment['something_written'] + "\n"
    return s


"""
if __name__ == "__main__":
    f = open("test.txt")
    content = f.read()
    list = AssignmentList(content)
    import pprint

    pprint.pprint(list.list)
    """
