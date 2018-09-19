"""
jsonで受けとる

json
https://qiita.com/kidatti/items/21cc5c5154dbbb1aa27f

flask
https://qiita.com/ynakayama/items/2cc0b1d3cf1a2da612e4
"""


from flask import Flask, render_template, request, redirect, url_for, Response, g
import json
from datetime import datetime
import sqlite3

DATABASE = "label.db"


# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        #コネクションを確保
        db = g._database = sqlite3.connect(DATABASE)
    return db
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# ここからウェブアプリケーション用のルーティングを記述
# index にアクセスしたときの処理
@app.route('/')
def index():
    # index.html をレンダリングする
    return render_template('index.html')

@app.route('/boot')
def boot():
    myid = request.args.get("id")
    return render_template('boot.html', myid=myid)

# /post にアクセスしたときの処理
@app.route('/post', methods=['POST'])
def post():
    js_list = request.json 
    #receive_dict = request.form

    db = get_db()
    c = db.cursor()
    for js in js_list:
        args = (js["id"], js["time"], js["action"],  js["s_joy"], js["s_trust"], js["s_anger"], js["s_anticipation"], js["memo"])
        c.execute("""insert into data values
            (?,?,?,?,?,?,?,?)""", args)
    db.commit()

    
    return Response(json.dumps({"result":"OK"}))

if __name__ == '__main__':
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0') # どこからでもアクセス可能に
