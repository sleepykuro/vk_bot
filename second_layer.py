import random 
import sqlite3
import numpy as np
from datetime import datetime, date, time
import json

def take_int_id(namber, id_user):
    id_id = id_user[namber]
    id_id = id_id[0]
    id_id = int(id_id)
    return id_id

def take_thing(response):
    if response == "камень": return "🗿"
    if response == "бумага": return "📜"
    if response == "ножницы": return "✂" 

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

def help_check(resp):
    a = ["help", "рудз", 
    "помощь", "gjvjom",
     "func", "функции"]
    if resp in a:
        return 'help'

def hello_check(resp):
    a = ["привет", 'здраствуй',
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
    times = ['время', 'скольковремя', 'которыйчас',
    'скольковремени', 'pair', 'пары', 'времядопары',
    'time', 'время', 'время', 'time', 'сколькодопары', 'когдапара', 'classes',
    'когдапары', 'когдапара', 'пара', 'урок', 'когдаурок', 'сколькодоурока',
    'когданачало', 'перемена', 'когдаперемена', 'конецурока', 'сколькодоперемены']
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
    a = ["математика", "русскийязык","литература", "физика",
    "асмтрономия", "английскийязык","инстронныйязык", "обществознание", "искусственныйинтелект","введениевискусственныйинтелект", 
    "python", "введениевpython", "физическаякультура", "информатика", "введениевпрограмированиенаpython",
    "english","englishlanguage", "русскаялитература", "физическиесвойствапк", "фсп", 
    "word","powerpoint","teams", "роднаялитература",
    "высшаяматематика","верстка","дизайн", "htmlcss"]#нужно узнать пары у других групп и записать
    if response in a: 
        return 'real'

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


#_________________________________________________________________________________________________________________________

#                                            Клавиатуры
#_________________________________________________________________________________________________________________________

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
            },
            "color": color
    }

keyboard_yes_no = {
      "one_time": True,
      "buttons": [
      [get_button(label="Да", color="positive"),
       get_button(label="Нет", color="negative")]
      ]
    }
keyboard_yes_no = json.dumps(keyboard_yes_no, ensure_ascii=False).encode('utf-8')
keyboard_yes_no = str(keyboard_yes_no.decode('utf-8'))

recruitment_team_keyboard = {
      "one_time": True,
      "buttons": [
      [get_button(label="В колледже", color="primary")],
      [get_button(label="В группе", color="primary"),]
      ]
    }

recruitment_team_keyboard = json.dumps(recruitment_team_keyboard, ensure_ascii=False).encode('utf-8')
recruitment_team_keyboard = str(recruitment_team_keyboard.decode('utf-8'))

keyboard_profilse = {
        "one_time": True,
        "buttons": [
        [get_button(label="Программисты", color="primary")],
        [get_button(label="Разработчики", color="primary"),
         get_button(label="Коммерция", color="primary")],
        [get_button(label="Безопасники", color="primary")]
        ]
      }
keyboard_profilse = json.dumps(keyboard_profilse, ensure_ascii=False).encode('utf-8')
keyboard_profilse = str(keyboard_profilse.decode('utf-8'))

keyboard_help_student = {
          "one_time": True,
          "buttons": [
          [get_button(label="Help", color="primary"),
           get_button(label="Массовое сообщение", color="primary")],
          [get_button(label="Игра", color="primary"),
           get_button(label="Время", color="primary")],
          [get_button(label="Домашнее задание", color="primary"),
           get_button(label="Уведомление", color="primary")],
          [get_button(label="Набор в команду", color="primary")]
          ]
        }
keyboard_help_student = json.dumps(keyboard_help_student, ensure_ascii=False).encode('utf-8')
keyboard_help_student = str(keyboard_help_student.decode('utf-8'))
keyboard_help_kurator = {
          "one_time": True,
          "buttons": [
          [get_button(label="Help", color="primary"),
           get_button(label="Массовое сообщение", color="primary")],
          [get_button(label="Игра", color="primary"),
           get_button(label="Время", color="primary")],
          [get_button(label="Домашнее задание", color="primary"),
           get_button(label="Уведомление", color="primary")],
          [get_button(label="Посещаемость", color="primary"),
           get_button(label="Набор в команду", color="primary")]
          ]
        }
keyboard_help_kurator = json.dumps(keyboard_help_kurator, ensure_ascii=False).encode('utf-8')
keyboard_help_kurator = str(keyboard_help_kurator.decode('utf-8'))

keyboard_help_teacher = {
          "one_time": True,
          "buttons": [
          [get_button(label="Help", color="primary"),
           get_button(label="Массовое сообщение", color="primary")],
          [get_button(label="Игра", color="primary"),
           get_button(label="Время", color="primary")],
          [get_button(label="Домашнее задание", color="primary"),
           get_button(label="Уведомление", color="primary")],
          [get_button(label="Посещаемость", color="primary"),
           get_button(label="Набор в команду", color="primary")]
          ]
        }
keyboard_help_teacher = json.dumps(keyboard_help_teacher, ensure_ascii=False).encode('utf-8')
keyboard_help_teacher = str(keyboard_help_teacher.decode('utf-8'))

keyboard_help_user = {
          "one_time": True,
          "buttons": [
          [get_button(label="Help", color="primary"),
           get_button(label="Регистрация", color="primary")],
          [get_button(label="Поступление", color="primary"),
           get_button(label="Специальности", color="primary")],
          [get_button(label="Мастер классы", color="primary"),
           get_button(label="ДОД", color="primary")]
          ]
        }
keyboard_help_user = json.dumps(keyboard_help_user, ensure_ascii=False).encode('utf-8')
keyboard_help_user = str(keyboard_help_user.decode('utf-8'))

keyboard_help_administration = {
          "one_time": True,
          "buttons": [
          [get_button(label="Help", color="primary"),
           get_button(label="Массовое сообщение", color="primary")],
          [get_button(label="Игра", color="primary"),
           get_button(label="Время", color="primary")],
          [get_button(label="Домашнее задание", color="primary"),
           get_button(label="Уведомление", color="primary")],
          [get_button(label="Смена ранга", color="primary"),
           get_button(label="Набор в команду", color="primary")]
          ]
        }
keyboard_help_administration = json.dumps(keyboard_help_administration, ensure_ascii=False).encode('utf-8')
keyboard_help_administration = str(keyboard_help_administration.decode('utf-8'))

keyboard_help_starosta = {
          "one_time": True,
          "buttons": [
          [get_button(label="Help", color="primary"),
           get_button(label="Массовое сообщение", color="primary")],
          [get_button(label="Игра", color="primary"),
           get_button(label="Время", color="primary")],
          [get_button(label="Домашнее задание", color="primary"),
           get_button(label="Уведомление", color="primary")],
          [get_button(label="Посещаемость", color="primary"),
           get_button(label="Набор в команду", color="primary")]
          ]
        }
keyboard_help_starosta = json.dumps(keyboard_help_starosta, ensure_ascii=False).encode('utf-8')
keyboard_help_starosta = str(keyboard_help_starosta.decode('utf-8'))

keyboard_course = {
        "one_time": True,
        "buttons": [
        [get_button(label="Первый курс", color="primary"),
        get_button(label="Второй курс", color="primary")],
        [get_button(label="Третий курс", color="primary"),
        get_button(label="Четвертый курс", color="primary")],
        [get_button(label="<<< Специальности", color="secondary")]
        ]
      }
keyboard_course = json.dumps(keyboard_course, ensure_ascii=False).encode('utf-8')
keyboard_course = str(keyboard_course.decode('utf-8'))

keyboard_game = {
        "one_time": True,
        "buttons": [
        [get_button(label="Камень", color="primary"),
        get_button(label="Ножницы", color="primary"),
        get_button(label="Бумага", color="primary")]
        ]
      }
keyboard_game = json.dumps(keyboard_game, ensure_ascii=False).encode('utf-8')
keyboard_game = str(keyboard_game.decode('utf-8'))

keyboard_replay = {
        "one_time": True,
        "buttons": [
        [get_button(label="Играть еще раз", color="primary"),
        get_button(label="Help", color="primary")]
        ]
      }
keyboard_replay = json.dumps(keyboard_replay, ensure_ascii=False).encode('utf-8')
keyboard_replay = str(keyboard_replay.decode('utf-8'))

bulk_keyboard = {
      "one_time": True,
      "buttons": [
      [get_button(label="Колледжу", color="primary")],
      [get_button(label="Группе", color="primary"),]
      ]
    }
bulk_keyboard = json.dumps(bulk_keyboard, ensure_ascii=False).encode('utf-8')
bulk_keyboard = str(bulk_keyboard.decode('utf-8'))

keyboard_lessons = {
      "one_time": True,
      "buttons": [
      [get_button(label="1 пара", color="primary"),
      get_button(label="2 пара", color="primary")],
      [get_button(label="3 пара", color="primary"),
      get_button(label="4 пара", color="primary")],
      [get_button(label="5 пара", color="primary")]
      ]
    }

keyboard_lessons = json.dumps(keyboard_lessons, ensure_ascii=False).encode('utf-8')
keyboard_lessons = str(keyboard_lessons.decode('utf-8'))

keyboard_help = {
    "one_time": True,
    "buttons": [
    [get_button(label="help", color="primary")]
    ]
}

keyboard_help = json.dumps(keyboard_help, ensure_ascii=False).encode('utf-8')
keyboard_help = str(keyboard_help.decode('utf-8'))


#________________________________________________________________________________________________________________________

#                                           Списки
#_________________________________________________________________________________________________________________________

game = {

"камень✂": "win",
"ножницы📜": "win",
"бумага🗿": "win",
"ножницы🗿": "lose",
"бумага✂": "lose",
"камень📜": "lose"

}

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
