import random 
import sqlite3
import numpy as np
from datetime import datetime, date, time
import json


groups = {
   "course_1": "1",
   "course_2": "2",
   "course_3": "3",
   "course_4": "4",

   "letter_1": "п",
   "letter_2": "р",
   "letter_3": "к",
   "letter_4": "иб",

   "year_1": "19",
   "year_2": "18",
   "year_3": "17",
   "year_4": "16"

}

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

def hello_check(resp):
    a = ["привет", 'прив' , 'здраствуй',
    'здраствуйте', 'hi' ,'hello' , 'hey' , 
    'приветствую' ,'здарова' , 'здарово' ,
    'ку' , 'салам' , 'саламсалам' ,'ghbdtn','приветик']
    if resp in a:
        return 'привет'

def hw(resp):
    a = ["домашняяработа","домашнеезадание","дз","homework","домашка","hm"]
    if resp in a:
        return 'real'

def registration_check(response):
    reg = ["какзарегистироваться","зарегистрироваться",
    "регистрация","какрегистрироваться","reg","registration"]
    if response in reg:
        return "какзарегистрироваться"

def time_for_end(respon):
    times = ['время', 'скольковремя', 'часы', 'которыйчас',
    'скольковремени', 'pair', 'пары', 'времядопары',
    'time', 'время', 'время', 'time', 'сколькодопары', 'когдапара', 'classes',
    'когдапары', 'когдапара', 'пара', 'урок', 'когдаурок', 'сколькодоурока',
    'когданачало', 'перемена', 'когдаперемена', 'конецурока', 'сколькодоперемены', 'break']
    if respon in times:
        response = 'время'
    return response

def groupa(grupa):
    a = ["1ат19","1ат219","1иб119","1иб219","1к119",
    "1к219","1п119","1п219","1п319","1р119","1р219","1са119",
    "1ф119","2ат118","2иб118","2к118","2к218","2п118","2п218","2п318",
    "2р118","2р218","1са118","3ат118","3иб117","3к117","3п117","3р117",
    "3са117","4п117"] 
    if grupa in a: 
        return 'real'

def subject_check(response):
    a = ["математика", "русский","русскийязык","литература","литра","физика",
    "асмтрономия","английский","английскийязык","инстронныйязык","обществознание",
    "общество","ии","введениевии","введениевискуссвенныйинтелект",
    "питон","python","введениевpython","физическаякультура","физра","информатика","введениевпрограмированиенаpython",
    "english","englishlanguage","англ","русскаялитература","физическиесвойствапк","питончик","общага","искусственныйинтелект",
    "word","powerpoint","teams","программированиенабалалайке","программированиенаpython","роднаялитература","матан","вышмат",
    "высшаяматематика","верстка","дизайн"]#нужно узнать пары у других групп и записать
    if response in a: 
        return 'real'

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
            },
            "color": color
    }




class Variables:
    where = 'курская'
    
    
    if where == 'курская':
        pair_hour = [
            ['9', '11', '13', '15', '16'],
            ['30','10', '30', '10', '50']
        ]
        # break hour 
        break_hour = [
            ['11', '12', '15', '16', '18'],
            ['00', '40', '00', '40', '20']
        ]
    else:
        pair_hour = [
            ['10', '11', '14', '15', '17'],
            ['00','40', '00', '40', '20']
        ]
        # break hour 
        break_hour = [
            ['11', '13', '15', '17', '18'],
            ['30', '10', '30', '10', '50']
        ]
    
    # time now
    hour_now = (datetime.strftime(datetime.now(), "%H"))
    minute_now = (datetime.strftime(datetime.now(), "%M"))
    
    # hour_now = '16'
    # minute_now = '00'

  

class TimeTimeTime(Variables):
    
    def __init__(self):
        
        self.hour = np.dtype(f"timedelta64[{self.hour_now}h]")
        self.minute = np.dtype(f'timedelta64[{self.minute_now}m]')
        print(f'{self.hour}, {self.minute}')
    
    
    def generater_vars(self): 
        
        try:
            self.hour_ = np.array(1, self.hour).astype('timedelta64[m]')
            self.minute_ =  np.array(1, self.minute).astype('timedelta64[m]')
            return self.hour_ + self.minute_
        except SystemError:
            return self.hour_

    
    def translate_time(self):
        
        self.pair_hour_ = [i for e, i in enumerate(self.pair_hour) if e == 0][0]
        self.pair_minute_ = [i for e, i in enumerate(self.pair_hour) if e == 1][0]
        self.break_hour_ = [i for e, i in enumerate(self.break_hour) if e == 0][0]
        self.break_minute_ = [i for e, i in enumerate(self.break_hour) if e == 1][0]
        
        return self.pair_hour_, self.pair_minute_, self.break_hour_, self.break_minute_
    
    
    def restailer(self):
        
        self.pair_hour_time = []
        for index in range(len(self.translate_time()[0])):
            self.pair_hour_time.append(np.dtype(f'timedelta64[{self.translate_time()[0][index]}h]'))
        
        self.pair_minute_time = []
        for index in range(len(self.translate_time()[1])):
            self.pair_minute_time.append(np.dtype(f'timedelta64[{self.translate_time()[1][index]}m]'))
        
        self.break_hour_time = []
        for index in range(len(self.translate_time()[2])):
            self.break_hour_time.append(np.dtype(f'timedelta64[{self.translate_time()[2][index]}h]'))
            
        self.break_minute_time = []
        for index in range(len(self.translate_time()[3])):
            self.break_minute_time.append(np.dtype(f'timedelta64[{self.translate_time()[3][index]}m]'))
    
        return self.pair_hour_time, \
        self.pair_minute_time, \
        self.break_hour_time, \
        self.break_minute_time
    
    def recycler(self):
        
        self.pair_hour_time_ = []
        for index in self.restailer()[0]:
            self.pair_hour_time_.append(np.datetime_data(index))
            
        self.pair_minute_time_ = []
        for index in self.restailer()[1]:
            self.pair_minute_time_.append(np.datetime_data(index))
        
        self.break_hour_time_ = []
        for index in self.restailer()[2]:
            self.break_hour_time_.append(np.datetime_data(index))
        
        self.break_minute_time_ = []
        for index in self.restailer()[3]:
            self.break_minute_time_.append(np.datetime_data(index))
        
        return self.pair_hour_time_, \
        self.pair_minute_time_, \
        self.break_hour_time_, \
        self.break_minute_time_
        
        
    def translate_recyler(self):
        
        self.pair_time = []
        for e, i in enumerate(self.recycler()[0]):
            try:
                self.pair_time.append(np.array(1, self.restailer()[0][e]).astype('timedelta64[h]') + np.array(1, self.restailer()[1][e]).astype('timedelta64[m]'))
            except SystemError:
                self.pair_time.append(np.array(1, self.restailer()[0][e]).astype('timedelta64[m]'))
        
        self.break_time = []
        for e, i in enumerate(self.recycler()[2]):
            try:
                self.break_time.append(np.array(1, self.restailer()[2][e]).astype('timedelta64[h]') + np.array(1, self.restailer()[3][e]).astype('timedelta64[m]'))
            except SystemError:
                self.break_time.append(np.array(1, self.restailer()[2][e]).astype('timedelta64[m]'))
                
        return self.pair_time, self.break_time
    
    def prr(self):
        
        return self.generater_vars()



class What(TimeTimeTime):
    
    def give_information(self):
        
        self.won = np.array(1, np.dtype(f'timedelta64[{10}m]')).astype('timedelta64[m]')
        self.own = np.array(1, np.dtype(f'timedelta64[{50}m]')).astype('timedelta64[m]')
        for i, e in enumerate(self.translate_recyler()[0]):
            for j in range(len(self.translate_recyler()[0])-1):
                
                if self.translate_recyler()[0][i] <= self.generater_vars() <= self.translate_recyler()[1][i]:
                    return f'До конца пары: {str(self.translate_recyler()[1][i] - self.generater_vars())}'
                
                elif (self.translate_recyler()[0][j+1] - self.translate_recyler()[1][i] == self.won and \
                self.translate_recyler()[1][i] <= self.generater_vars() <= self.translate_recyler()[0][j+1]) or \
                (self.translate_recyler()[0][j+1] - self.translate_recyler()[1][i] == self.own and \
                self.translate_recyler()[1][i] <= self.generater_vars() <= self.translate_recyler()[0][j+1]):
                    return f'До начала пары: {str(self.translate_recyler()[0][j+1] - self.generater_vars())}'
        else:
            return 'Пар нет!'


h = What()
h.give_information()