# coding: utf-8

import json
file = open('user_info.json')
user_info = json.load(file)
file.close()

# botアカウントのトークンを指定
API_TOKEN = user_info['slack']['API_TOKEN']

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "何を言っているのかわからないよ？"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugin']
