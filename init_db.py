import sqlite3

#DBの初期化のために実行するコマンド

conn = sqlite3.connect('label.db')
c = conn.cursor()

c.execute('''
        create table if not exists data(
            id text,
            time int,
            emotion text,
            valence int,
            arousal int,
            memo text)''')

#c.execute("alter table data add column bpm real")
conn.commit()
conn.close()
print("DB初期化完了！")