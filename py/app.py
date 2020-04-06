from flask import Flask
import mysql.connector
import config

app=Flask(__name__)
app.config['SECFET_KEY']=config.key['FLASK_SECRET_KEY']

# conn =mysql.connector.connect(host='127.0.0.1',post=3306,user='root',passwd='123456',database='strong',charset='usf8mb4')
# #获取操作游标
# db=conn.cursor()


if __name__=='__main__':
    app.run(host='127.0.0.1',port=5000)