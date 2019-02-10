# EEIC2019 Bot

[EEIC](http://www.ee.t.u-tokyo.ac.jp/)2019のためのBotです。

以下、主にEEIC2019のためのREADME。

## 使い方

python3とpipをインストールしたあとこのリポジトリをcloneして、以下のコマンドを実行します。

 $ pip3 install -r requirements.txt

 $ python3 main.py

ただし，slackがbotのアクセスをglobal ipのホワイトリストで制限しているため，おそらく使えません．

現在，Herokuのipしか登録してません．

slackにアクセスするためのapi tokenやwikiアクセスのためのユーザー名，パスワードは
API_TOKEN, BOT_USERNAME, BOT_PASSWORDというkeyで環境変数にする，もしくはこのディレクトリにuser_info.jsonという名前でjson形式で書いたものを用意してください

## サーバー

現在，Heroku上で動いています．

新規に何か開発したらプルリクをください．

## 課題お知らせちゃん (EEICたん)

膨大な量のEEICの課題をSlackにお知らせするBOT。

### やること

* 毎日17:00に次の日が締切の課題をお知らせします。
* 毎週土曜の17:00にその週の課題一覧をお知らせします。

### 課題登録

課題一覧はWikiの指定されたページを編集すると自動で登録されます。

Wikiページは誰でも気軽に編集してください。というか課題が出てるのに登録されてないのを見つけたらためらわずに編集してください。みんなのためです。
