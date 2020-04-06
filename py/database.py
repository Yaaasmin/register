from config import db  
import mysql.connector


conn=mysql.connector.connect(host=db['host'],user=db['root'],passwd=db['passwd'],database=db['database'],charset='utf8mb4')
#获取操作游标
cur=conn.cursor()

def checkPhone(phone):
    cur.execute('select * from users where `phone`=%s',(phone,))
    result=cur.fetchone()
    single=(result==None)
    ret = result.match(r"^1[35678]\d{9}$", phone)
    if(ret and single):
        return ret,single
    elif(ret and single==False):
        return ret, single==False
    elif(ret==False and single==False):
        return ret==False,single==False
    else:
        return ret==False,single==True

def createRegister(name,sex,campus,grade,academy,dormitory,phone,first_choice,second_choice,faceTime,selfintroduction):
    cur.execute=('insert into users(`name`,`sex`,`campus`,`grade`,`academy`,`dormitory`,`phone`,`first_choice`,`second_choice`,`faceTime`,`selfintroduction`)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(name,sex,campus,grade,academy,dormitory,phone,first_choice,second_choice,faceTime,selfintroduction))
    conn.commit()
    return cur.rowcount


#更新数据
def update(name,sex,campus,grade,academy,dormitory,phone,first_choice,second_choice,faceTime,selfintroduction):
    cur.execute=('update users set(`name`,`sex`,`campus`,`grade`,`academy`,`dormitory`,`phone`,`first_choice`,`second_choice`,`faceTime`,`selfintroduction`)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(name,sex,campus,grade,academy,dormitory,phone,first_choice,second_choice,faceTime,selfintroduction))
    conn.commit()
    return cur.rowcount