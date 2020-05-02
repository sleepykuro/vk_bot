import random 
import json
import sqlite3
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import time
import random
import sys
import json
import re
import sqlite3


def hi_answer_random(hi):
    if hi == 'hi':
        r = random.randint(1,11)
        if r == 1: 
            answer = 'Привет, что нужно ?'
        elif r == 2:
            answer = 'Привет, я личный бот itHub колледжа😉 \n Надеюсь мы поладим ) обращайся если будет нужна помощь'
        elif r == 3:
            answer = 'Здравствуй, что нужно ?'
        elif r == 4:
            answer = 'Привет, если тебе нужен список команд используй команду "help"'
        elif r == 5:
            answer = 'Привет, если тебе нужен список команд используй команду "help"'
        elif r == 6:
            answer = 'Приветствую'
        elif r == 7:
            answer = 'Greetings traveller😉'
        elif r == 11:
            answer = 'Greetings traveller😉'
        elif r == 8:
            answer = 'Привет, я личный бот itHub колледжа😉 \n Надеюсь мы поладим ) обращайся если будет нужна помощь '                   
        elif r == 9:
            answer = 'Привет, я личный бот itHub колледжа😉 \n Надеюсь мы поладим ) обращайся если будет нужна помощь '
        elif r == 10:
            answer = 'Привет, я личный бот itHub колледжа😉 \n Надеюсь мы поладим ) обращайся если будет нужна помощь '
        else:
            answer = 'Привет'
        return answer


def bas_for_mass_masseg(iddd):
    
    iddd = str(iddd)
    bas_for_mass_masseg_open = open('bas_for_mass_masseg.txt', encoding='utf_8')
    if iddd + '\n' in bas_for_mass_masseg_open:
        pass
    else:
        bas_for_mass_masseg = open('bas_for_mass_masseg.txt', 'a' , encoding='utf_8')
        bas_for_mass_masseg.write(iddd + '\n')
        bas_for_mass_masseg.close()
    
   

# def timeforend(time):

#     import time
#     from datetime import datetime

    
#     time_now_h = (str(datetime.strftime(datetime.now(), "%H,%M")))
#     time_now_m = (str(datetime.strftime(datetime.now(), "%M")))
#     dop_fraza = 'До конца пары'

#     para1_kurskaya_h = '9'
#     para1_kurskaya_m = '30'

#     para2_kurskaya_h = '11'
#     para2_kurskaya_m = '15'

#     para3_kurskaya_h = '13'
#     para3_kurskaya_m = '40'

#     para4_kurskaya_h = '15'
#     para4_kurskaya_m = '05'


#     para1_kurskaya_end_h = '11'
#     para1_kurskaya_end_m = '05'

#     para2_kurskaya_end_h = '12'
#     para2_kurskaya_end_m = '50'

#     para3_kurskaya_end_h = '15'
#     para3_kurskaya_end_m = '15'

#     para4_kurskaya_end_h = '17'
#     para4_kurskaya_end_m = '00'

#     # para1_kurskaya_h = '20'
#     # para1_kurskaya_end_h = '22' 
#     # para1_kurskaya_m = '00'
#     # para1_kurskaya_end_m = '00'


#     if time_now_h >= para1_kurskaya_h and time_now_h <= para1_kurskaya_end_h:
#         para1_kurskaya_end_h = int(para1_kurskaya_end_h)
#         para1_kurskaya_end_m = int(para1_kurskaya_end_m)
#         time_now_m = int(time_now_m)
#         time_now_h = int(time_now_h)
#         time_for_end_h = para1_kurskaya_end_h - time_now_h
#         time_for_end_m = para1_kurskaya_end_m - time_now_m
#         time_for_end_h = str(time_for_end_h)
#         time_for_end_m = str(time_for_end_m)
#         if time_for_end_h == '0':
#             time_for_end_h = ' минут '
#             time_now = dop_fraza + time_for_end_h + ':' + time_for_end_m
        
        

#     elif time_now_h >= para2_kurskaya_h and time_now_h <= para2_kurskaya_end_h:
#         para2_kurskaya_end_h = int(para2_kurskaya_end_h)
#         para2_kurskaya_end_m = int(para2_kurskaya_end_m)
#         time_now_m = int(time_now_m)
#         time_now_h = int(time_now_h)
#         time_for_end_h = para2_kurskaya_end_h - time_now_h
#         time_for_end_m = para2_kurskaya_end_m - time_now_m
#         time_for_end_h = str(time_for_end_h)
#         time_for_end_m = str(time_for_end_m)
#         if time_for_end_h == '0':
#             time_for_end_h = ' минут '
#             time_now = dop_fraza + time_for_end_h + ':' + time_for_end_m
        
        

#     elif time_now_h >= para3_kurskaya_h and time_now_h <= para3_kurskaya_end_h:
#         para3_kurskaya_end_h = int(para3_kurskaya_end_h)
#         para3_kurskaya_end_m = int(para3_kurskaya_end_m)
#         time_now_m = int(time_now_m)
#         time_now_h = int(time_now_h)
#         time_for_end_h = para3_kurskaya_end_h - time_now_h
#         time_for_end_m = para3_kurskaya_end_m - time_now_m
#         time_for_end_h = str(time_for_end_h)
#         time_for_end_m = str(time_for_end_m)
#         if time_for_end_h == '0':
#             time_for_end_h = ' минут '
#             time_now = dop_fraza + time_for_end_h + ':' + time_for_end_m
#         else:
#             time_now = dop_fraza + ': ' + time_for_end_h + ':' + time_for_end_m
        
        

#     elif time_now_h >= para4_kurskaya_h and time_now_h <= para4_kurskaya_end_h:
#         para4_kurskaya_end_h = int(para4_kurskaya_end_h)
#         para4_kurskaya_end_m = int(para4_kurskaya_end_m)
#         time_now_m = int(time_now_m)
#         time_now_h = int(time_now_h)
#         time_for_end_h = para4_kurskaya_end_h - time_now_h
#         time_for_end_m = para4_kurskaya_end_m - time_now_m
#         time_for_end_h = str(time_for_end_h)
#         time_for_end_m = str(time_for_end_m)
#         if time_for_end_h == '0':
#             time_for_end_h = ' минут '
#             time_now = dop_fraza + time_for_end_h + ':' + time_for_end_m
        
        

#     else:
#         time_now = 'Пары закончились )'
           

#     return time_now



def hello(resp):
    a = ["привет", 'прив' , 'здраствуй',
    'здраствуйте', 'hi' ,'hello' , 'хай' , 
    'приветствую' ,'здарова' , 'здорово' , 'здорово',
    'ку' , 'салам' , 'саламаллейкум' ,'ghbdtn']
    if resp in a:
        return 'привет'



        


# def db(user_id, group, answerr):
    
#         grups = ['1п1.19', '1р1.19','1п2.19','1п3.19', '1р2.19', '1ат2.19' , '1ат1.19' , '1к2.19' , '1к1.19' ]
#         if grup_put in grups:
#             return grup_put
#         return 'bad request'
#     info = []
#     info.append(user_id)


def check_db(user_id=0):
    conn = sqlite3.connect('botdatabase.db')
    cursor = conn.cursor()
    data = (" SELECT user_id FROM Groups")
    id_user = cursor.execute(data)
    id_user = id_user.fetchall()
    user_id = int(user_id)

    for i in range(len(id_user)):
        id_id = id_user[i]
        id_id = id_id[0]
        id_id = int(id_id)
        if id_id == user_id:
            return user_id



    conn.commit()
    cursor.close()
    conn.close()

def database(user_id=0, group='', answerr='', rang=''):
    
    data = [user_id, group, answerr, rang]
    
    conn = sqlite3.connect('botdatabase.db')
    cursor = conn.cursor()
    
    cursor.execute(" INSERT INTO Groups VALUES (?, ?, ?, ?) ", data)

    conn.commit()
    cursor.close()
    conn.close()




def zvonok(cheto):
    user_idd = cheto
    idd = -1
    conn = sqlite3.connect('botdatabase.db')
    cursor = conn.cursor()
    data = (" SELECT user_answer FROM Groups")
    user__answer = cursor.execute(data)
    user__answer = user__answer.fetchall()

    data = (" SELECT user_id FROM Groups")
    id_user = cursor.execute(data)
    id_user = id_user.fetchall()

    for i in range(len(id_user)):
        id_id = id_user[i]
        id_id = id_id[0]
        id_id = int(id_id)
        idd += 1
        if user_idd == id_id:
            id_id = user__answer[idd]
            id_id = id_id[0]
            return id_id


def rang_check(user_id=0):
    conn = sqlite3.connect('botdatabase.db')
    cursor = conn.cursor()
    data = (" SELECT user_id FROM Groups")
    id_user = cursor.execute(data)
    id_user = id_user.fetchall()
    user_id = int(user_id)

    for i in range(len(id_user)):
        id_id = id_user[i]
        id_id = id_id[0]
        id_id = int(id_id)
        if id_id == user_id:
            return user_id

token = "3d8a09922a0c25bd4a2235165d4eef42fe1f9d52ab09de8760edf915327cbc33bc79b2ab81c8aa139dfea"


 
def time_for_end(respon):
   
    times = ['время', 'скольковремя', 'часы', 'которыйчас',
    'скольковремени', 'pair', 'пары', 'времядопары',
    'time', 'время', 'время', 'time', 'сколькодопары', 'когдапара', 'classes',
    'когдапары', 'когдапара', 'пара', 'урок', 'когдаурок', 'сколькодоурока',
    'когданачало', 'перемена', 'когдаперемена', 'конецурока', 'сколькодоперемены', 'break']
    if respon in times:
        response = 'время'
    return response



