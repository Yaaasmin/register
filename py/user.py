from app import app
from flask import request,session
from database import checkPhone,createRegister,update

@app.route('/register',methods=['POST'])
def register():
    data=request.get_json()
    name=data['name']
    sex=data['sex']
    campus=data['campus']
    grade=data['grade']
    academy=data['academy']
    dormitory=data['dormitory']
    phone=data['phone']
    first_choice=data['first_choice']
    second_choice=data['second_choice']
    faceTime=data['faceTime']
    selfintroduction=data['selfintroduction']
    
    lastresult=checkPhone(phone)
    if(lastresult[0]==True and lastresult[1]==False):
        return{
            'errcode':400,
            'errmsg':'此手机号已经被填写'
        },400
    elif(lastresult[0]==False):
        return{
            'errcode':400,
            'errmsg':'请输入正确的手机号'
        },400

    allrow=createRegister(name,sex,campus,grade,academy,dormitory,phone,first_choice,second_choice,faceTime,selfintroduction)
    if(allrow>0):
        return{
            'errcode':0,
            'errmsg':'报名成功'
        },200
    return{
           'errcode':400,
           'errmsg':'出现错误，请重试'
        },400

@app.route('/modify',methods=['POST'])
def modify():
    data=request.get_json()
    name=data['name']
    sex=data['sex']
    campus=data['campus']
    grade=data['grade']
    academy=data['academy']
    dormitory=data['dormitory']
    phone=data['phone']
    first_choice=data['first_choice']
    second_choice=data['second_choice']
    faceTime=data['faceTime']
    selfintroduction=data['selfintroduction']

    lastresult=checkPhone(phone)
    if(lastresult[0]==True and lastresult[1]==False):
        return{
            'errcode':400,
            'errmsg':'此手机号已经被填写'
        },400
    elif(lastresult[0]==False):
        return{
            'errcode':400,
            'errmsg':'请输入正确的手机号'
        },400
    all=update(name,sex,campus,grade,academy,dormitory,phone,first_choice,second_choice,faceTime,selfintroduction)
    if(all>0):
        return{
            'errcode':0,
            'errmsg':'报名成功'
        },200
    return{
           'errcode':401,
           'errmsg':'出现错误，请重试'
        },401
    


    

