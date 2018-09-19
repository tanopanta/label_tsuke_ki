"""
jsonで受けとる

json
https://qiita.com/kidatti/items/21cc5c5154dbbb1aa27f

flask
https://qiita.com/ynakayama/items/2cc0b1d3cf1a2da612e4
"""


from flask import Flask, render_template, request, redirect, url_for, Response
import json
from datetime import datetime


# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

# ここからウェブアプリケーション用のルーティングを記述
# index にアクセスしたときの処理
@app.route('/')
def index():
    message = "今なにしてる？"
    # index.html をレンダリングする
    return render_template('boot.html',
                           message=message)

# /post にアクセスしたときの処理
@app.route('/post', methods=['POST'])
def post():
    receive_dict = request.json #辞書型
    print(receive_dict["id"], datetime.fromtimestamp(receive_dict["time"]), receive_dict["state"])
    return Response(json.dumps(receive_dict))

if __name__ == '__main__':
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0') # どこからでもアクセス可能に
