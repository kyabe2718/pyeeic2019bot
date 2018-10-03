# coding: utf-8

import os

# botアカウントのトークンを指定

import json

f = open("user_info.json")
user_info = json.load(f)
f.close()

API_TOKEN = user_info['API_TOKEN']
#API_TOKEN = os.environ'API_TOKEN']

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "何を言っているのかわからないよ？"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugin']
