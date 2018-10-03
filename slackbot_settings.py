# coding: utf-8

import os

# botアカウントのトークンを指定
file_path=os.path.dirname(os.path.abspath(__file__)) + "/user_info.json"
if os.path.exists(file_path):
    f = open(file_path)
    import json
    user_info = json.load(f)
    f.close()
    API_TOKEN = user_info['API_TOKEN']
else:
    API_TOKEN = os.environ['API_TOKEN']

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "何を言っているのかわからないよ？"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugin']
