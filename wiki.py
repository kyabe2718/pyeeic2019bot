#! /bin/usr/python3

import requests


class MediaWikiSession:
    def __init__(self, api_url, bot_username, bot_password):
        self.session = requests.Session()
        self.api_url = api_url
        self.bot_username = bot_username
        self.bot_password = bot_password
        login_token = self.getLoginToken()
        self.login(login_token)

    def getLoginToken(self):
        login_token_param = {
            'action': "query",
            'meta': "tokens",
            'type': "login",
            'format': "json"
        }
        ret = self.session.get(url=self.api_url, params=login_token_param)
        print(ret)
        login_token = (ret.json())['query']['tokens']['logintoken']
        return login_token

    def login(self, login_token):
        login_param = {
            'action': "login",
            'lgname': self.bot_username,
            'lgpassword': self.bot_password,
            'lgtoken': login_token,
            'format': "json"
        }
        ret = self.session.post(self.api_url, data=login_param)
        return ret.json()

    def getPageContent(self, page_name):
        get_content_param = {
            "action": "query",
            "format": "json",
            "prop": "revisions",
            "titles": page_name,
            "utf8": 1,
            "rvprop": "content"
        }
        ret = self.session.post(self.api_url, data=get_content_param)
        pages = ret.json()['query']['pages']
        for page_id in pages:
            content = pages[page_id]['revisions'][0]['*']
            return content
        return False


def getEEICWikiSession():
    import json
    WIKI_URL = "https://wiki.eeic.jp"
    API_URL = WIKI_URL + "/api.php"
    file = open('user_info.json')
    user_info = json.load(file)
    file.close()
    session = MediaWikiSession(API_URL, user_info['wiki']['bot_username'], user_info['wiki']['bot_password'])
    return session
