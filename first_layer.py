from second_layer import *
from new_db import *
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import time
import random
import sqlite3
import re
import json


tokenn = open(r"C:\Users\alfas\Desktop\token.txt", "r")
tokenn = tokenn.read()
vk_session = vk_api.VkApi(token=tokenn)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
            },
            "color": color
    }


keyboard = {
    "one_time": True,
    "buttons": [
    [
    get_button(label="Програмисты", color="secondary"),
    get_button(label="Разроботчики", color="secondary"),
    get_button(label="Комерция", color="secondary"),
    get_button(label="Безопасники", color="secondary")
    ]
    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

def keyboard_(event, user_id, response):
  if response == "клавиатура":
     vk_session.method("messages.send", {"user_id": user_id, "message": "Попочка*", "random_id": 0, "keyboard": keyboard})

def database_connection():
  class User():

    def __init__(self, user_id, user_group, user_rang):

      self.user_id = user_id
      self.user_group = user_group
      self.user_rang = user_rang 

def bot_on():
  return "on"

def take_event_user_id(event):
  if event.type == VkEventType.MESSAGE_NEW:
            user_id = event.user_id
            return user_id

def take_user_response(event):
  if event.type == VkEventType.MESSAGE_NEW:
            response = event.text.lower()
            regular = regular = re.compile("[^a-zA-Zа-яА-я,\d]")
            response = regular.sub('' , response)
            return response

def take_user_response_not_general_reg(event):
  if event.type == VkEventType.MESSAGE_NEW:
            response = event.text
            return response
                                  
def user_message(event,user_id, response):
  if event.type == VkEventType.MESSAGE_NEW:
    print('Сообщение от ' + str(user_id) + ' пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
    print('Текст сообщения: ' + str(response))

def hello(event,user_id, response):
  if hello_check(response) == 'привет':
    hi_answer = hi_answer_random('hi')
    vk_session.method('messages.send', {'user_id': user_id, 'message':hi_answer, 'random_id':0}) 

def regestration_info(event,user_id, response):
  if registration_check(response) == "какзарегистрироваться":
    vk_session.method('messages.send', {'user_id': user_id, 'message':'Что бы зарегестрироваться: \n 1.Напишите номер вашей группы \n 2.Напишите ваш статус в колледже (доступен только "ученик")', 'random_id':0}) 

def regestration_one(event, user_id, response):
  if user_id != check_db(user_id):
    enter = groupa(response)
    if enter == 'real':
      step = 1
      database(user_id, response, step, rang = '0', bulk = '')
      vk_session.method('messages.send', {'user_id': user_id, 'message':'Введите пожалуйста ваш статус в колледже', 'random_id':0})

def regestration_two(event, user_id, response): 
    if response == "ученик" or response =="студент":
      try:
        if rang_check(user_id) == 0:
          if step_check(user_id) == 1:
            response = "0.010"
            update_rang(user_id, response)
            vk_session.method('messages.send', {'user_id': user_id, 'message':'Отлично! теперь вы можете полностью использовать меня', 'random_id':0})
            nullify_step(user_id, step=0)
          elif step_check(user_id) == 0: 
            vk_session.method('messages.send', {'user_id': user_id, 'message':'сначала введите вашу группу', 'random_id':0})
        else:
          if rang_check(user_id) < 1000:
            vk_session.method('messages.send', {'user_id': user_id, 'message':'Поменять статус, можно только после одобрения Куратора', 'random_id':0})
      except IndexError:
        vk_session.method('messages.send', {'user_id': user_id, 'message':'сначала введите вашу группу', 'random_id':0})

def help_user(event,user_id, response):
  try:
    if response == "help" or response == "помощь" :
      if rang_check(user_id) == 0.010:
        keyboard = {
          "one_time": True,
          "buttons": [
          [get_button(label="Help", color="primary"),
           get_button(label="Массовое сообщение", color="primary")],
          [get_button(label="Игра", color="primary"),
           get_button(label="Время", color="primary")],
          [get_button(label="Домашнее задание", color="primary"),
           get_button(label="Уведомление", color="primary")]
          ]
        }
        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
        keyboard = str(keyboard.decode('utf-8'))
        vk_session.method('messages.send', {'user_id': user_id, 'message':
        """
        \n1. Help: Список комманд доступный вашему статусу (Студент)
        \n2. Массовое сообщение: Рассылка сообщения группе/колледжу
        \n3. Игра: Простое развлечение
        \n4. Время: Время до начала и конца пары
        \n5. Домашнее задание: Просмотр заданного домашнего задания
        \n6. Уведомления: Настройка получения удомлений
        """, 'random_id':0, "keyboard": keyboard})

      if rang_check(user_id) == 0.050:
        keyboard = {
          "one_time": True,
          "buttons": [
          [get_button(label="Help", color="primary"),
           get_button(label="Массовое сообщение", color="primary")],
          [get_button(label="Игра", color="primary"),
           get_button(label="Время", color="primary")],
          [get_button(label="Домашнее задание", color="primary"),
           get_button(label="Уведомление", color="primary")],
          [get_button(label="Посещаемость", color="primary")]
          ]
        }
        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
        keyboard = str(keyboard.decode('utf-8'))
        vk_session.method('messages.send', {'user_id': user_id, 'message':
        """
        \n1. Help: Список комманд доступный вашему статусу (Староста)
        \n2. Массовое сообщение: Рассылка сообщения группе/колледжу
        \n3. Игра: Простое развлечение
        \n4. Время: Время до начала и конца пары
        \n5. Домашнее задание: Просмотр заданного домашнего задания
        \n6. Уведомления: Настройка получения удомлений
        \n7. Посещаемость: Просмотр просещаемость своей группы группы
        """, 'random_id':0, "keyboard": keyboard})

      if rang_check(user_id) == 0.070:
        keyboard = {
          "one_time": True,
          "buttons": [
          [get_button(label="Help", color="primary"),
           get_button(label="Массовое сообщение", color="primary")],
          [get_button(label="Игра", color="primary"),
           get_button(label="Время", color="primary")],
          [get_button(label="Домашнее задание", color="primary"),
           get_button(label="Уведомление", color="primary")],
          [get_button(label="Посещаемость", color="primary")]
          ]
        }
        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
        keyboard = str(keyboard.decode('utf-8'))
        vk_session.method('messages.send', {'user_id': user_id, 'message':
        """
        \n1. Help: Список комманд доступный вашему статусу (Куратор)
        \n2. Массовое сообщение: Рассылка сообщения группе/колледжу
        \n3. Игра: Простое развлечение
        \n4. Время: Время до начала и конца пары
        \n5. Домашнее задание: Просмотр заданного домашнего задания
        \n6. Уведомления: Настройка получения удомлений
        \n7. Посещаемость: Просмотр просещаемость курируемой группы
        """, 'random_id':0, "keyboard": keyboard})

      if rang_check(user_id) == 1:
        keyboard = {
          "one_time": True,
          "buttons": [
          [get_button(label="Help", color="primary"),
           get_button(label="Массовое сообщение", color="primary")],
          [get_button(label="Игра", color="primary"),
           get_button(label="Время", color="primary")],
          [get_button(label="Домашнее задание", color="primary"),
           get_button(label="Уведомление", color="primary")],
          [get_button(label="Посещаемость", color="primary")]
          ]
        }
        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
        keyboard = str(keyboard.decode('utf-8'))
        vk_session.method('messages.send', {'user_id': user_id, 'message':
        """
        \n1. Help: Список комманд доступный вашему статусу (Преподаватель)
        \n2. Массовое сообщение: Рассылка сообщения группе/колледжу
        \n3. Игра: Простое развлечение
        \n4. Время: Время до начала и конца пары
        \n5. Домашнее задание: Отправка домашнего задания
        \n6. Уведомления: Настройка получения удомлений
        \n7. Посещаемость: Проверка посещаемость
        """, 'random_id':0, "keyboard": keyboard})

      if rang_check(user_id) == 0.100:
        keyboard = {
          "one_time": True,
          "buttons": [
          [get_button(label="Help", color="primary"),
           get_button(label="Массовое сообщение", color="primary")],
          [get_button(label="Игра", color="primary"),
           get_button(label="Время", color="primary")],
          [get_button(label="Домашнее задание", color="primary"),
           get_button(label="Уведомление", color="primary")],
          [get_button(label="Смена ранга", color="primary")]
          ]
        }
        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
        keyboard = str(keyboard.decode('utf-8'))
        vk_session.method('messages.send', {'user_id': user_id, 'message':
        """
        \n1. Help: Список комманд доступный вашему статусу (Администратор)
        \n2. Массовое сообщение: Рассылка сообщения группе/колледжу
        \n3. Игра: Простое развлечение
        \n4. Время: Время до начала и конца пары
        \n5. Домашнее задание: Просмотр заданного домашнего задания
        \n6. Уведомления: Настройка получения удомлений
        \n7. Смена ранга: Изменение ранга пользователя
        """, 'random_id':0, "keyboard": keyboard})     
  except: pass

      

def bulk_message(event, user_id, response):
  if response == "сообщение": 

    keyboard = {
      "one_time": True,
      "buttons": [
      [get_button(label="колледжу", color="primary")],
      [get_button(label="группе", color="primary"),]
      ]
    }

    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))

    vk_session.method('messages.send', {'peer_id': user_id, 'message':"кому вы хотите отправить сообщение ?", 'random_id':0, "keyboard": keyboard})

def bulk_message_take(event, user_id, response):
  if response == "колледжу":
    update_step(user_id, 10)
    vk_session.method('messages.send', {'peer_id': user_id, 'message':"какое сообщение отправить?", 'random_id':0})
  if response == "группе":
    update_step(user_id, 11)
    vk_session.method('messages.send', {'peer_id': user_id, 'message':"какое сообщение отправить?", 'random_id':0})

def bulk_group_message(event,user_id, response, bulk):
  try:
    if response != "колледжу" and response != "группе" and response != "сообщение":
      if step_check(user_id) == 10:
        if rang_check(user_id) >= 0.100:
          vk_session.method('messages.send', {'peer_id': user_id, 'message':"сообщние отправленно!", 'random_id':0})
          nullify_step(user_id, 0)
          conn = sqlite3.connect('botdatabase.db')
          cursor = conn.cursor()
          data = (" SELECT user_id FROM Groups")
          id_user = cursor.execute(data)
          id_user = id_user.fetchall()

          for i in range(len(id_user)):
              id_id = id_user[i]
              id_id = id_id[0]
              id_id = int(id_id)
              if id_id != user_id:
                vk_session.method('messages.send', {'peer_id': id_id, 'message':bulk, 'random_id':0})

        elif rang_check(user_id) < 0.100:
          update_bulk(user_id, bulk)
          vk_session.method('messages.send', {'user_id': user_id, 'message':"Ваше сообение направленно на одобрение Администрации", 'random_id':0})
          group = group_check(user_id)
          conn = sqlite3.connect('botdatabase.db')
          cursor = conn.cursor()
          data = (" SELECT user_id FROM Groups")
          id_user = cursor.execute(data)
          id_user = id_user.fetchall()

          while True:
              id_id = id_user[i]
              id_id = id_id[0]
              id_id = int(id_id)
              if group == group_check(id_id):
                if rang_check(id_id) >= 0.100:
                  update_step(id_id, step=12)
                  update_bulk(id_id, str(user_id))
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':f"Сообщение на одобрение: {bulk}", 'random_id':0})
                  keyboard = {
                      "one_time": True,
                      "buttons": [
                      [
                      get_button(label="да", color="positive"),
                      get_button(label="нет", color="negative")
                      ]
                      ]
                   }

                  keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                  keyboard = str(keyboard.decode('utf-8'))

                  vk_session.method('messages.send', {'peer_id': id_id, 'message':"\n\n Одобрить сообщение ? ", 'random_id':0, "keyboard": keyboard})
                  break
    if response != "колледжу" and response != "группе" and response != "сообщение":
      if step_check(user_id) == 11:
        if rang_check(user_id) >= 0.050:
          conn = sqlite3.connect('botdatabase.db')
          cursor = conn.cursor()
          data = (" SELECT user_id FROM Groups")
          id_user = cursor.execute(data)
          id_user = id_user.fetchall()

          for i in range(len(id_user)):
              id_id = id_user[i]
              id_id = id_id[0]
              id_id = int(id_id)
              if group_check(user_id) == group_check(id_id):
                if id_id != user_id:
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':bulk, 'random_id':0})

        elif rang_check(user_id) < 0.050:
          update_bulk(user_id, bulk)
          vk_session.method('messages.send', {'user_id': user_id, 'message':"Ваше сообение направленно на одобрение Куратору", 'random_id':0})
          group = group_check(user_id)
          conn = sqlite3.connect('botdatabase.db')
          cursor = conn.cursor()
          data = (" SELECT user_id FROM Groups")
          id_user = cursor.execute(data)
          id_user = id_user.fetchall()

          for i in range(len(id_user)):
              id_id = id_user[i]
              id_id = id_id[0]
              id_id = int(id_id)
              if group == group_check(id_id):
                if rang_check(id_id) >= 0.050:
                  update_step(id_id, step=12)
                  update_bulk(id_id, str(user_id))
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':f"Сообщение на одобрение: {bulk}", 'random_id':0})
                  keyboard = {
                      "one_time": True,
                      "buttons": [
                      [
                      get_button(label="да", color="positive"),
                      get_button(label="нет", color="negative")
                      ]
                      ]
                   }

                  keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                  keyboard = str(keyboard.decode('utf-8'))

                  vk_session.method('messages.send', {'peer_id': id_id, 'message':"\n\n Одобрить сообщение ? ", 'random_id':0, "keyboard": keyboard})
  except: pass
  
def bulk_message_check(event,user_id, response): 
  try:
    if response == "да" or response == "одобряю": 
          if step_check(user_id) == 12:
            message_id = bulk_check_id(user_id)
            vk_session.method('messages.send', {'peer_id': message_id, 'message':"Отправка вашего сообщения одобренна!", 'random_id':0})
            bulk = bulk_check(message_id)
            conn = sqlite3.connect('botdatabase.db')
            cursor = conn.cursor()
            data = (" SELECT user_id FROM Groups")
            id_user = cursor.execute(data)
            id_user = id_user.fetchall()

            for i in range(len(id_user)):
                id_id = id_user[i]
                id_id = id_id[0]
                id_id = int(id_id)
                if rang_check(id_id) < 0.100:
                    vk_session.method('messages.send', {'peer_id': id_id, 'message':bulk, 'random_id':0})
            nullify_step(user_id, step = 0)
            update_bulk(user_id, "")
            update_bulk(message_id, "")
    elif response == "нет" or "неодобряю": 
            if step_check(user_id) == 12:
              message_id = int(bulk_check(user_id))
              vk_session.method('messages.send', {'peer_id': message_id, 'message':"Отправка вашего сообщения отклонена", 'random_id':0})
              nullify_step(user_id, step = 0)
              update_bulk(user_id, "")
              update_bulk(message_id, "")
  except: pass

def group_message_check(event,user_id, response): 
    try:
      if response == "да" or response == "одобряю": 
        if step_check(user_id) == 13:
          message_id = bulk_check_id(user_id)
          vk_session.method('messages.send', {'peer_id': message_id, 'message':"Отправка вашего сообщения одобренна!", 'random_id':0})
          bulk = bulk_check(message_id)
          group = group_check(user_id)
          conn = sqlite3.connect('botdatabase.db')
          cursor = conn.cursor()
          data = (" SELECT user_id FROM Groups")
          id_user = cursor.execute(data)
          id_user = id_user.fetchall()

          for i in range(len(id_user)):
              id_id = id_user[i]
              id_id = id_id[0]
              id_id = int(id_id)
              if group == group_check(id_id):
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':bulk, 'random_id':0})
          nullify_step(user_id, step = 0)
          update_bulk(user_id, "")
          update_bulk(message_id, "")
      elif response == "нет" or "неодобряю": 
        if step_check(user_id) == 13:
          message_id = int(bulk_check(user_id))
          vk_session.method('messages.send', {'peer_id': message_id, 'message':"Отправка вашего сообщения отклонена", 'random_id':0})
          nullify_step(user_id, step = 0)
          update_bulk(user_id, "")
          update_bulk(message_id, "")
    except: pass

def game_1(event,user_id, response):
  if response == 'игра':
    update_step(user_id, step = 20)
    vk_session.method('messages.send', {'peer_id': user_id, 'message':"Я загадал число от 1 до 5, попробуй угадать!", 'random_id':0})

def game_2(event,user_id, response):
  if response != "игра":
    try:
      if step_check(user_id) == 20:
        a = random.randint(1,5)
        if response == str(a): 
          nullify_step(user_id, step=0)
          vk_session.method('messages.send', {'peer_id': user_id, 'message':f"молодец! мое число действительно было {a}", 'random_id':0})
        else: 
          nullify_step(user_id, step=0)
          vk_session.method('messages.send', {'peer_id': user_id, 'message':"к сожалению ты не угадал (", 'random_id':0})
      
    except: pass

def timetable(event, user_id, response):
  if response == "время":
      h = What()
      vk_session.method('messages.send', {'peer_id': user_id, 'message':h.give_information(), 'random_id':0})

def attendance_1(event, user_id, response):
  if response == "посещаемость":
    if rang_check(user_id) >= 1:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="Програмисты", color="primary")],
            [
              get_button(label="Разроботчики", color="primary"),
              get_button(label="Комерция", color="primary")
            ],
            [get_button(label="Безопасники", color="primary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=30)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Пожалуйста выберите Курс", 'random_id':0, "keyboard": keyboard})
    if rang_check(user_id) >= 0.050 and rang_check(user_id) < 1:
      group = group_check(user_id)
      conn = sqlite3.connect('botdatabase.db')
      cursor = conn.cursor()
      data = (" SELECT user_id FROM Groups")
      id_user = cursor.execute(data)
      id_user = id_user.fetchall()
      all_users_attendance = ""
      for i in range(len(id_user)):
          id_id = id_user[i]
          id_id = id_id[0]
          id_id = int(id_id)
          if group == group_check(id_id):   
            attendance = attendance_check(id_id)
            if attendance == "":
              attendance = "прогул"
            vk = vk_session.get_api() 
            user_get=vk.users.get(user_ids = (id_id))
            user_get=user_get[0]
            first_name=user_get['first_name']
            last_name=user_get['last_name']
            full_name=first_name+" "+last_name
            users_attendance = full_name + ": " + attendance
            all_users_attendance = all_users_attendance +"\n" +users_attendance  
      vk_session.method('messages.send', {'peer_id': user_id, 'message':all_users_attendance, 'random_id':0})

def attendance_1_keyboard_2(event, user_id, response):
  if response == "програмисты":
    if step_check(user_id) == 30:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="Первый курс", color="primary"),
            get_button(label="Второй курс", color="primary")
            ],
            [
            get_button(label="Третий курс", color="primary"),
            get_button(label="Четвертый курс", color="primary")
            ],
            [
              get_button(label="<<< Специальности", color="secondary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))

      update_step(user_id, step=31)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Укажите группу!", 'random_id':0, "keyboard": keyboard})
  if response == "разроботчики":
    if step_check(user_id) == 30:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="Первый курс", color="primary"),
            get_button(label="Второй курс", color="primary")
            ],
            [
            get_button(label="Третий курс", color="primary"),
            get_button(label="Четвертый курс", color="primary")
            ],
            [
              get_button(label="<<< Специальности", color="secondary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))

      update_step(user_id, step=32)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Укажите группу!", 'random_id':0, "keyboard": keyboard})
  if response == "комерция":
    if step_check(user_id) == 30:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="Первый курс", color="primary"),
            get_button(label="Второй курс", color="primary")
            ],
            [
            get_button(label="Третий курс", color="primary"),
            get_button(label="Четвертый курс", color="primary")
            ],
            [
              get_button(label="<<< Специальности", color="secondary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))

      update_step(user_id, step=33)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Укажите группу!", 'random_id':0, "keyboard": keyboard})
  if response == "безопасники":
    if step_check(user_id) == 30:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="Первый курс", color="primary"),
            get_button(label="Второй курс", color="primary")
            ],
            [
            get_button(label="Третий курс", color="primary"),
            get_button(label="Четвертый курс", color="primary")
            ],
            [
              get_button(label="<<< Специальности", color="secondary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))

      update_step(user_id, step=34)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Укажите курс!", 'random_id':0, "keyboard": keyboard})

def attendance_2(event, user_id, response):
  if response == "ltспециальности":
    keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="Програмисты", color="primary")],
            [
              get_button(label="Разроботчики", color="primary"),
              get_button(label="Комерция", color="primary")
            ],
            [get_button(label="Безопасники", color="primary")
            ]
            ]
        }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    update_step(user_id, step=30)
    vk_session.method('messages.send', {'peer_id': user_id, 'message':"Пожалуйста выберите Курс", 'random_id':0, "keyboard": keyboard})

  if response == "первыйкурс":
    if step_check(user_id) == 31:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="1п1.19", color="primary"),
            get_button(label="1п2.19", color="primary"),
            get_button(label="1п3.19", color="primary"),
            ],
            [
              get_button(label="<<< курсы", color="secondary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=35)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какая группа?", 'random_id':0, "keyboard": keyboard})
  if response == "первыйкурс":
    if step_check(user_id) == 32:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="1р1.19", color="primary"),
            get_button(label="1р2.19", color="primary"),
            get_button(label="1р3.19", color="primary"),
            ],
            [
              get_button(label="<<< курсы", color="secondary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=35)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какая группа?", 'random_id':0, "keyboard": keyboard})
  if response == "первыйкурс":
    if step_check(user_id) == 33:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="1к1.19", color="primary"),
            get_button(label="1к2.19", color="primary"),
            get_button(label="1к3.19", color="primary"),
            ],
            [
              get_button(label="<<< курсы", color="secondary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=35)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какая группа?", 'random_id':0, "keyboard": keyboard})
  if response == "первыйкурс":
    if step_check(user_id) == 34:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="1иб1.19", color="primary"),
            get_button(label="1иб2.19", color="primary"),
            get_button(label="1иб3.19", color="primary"),
            ],
            [
              get_button(label="<<< курсы", color="secondary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=35)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какая группа?", 'random_id':0, "keyboard": keyboard})
  if response == "второйкурс":
    if step_check(user_id) == 31:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="2п1.18", color="primary"),
            get_button(label="2п2.18", color="primary"),
            get_button(label="2п3.18", color="primary"),
            ],
            [
              get_button(label="<<< курсы", color="secondary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=35)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какая группа?", 'random_id':0, "keyboard": keyboard})
  if response == "второйкурс":
    if step_check(user_id) == 32:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="2р1.18", color="primary"),
            get_button(label="2р2.18", color="primary"),
            get_button(label="2р3.18", color="primary"),
            ],
            [
              get_button(label="<<< курсы", color="secondary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=35)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какая группа?", 'random_id':0, "keyboard": keyboard})
  if response == "второйкурс":
    if step_check(user_id) == 33:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="2к1.18", color="primary"),
            get_button(label="2к2.18", color="primary"),
            get_button(label="2к3.18", color="primary"),
            ],
            [
              get_button(label="<<< курсы", color="secondary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=35)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какая группа?", 'random_id':0, "keyboard": keyboard})
  if response == "второйкурс":
    if step_check(user_id) == 34:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="2иб1.18", color="primary"),
            get_button(label="2иб2.18", color="primary"),
            get_button(label="2иб3.18", color="primary"),
            ],
            [
              get_button(label="<<< курсы", color="secondary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=35)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какая группа?", 'random_id':0, "keyboard": keyboard})
  if response == "третийкурс":
    if step_check(user_id) == 31:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="3п1.17", color="primary"),
            get_button(label="3п2.17", color="primary"),
            get_button(label="3п3.17", color="primary"),
            ],
            [
              get_button(label="<<< курсы", color="secondary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=35)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какая группа?", 'random_id':0, "keyboard": keyboard})
  if response == "третийкурс":
    if step_check(user_id) == 32:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="3р1.17", color="primary"),
            get_button(label="3р2.17", color="primary"),
            get_button(label="3р3.17", color="primary"),
            ],
            [
              get_button(label="<<< курсы", color="secondary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=35)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какая группа?", 'random_id':0, "keyboard": keyboard})
  if response == "третийкурс":
    if step_check(user_id) == 33:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="3к1.17", color="primary"),
            get_button(label="3к2.17", color="primary"),
            get_button(label="3к3.17", color="primary"),
            ],
            [
              get_button(label="<<< курсы", color="secondary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=35)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какая группа?", 'random_id':0, "keyboard": keyboard})
  if response == "третийкурс":
    if step_check(user_id) == 34:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="3иб1.17", color="primary"),
            get_button(label="3иб2.17", color="primary"),
            get_button(label="3иб3.17", color="primary"),
            ],
            [
              get_button(label="<<< курсы", color="secondary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=35)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какая группа?", 'random_id':0, "keyboard": keyboard})
  if response == "четвертыйкурс":
    if step_check(user_id) == 31:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="4п1.17", color="primary")
            ],
            [
              get_button(label="<<< курсы", color="secondary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=35)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какая группа?", 'random_id':0, "keyboard": keyboard})
  if response == "четвертыйкурс":
    if step_check(user_id) == 32:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="4п1.17", color="primary")
            ],
            [
              get_button(label="<<< курсы", color="secondary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=35)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какая группа?", 'random_id':0, "keyboard": keyboard})
  if response == "четвертыйкурс":
    if step_check(user_id) == 33:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="4п1.17", color="primary")

            ],
            [
              get_button(label="<<< курсы", color="secondary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=35)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какая группа?", 'random_id':0, "keyboard": keyboard})
  if response == "четвертыйкурс":
    if step_check(user_id) == 34:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="4п1.17", color="primary")
            ],
            [
              get_button(label="<<< курсы", color="secondary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=35)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какая группа?", 'random_id':0, "keyboard": keyboard})

def attendance_3(event, user_id, response):
  try:
    if step_check(user_id) == 35:
      if groupa(response) == "real":
        update_attendance(user_id, response)
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Введите слово!", 'random_id':0})
        update_step(user_id, step=36)

      if response == "ltкурсы":
        keyboard = {
              "one_time": True,
              "buttons": [
              [
              get_button(label="Первый курс", color="primary"),
              get_button(label="Второй курс", color="primary")
              ],
              [
              get_button(label="Третий курс", color="primary"),
              get_button(label="Четвертый курс", color="primary")
              ],
              [
                get_button(label="<<< Специальности", color="secondary")
              ]
              ]
          }
        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
        keyboard = str(keyboard.decode('utf-8'))
        update_step(user_id, step=31)
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Укажите группу!", 'random_id':0, "keyboard": keyboard})
  except: pass

def attendance_3_world(event, user_id, response):
  try:
    if step_check(user_id) == 36:
      if groupa(response) != "real":
        update_attendance_world(user_id, response)
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Отлично !", 'random_id':0})
        
        conn = sqlite3.connect('botdatabase.db')
        cursor = conn.cursor()
        data = (" SELECT user_id FROM Groups")
        id_user = cursor.execute(data)
        id_user = id_user.fetchall()

        for i in range(len(id_user)):
                id_id = id_user[i]
                id_id = id_id[0]
                id_id = int(id_id)
                if attendance_check(user_id) == group_check(id_id):
                  update_step(id_id, step=37)
                  update_attendance_world(id_id, response)
                  update_attendance(id_id, group_check(user_id))
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':"Введите слово!", 'random_id':0})
        nullify_step(user_id, step = 0)
        update_attendance_world(user_id, "")
        update_attendance(user_id, "")
  except: pass

def attendance_world_check(event, user_id, response):
  try:
    if response == attendance_check_world(user_id):
        if step_check(user_id) == 37:
            subject = attendance_check(user_id)
            update_attendance(user_id, attendance = subject + " " + str(datetime.strftime(datetime.now(), "%H:%M")))
            vk_session.method('messages.send', {'peer_id': user_id, 'message':"Отлично вы отметелись !", 'random_id':0})
            update_step(user_id, step = 0)
            update_attendance_world(user_id, attendance_world = "")
    elif response != attendance_check_world(user_id):
      if step_check(user_id) == 37:
        update_step(user_id, step = 0)
        update_attendance(user_id, attendance_world = "прогул")
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Не верное слово:(", 'random_id':0})
  except: pass

def regestration_for_teacher(event, user_id, response):
  if response == "преподаватель":
    if user_id != check_db(user_id):
      check_db(user_id)
      database(user_id, user_group="", step=40, rang = 1)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Укажите ваш предмет", 'random_id':0})
    else: vk_session.method('messages.send', {'peer_id': user_id, 'message':"вы уже зарегестрированны", 'random_id':0})

def regestration_for_teacher_step_two(event, user_id, response):
  if "real" == subject_check(response):
    if step_check(user_id) == 40:
      nullify_step(user_id, step = 0)
      update_group(user_id, response)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Буду рад в дальнейшем сотрудничать", 'random_id':0})

def recruitment_team(event, user_id, response):
  if response == "наборвкоманду": 
    vk_session.method('messages.send', {'peer_id': user_id, 'message':"Где вы хотите набрать команду ? \n в колледже/в группе", 'random_id':0})
    update_step(user_id, step = 50)

def recruitment_team_2(event, user_id, response):
  if response == "вгруппе":
    if step_check(user_id) == 50:
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Хорошо в таком случае укажите следующие данные: \n\n 1. Номер группы\n2. Сообщение и ссылку на беседу", 'random_id':0})
      update_step(user_id, step = 51)
  if response == "вколледже":
    if step_check(user_id) == 50:
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"хорошо, в таком случае напишите сообщение которое нужно отправить вместе с ссылкой на беседу", 'random_id':0})
      update_step(user_id, step = 52)

def recruitment_team_21(event, user_id, response):
  try: 
    if step_check(user_id) == 51:
      if groupa(response) == "real":
        update_recruitment_group(user_id, response)
        update_step(user_id, step = 53)
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"теперь укажите сообщение с ссылкой на беседу", 'random_id':0})
  except: pass

def recruitment_team_31(event, user_id, response, bulk):
  try:
    if step_check(user_id) == 53:
      if groupa(response) != "real":
        if rang_check(user_id) < 0.050:
          update_recruitment(user_id, bulk)
          vk_session.method('messages.send', {'peer_id': user_id, 'message':"Ваш запрос направлен на одобрение", 'random_id':0})
          nullify_step(user_id, step=0)
          group = recruitment_group_check(user_id)
          conn = sqlite3.connect('botdatabase.db')
          cursor = conn.cursor()
          data = (" SELECT user_id FROM Groups")
          id_user = cursor.execute(data)
          id_user = id_user.fetchall()

          for i in range(len(id_user)):
              id_id = id_user[i]
              id_id = id_id[0]
              id_id = int(id_id)
              if group == group_check(id_id):
                if rang_check(id_id) >= 0.050:
                  update_step(id_id, step=54)
                  update_recruitment(id_id, str(user_id))
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':f"Сообщение на одобрение: {bulk}", 'random_id':0})
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':"\n\n Одобрить сообщение ? ", 'random_id':0})
        if rang_check(user_id) >= 0.050:
          group = recruitment_group_check(user_id)
          conn = sqlite3.connect('botdatabase.db')
          cursor = conn.cursor()
          data = (" SELECT user_id FROM Groups")
          id_user = cursor.execute(data)
          id_user = id_user.fetchall()
          for i in range(len(id_user)):
              id_id = id_user[i]
              id_id = id_id[0]
              id_id = int(id_id)
              if group == group_check(id_id):
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':bulk, 'random_id':0})
          nullify_step(user_id, step=0)
          update_recruitment_group(user_id, "")
          update_recruitment(user_id, "")
          vk_session.method('messages.send', {'peer_id': user_id, 'message':"надеюсь в скором времени к вам подключаться люди!(или нет)", 'random_id':0})
  except: pass

def recruitment_team_41_check(event, user_id, response, bulk):
  if response == "да": 
    if step_check(user_id) == 54:
      if rang_check(user_id) >= 0.050:
        message_id = recruitment_check(user_id)
        vk_session.method('messages.send', {'peer_id': message_id, 'message':"Ваш запрос одобрен", 'random_id':0})
        group = recruitment_group_check(message_id)
        conn = sqlite3.connect('botdatabase.db')
        cursor = conn.cursor()
        data = (" SELECT user_id FROM Groups")
        id_user = cursor.execute(data)
        id_user = id_user.fetchall()

        for i in range(len(id_user)):
              id_id = id_user[i]
              id_id = id_id[0]
              id_id = int(id_id)
              if group == group_check(id_id):
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':recruitment_check(message_id), 'random_id':0})
        nullify_step(user_id, 0)
        update_recruitment(user_id, "")
        nullify_step(message_id, 0)
        update_recruitment(message_id, "")
        update_recruitment_group(message_id, "")
  if response == "нет": 
    if step_check(user_id) == 54:
      if rang_check(user_id) >= 0.050:
        message_id = recruitment_check(user_id)
        vk_session.method('messages.send', {'peer_id': message_id, 'message':"Ваш запрос откланен", 'random_id':0})
        nullify_step(user_id, 0)
        update_recruitment(user_id, "")
        nullify_step(message_id, 0)
        update_recruitment(message_id, "")
        update_recruitment_group(message_id, "")

def recruitment_team_32(event, user_id, response, bulk):
  try: 
    if step_check(user_id) == 52:
      if rang_check(user_id) >= 0.050:
        if response != "вколледже":
          vk_session.method('messages.send', {'peer_id': user_id, 'message':"Отлично, надеюсь скоро к вам кто нибудь подключиться", 'random_id':0})
          conn = sqlite3.connect('botdatabase.db')
          cursor = conn.cursor()
          data = (" SELECT user_id FROM Groups")
          id_user = cursor.execute(data)
          id_user = id_user.fetchall()

          for i in range(len(id_user)):
              id_id = id_user[i]
              id_id = id_id[0]
              id_id = int(id_id)
              if id_id != user_id:
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':bulk,'random_id':0})
      if rang_check(user_id) < 0.050:
          update_recruitment(user_id, bulk)
          vk_session.method('messages.send', {'peer_id': user_id, 'message':"Ваш запрос направлен на одобрение", 'random_id':0})
          nullify_step(user_id, step=0)
          group = recruitment_group_check(user_id)
          conn = sqlite3.connect('botdatabase.db')
          cursor = conn.cursor()
          data = (" SELECT user_id FROM Groups")
          id_user = cursor.execute(data)
          id_user = id_user.fetchall()

          for i in range(len(id_user)):
              id_id = id_user[i]
              id_id = id_id[0]
              id_id = int(id_id)
              if group == group_check(id_id):
                if rang_check(id_id) >= 0.050:
                  update_step(id_id, step=55)
                  update_recruitment(id_id, str(user_id))
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':f"Сообщение на одобрение: {bulk}", 'random_id':0})
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':"\n\n Одобрить сообщение ? ", 'random_id':0})
  except: pass

def recruitment_team_42_check(event, user_id, response, bulk):
  if response == "да": 
    if step_check(user_id) == 55:
      if rang_check(user_id) >= 0.050:
        message_id = recruitment_check(user_id)
        vk_session.method('messages.send', {'peer_id': message_id, 'message':"Ваш запрос одобрен", 'random_id':0})
        conn = sqlite3.connect('botdatabase.db')
        cursor = conn.cursor()
        data = (" SELECT user_id FROM Groups")
        id_user = cursor.execute(data)
        id_user = id_user.fetchall()

        for i in range(len(id_user)):
              id_id = id_user[i]
              id_id = id_id[0]
              id_id = int(id_id)
              vk_session.method('messages.send', {'peer_id': id_id, 'message':recruitment_check(message_id), 'random_id':0})
        nullify_step(user_id, 0)
        update_recruitment(user_id, "")
        nullify_step(message_id, 0)
        update_recruitment(message_id, "")
        update_recruitment_group(message_id, "")
  if response == "нет": 
    if step_check(user_id) == 55:
      if rang_check(user_id) >= 0.050:
        message_id = recruitment_check(user_id)
        vk_session.method('messages.send', {'peer_id': message_id, 'message':"Ваш запрос откланен", 'random_id':0})
        nullify_step(user_id, 0)
        update_recruitment(user_id, "")
        nullify_step(message_id, 0)
        update_recruitment(message_id, "")
    
def homework_send(event, user_id, response):
  if hw(response) == "real":
    if rang_check(user_id) >= 1: 
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какой группе вы хотите отправить дз?", 'random_id':0})
      update_step(user_id, 60)
    if rang_check(user_id) < 1:
      if homework_check(user_id) == "":
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Домашки пока нет", 'random_id':0})
      else:
        vk_session.method('messages.send', {'peer_id': user_id, 'message':homework_check(user_id), 'random_id':0})

def homework_send_2(event, user_id, response):
  if groupa(response) == "real":
    if step_check(user_id) == 60:
      update_homework(user_id, response)
      update_step(user_id, 61)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"какое будет домашнее задание?", 'random_id':0})
        
def homework_send_3(event, user_id, response, bulk): 
  try:
    if step_check(user_id) == 61:
      if groupa(response) != "real":
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Домашнее задание отправленно!", 'random_id':0})
        conn = sqlite3.connect('botdatabase.db')
        cursor = conn.cursor()
        data = (" SELECT user_id FROM Groups")
        id_user = cursor.execute(data)
        id_user = id_user.fetchall()
        grupa = homework_check(user_id)

        for i in range(len(id_user)):
              id_id = id_user[i]
              id_id = id_id[0]
              id_id = int(id_id)
              if grupa == group_check(id_id):
                day_homework(id_id, bulk, group_check(user_id))
                if chose_homework_check(id_id) == '1':
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':f"домашнее задание по предмету {group_check(user_id)} \n {bulk}", 'random_id':0})
                if chose_homework_check(id_id) == "":
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':f"домашнее задание по предмету {group_check(user_id)} \n {bulk}", 'random_id':0})
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':"\n Если хотите настроить отравку вам уведомлений то напишите - уведомления", 'random_id':0})
                
                
        nullify_step(user_id, 0)
        update_homework(user_id, "")
  except: pass

def homework_send_notification(event, user_id, response):
  if response == "уведомление":
    update_step(user_id, step = 70)
    vk_session.method('messages.send', {'peer_id': user_id, 'message':"Хотите ли вы получать домашнее задание сразу\n да\нет", 'random_id':0})

def homework_send_notification_2(event, user_id, response):
  try: 
    if response == "да":
      if step_check(user_id) == 70:
        update_chose_homework(user_id, 1)
        nullify_step(user_id, 0)
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"отлично! теперь буду прислать вам домашнее задание ", 'random_id':0})
    if response == "нет":
      if step_check(user_id) == 70:
        update_chose_homework(user_id, 0)
        nullify_step(user_id, 0)
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Хорошо не буду беспокоить", 'random_id':0})   
  except: pass 

def delete_homework(bot_on):
  if bot_on == "on":
    if str(datetime.strftime(datetime.now(), "%H:%M")) == '12:40':
        print("дом")
        conn = sqlite3.connect('botdatabase.db')
        cursor = conn.cursor()
        data = (" SELECT user_id FROM Groups")
        id_user = cursor.execute(data)
        id_user = id_user.fetchall()

        for i in range(len(id_user)):
          id_id = id_user[i]
          id_id = id_id[0]
          id_id = int(id_id)
          update_homework(id_id, "")




#___________________________________________________________________________________________________________________

#                                            Административные функции
#_________________________________________________________________________________________________________________________

def rang_update(event, user_id, response):
  try:
    if rang_check(user_id) == 1000:
      if response == "rangupdate":
        update_step(user_id, step = 101)
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Введите id пользователя", 'random_id':0})
  except: pass

def rang_update_step_two(event, user_id, response):
  try:
    if rang_check(user_id) == 1000:
      if step_check(user_id) == 101:
        if response != "rangupdate":
          update_bulk(user_id, response)
          vk_session.method('messages.send', {'peer_id': user_id, 'message':" Какой ранг ?", 'random_id':0})
          update_step(user_id, step = 102)
  except: pass

def rang_update_step_3(event, user_id, response, bulk): 
        if response == "ученик":
          if rang_check(user_id) == 1000:        
            if step_check(user_id) == 102:
              new_rang = 0.010
              id_id = bulk_check_id(user_id)
              print(id_id)
              update_rang(bulk_check_id(user_id), new_rang)
              vk_session.method('messages.send', {'peer_id': bulk_check_id(user_id), 'message':f"Ваш ранг теперь {response}", 'random_id':0})
              update_bulk(user_id, "")
              nullify_step(user_id, step = 0)
              vk_session.method('messages.send', {'peer_id': user_id, 'message':"Готово", 'random_id':0})
        if response == "староста":
          if rang_check(user_id) == 1000:        
            if step_check(user_id) == 102:
              new_rang = 0.050
              id_id = bulk_check_id(user_id)
              print(id_id)
              update_rang(bulk_check_id(user_id), new_rang)
              vk_session.method('messages.send', {'peer_id': bulk_check_id(user_id), 'message':f"Ваш ранг теперь {response}", 'random_id':0})
              update_bulk(user_id, "")
              nullify_step(user_id, step = 0)
              vk_session.method('messages.send', {'peer_id': user_id, 'message':"Готово", 'random_id':0})
        if response == "учитель":
          if rang_check(user_id) == 1000:        
            if step_check(user_id) == 102:
              new_rang = 1
              id_id = bulk_check_id(user_id)
              print(id_id)
              update_rang(bulk_check_id(user_id), new_rang)
              vk_session.method('messages.send', {'peer_id': bulk_check_id(user_id), 'message':f"Ваш ранг теперь {response}", 'random_id':0})
              update_bulk(user_id, "")
              nullify_step(user_id, step = 0)
              vk_session.method('messages.send', {'peer_id': user_id, 'message':"Готово", 'random_id':0})
        if response == "куратор":
          if rang_check(user_id) == 1000:        
            if step_check(user_id) == 102:
              new_rang = 0.070
              id_id = bulk_check_id(user_id)
              print(id_id)
              update_rang(bulk_check_id(user_id), new_rang)
              vk_session.method('messages.send', {'peer_id': bulk_check_id(user_id), 'message':f"Ваш ранг теперь {response}", 'random_id':0})
              update_bulk(user_id, "")
              nullify_step(user_id, step = 0)
              vk_session.method('messages.send', {'peer_id': user_id, 'message':"Готово", 'random_id':0})
        