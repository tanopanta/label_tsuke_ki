import sqlite3

#DBの初期化のために実行するコマンド

conn = sqlite3.connect('label.db')
c = conn.cursor()

c.execute('''
        create table if not exists data(
            id text,
            time int,
            action text,
            s_joy real,
            s_trust real,
            s_anger real,
            s_anticipation real,
            memo text)''')

#c.execute("alter table data add column bpm real")
conn.commit()
conn.close()
print("DB初期化完了！")