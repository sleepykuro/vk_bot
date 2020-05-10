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


tokenn = open(r"C:\Users\egor\Desktop\token.txt", "r")
tokenn = tokenn.read()
vk_session = vk_api.VkApi(token=tokenn)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

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
      vk_session.method('messages.send', {'user_id': user_id, 'message':'Введите ваш статус в колледже', 'random_id':0})

def regestration_two(event, user_id, response): 
    if response == "ученик" or response =="студент":
      try:
        if rang_check(user_id) == 0:
          if step_check(user_id) == 1:
            response = "0.010"
            update_rang(user_id, response)
            vk_session.method('messages.send', {'user_id': user_id, 'message':'Отлично! Теперь вам доступен весь мой фукнционал', 'random_id':0})
            nullify_step(user_id, step=0)
          elif step_check(user_id) == 0: 
            vk_session.method('messages.send', {'user_id': user_id, 'message':'Сначала введите вашу группу', 'random_id':0})
        else:
          if rang_check(user_id) < 1000:
            vk_session.method('messages.send', {'user_id': user_id, 'message':'Поменять статус, можно только после одобрения Куратора', 'random_id':0})
      except IndexError:
        vk_session.method('messages.send', {'user_id': user_id, 'message':'Сначала введите вашу группу', 'random_id':0})

def regestration_for_kurator(event, user_id, response): #Поменял пароль
  if response == "куратор20202020":
    update_step(user_id, 80)
    vk_session.method('messages.send', {'user_id': user_id, 'message':'Укажите группу которую будете курировать', 'random_id':0})

def regestration_for_kurator_2(event, user_id, response):
  try: 
    if step_check(user_id) == 80:
      if groupa(response) == "real":
        update_group_for_startsta(user_id, response)
        update_rang(user_id, "0.070")
        nullify_step(user_id, 0)
        vk_session.method('messages.send', {'user_id': user_id, 'message':'Отлично! Надеюсь вы будете хорошим Куратором!', 'random_id':0})
  except: pass

def regestration_for_starosta(event, user_id, response):
  if response == "староста":
    update_step(user_id, 81)
    vk_session.method('messages.send', {'user_id': user_id, 'message':'Пароль на одобрение статуса отправлен куратору!', 'random_id':0})
    vk_session.method('messages.send', {'user_id': user_id, 'message':'Введите пароль', 'random_id':0})
    update_group_for_startsta(user_id, random.randint(1000, 9999))
    id_user = all_user_ids()
    for i in range(len(id_user)):
      id_id = take_int_id(i, id_user)
      if group_check(user_id) == group_for_startsta_check(id_id):
        vk_session.method('messages.send', {'peer_id': id_id, 'message':f"Пароль на получения статуса старосты {group_for_startsta_check(user_id)}", 'random_id':0})

def regestration_for_starosta_2(event, user_id, response):
  try:
    if step_check(user_id) == 81:
      if response == group_for_startsta_check(user_id):
        nullify_step(user_id, 0)
        update_rang(user_id, "0.050")
        update_group_for_startsta(user_id, "")
        vk_session.method('messages.send', {'user_id': user_id, 'message':'Надеюсь ты будешь хорошим старостой !', 'random_id':0})
  except: pass

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
           get_button(label="Уведомление", color="primary")],
          [get_button(label="Набор в команду", color="primary")]
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
        \n7. Набор в команду: Рассылка ссылки на беседу группе/колледжу
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
          [get_button(label="Посещаемость", color="primary"),
           get_button(label="Набор в команду", color="primary")]
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
        \n8. Набор в команду: Рассылка ссылки на беседу группе/колледжу
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
          [get_button(label="Посещаемость", color="primary"),
           get_button(label="Набор в команду", color="primary")]
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
        \n8. Набор в команду: Рассылка ссылки на беседу группе/колледжу
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
          [get_button(label="Посещаемость", color="primary"),
           get_button(label="Набор в команду", color="primary")]
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
        \n7. Посещаемость: Проверка посещаемости
        \n8. Набор в команду: Рассылка ссылки на беседу группе/колледжу
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
          [get_button(label="Смена ранга", color="primary"),
           get_button(label="Набор в команду", color="primary")]
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
        \n8. Набор в команду: Рассылка ссылки на беседу группе/колледжу
        """, 'random_id':0, "keyboard": keyboard})     
  except:
    if response == "help" or response == "помощь" :
      keyboard = {
        "one_time": True,
        "buttons": [
        [get_button(label="Help", color="primary"),
         get_button(label="Регистрация", color="primary")]
        ]
      }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))   
      vk_session.method('messages.send', {'user_id': user_id, 'message':
      """
      \n1. Help: Список комманд доступный вашему статусу (Не зарегистрированный пользователь)
      \n2. Регистрация:  Информация о том как зарегестрировать себя в боте
      """, 'random_id':0, "keyboard": keyboard})

def bulk_message(event, user_id, response):
  if response == "массовоесообщение":    
    vk_session.method('messages.send', {'peer_id': user_id, 'message':"Кому вы хотите отправить сообщение ?", 'random_id':0, "keyboard": bulk_keyboard})

def bulk_message_take(event, user_id, response):
  if response == "колледжу":
    update_step(user_id, 10)
    vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какое сообщение отправить?", 'random_id':0})
  if response == "группе":
    update_step(user_id, 11)
    vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какое сообщение отправить?", 'random_id':0})

def bulk_group_message(event,user_id, response, bulk):
  try:
    if response != "колледжу" and response != "группе" and response != "сообщение":
      if step_check(user_id) == 10:
        if rang_check(user_id) >= 0.100:
          vk_session.method('messages.send', {'peer_id': user_id, 'message':"Сообщние отправленно!", 'random_id':0})
          nullify_step(user_id, 0)
          id_user = all_user_ids()
          for i in range(len(id_user)):
            id_id = take_int_id(i, id_user)
            if id_id != user_id:
              vk_session.method('messages.send', {'peer_id': id_id, 'message':bulk, 'random_id':0})
        elif rang_check(user_id) < 0.070:
          update_bulk(user_id, bulk)
          group = group_check(user_id)
          id_user = all_user_ids()
          while True:
            id_id = id_user[i]
            id_id = id_id[0]
            id_id = int(id_id)
            if group == group_for_startsta_check(id_id):
              if rang_check(id_id) >= 0.70:
                if bulk_check_id(id_id) == "":
                  vk_session.method('messages.send', {'user_id': user_id, 'message':"Ваше сообение направленно на одобрение Куратору", 'random_id':0})
                  update_step(id_id, step=12)
                  update_bulk(id_id, str(user_id))
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':f"Сообщение на одобрение: {bulk}", 'random_id':0})
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':"\n\n Одобрить сообщение ? ", 'random_id':0, "keyboard": keyboard_yes_no})
                  break
                elif bulk_check_id(id_id) != "":
                  nullify_step(user_id, 0)
                  vk_session.method('messages.send', {'peer_id': user_id, 'message':"сообщение другого пользователя пока не одобренно, попробуйте позже", 'random_id':0})
                  break
    if response != "колледжу" and response != "группе" and response != "сообщение":
      if step_check(user_id) == 11:
        if rang_check(user_id) >= 0.050 and rang_check(user_id) < 0.070:
          id_user = all_user_ids()
          for i in range(len(id_user)):
            id_id = take_int_id(i, id_user)
            if group_check(user_id) == group_check(id_id):
              if id_id != user_id:
                vk_session.method('messages.send', {'peer_id': id_id, 'message':bulk, 'random_id':0})

      elif rang_check(user_id) < 0.050:
          update_bulk(user_id, bulk)
          group = group_check(user_id)
          id_user = all_user_ids()
          for i in range(len(id_user)):
            id_id = take_int_id(i, id_user)
            if group == group_check(id_id):
              if rang_check(id_id) >= 0.050:
                if bulk_check_id(id_id) == "":
                  vk_session.method('messages.send', {'user_id': user_id, 'message':"Ваше сообение направленно на одобрение старосте", 'random_id':0})
                  update_step(id_id, step=12)
                  update_bulk(id_id, str(user_id))
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':f"Сообщение на одобрение: {bulk}", 'random_id':0})
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':"\n\n Одобрить сообщение ? ", 'random_id':0, "keyboard": keyboard_yes_no})
                elif bulk_check_id(id_id) != "":
                  nullify_step(user_id, 0)
                  vk_session.method('messages.send', {'peer_id': user_id, 'message':"сообщение другого пользователя пока не одобренно, попробуйте позже", 'random_id':0})                   
  except: pass
  
def bulk_message_check(event,user_id, response): 
  try:
    if response == "да" or response == "одобряю": 
      if step_check(user_id) == 12:
        message_id = bulk_check_id(user_id)
        vk_session.method('messages.send', {'peer_id': message_id, 'message':"Отправка вашего сообщения одобренна!", 'random_id':0})
        bulk = bulk_check(message_id)
        id_user = all_user_ids()
        for i in range(len(id_user)):
          id_id = take_int_id(i, id_user)
          if rang_check(id_id) < 0.100:
            vk_session.method('messages.send', {'peer_id': id_id, 'message':bulk, 'random_id':0})
        nullify_step(user_id, step = 0)
        update_bulk(user_id, "")
        update_bulk(message_id, "")
    elif response == "нет" or response == "неодобряю": 
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
        id_user = all_user_ids()
        for i in range(len(id_user)):
          id_id = take_int_id(i, id_user)
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
          vk_session.method('messages.send', {'peer_id': user_id, 'message':f"Молодец! Мое число действительно было {a}", 'random_id':0})
        else: 
          nullify_step(user_id, step=0)
          vk_session.method('messages.send', {'peer_id': user_id, 'message':"К сожалению ты не угадал (", 'random_id':0})
      
    except: pass

def timetable(event, user_id, response):
  if response == "время":
      h = What()
      vk_session.method('messages.send', {'peer_id': user_id, 'message':h.give_information(), 'random_id':0})

def attendance_1(event, user_id, response):
  if response == "посещаемость":
    if rang_check(user_id) >= 1:
      update_step(user_id, step=30)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Пожалуйста выберите Курс", 'random_id':0, "keyboard": keyboard_profilse})
    if rang_check(user_id) >= 0.050 and rang_check(user_id) < 0.070:
      group = group_check(user_id)
      id_user = all_user_ids()
      for i in range(len(id_user)):
        id_id = take_int_id(i, id_user)
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
    if rang_check(user_id) == 0.070:
      group = group_for_startsta_check(user_id)
      id_user = all_user_ids()
      for i in range(len(id_user)):
        id_id = take_int_id(i, id_user)
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
  try:
    if step_check(user_id) == 30: 
      if response == "программисты":
        update_step(user_id, step=31)
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Укажите группу!", 'random_id':0, "keyboard": keyboard_course})
      if response == "разработчики":
          update_step(user_id, step=32)
          vk_session.method('messages.send', {'peer_id': user_id, 'message':"Укажите группу!", 'random_id':0, "keyboard": keyboard_course})
      if response == "коммерция":
        update_step(user_id, step=33)
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Укажите группу!", 'random_id':0, "keyboard": keyboard_course})
      if response == "безопасники":
        update_step(user_id, step=34)
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Укажите курс!", 'random_id':0, "keyboard": keyboard_course})
  except: pass

def attendance_2(event, user_id, response):
  if response == "ltспециальности":
    if step_check(user_id) == 31 or step_check(user_id) == 32 or step_check(user_id) == 33 or step_check(user_id) == 34:
      update_step(user_id, step=30)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Пожалуйста выберите специальность", 'random_id':0, "keyboard": keyboard_profilse})

  if response == "первыйкурс":
    if step_check(user_id) == 31:
      course_letter = groups["course_1"] + groups["letter_1"]
      year = groups["year_1"]
  if response == "первыйкурс":
    if step_check(user_id) == 32:
      course_letter = groups["course_1"] + groups["letter_2"]
      year = groups["year_1"]
  if response == "первыйкурс":
    if step_check(user_id) == 33:
      course_letter = groups["course_1"] + groups["letter_3"]
      year = groups["year_1"]
  if response == "первыйкурс":
    if step_check(user_id) == 34:
      course_letter = groups["course_1"] + groups["letter_4"]
      year = groups["year_1"]
  if response == "второйкурс":
    if step_check(user_id) == 31:
      course_letter = groups["course_2"] + groups["letter_1"]
      year = groups["year_2"]
  if response == "второйкурс":
    if step_check(user_id) == 32:
      course_letter = groups["course_2"] + groups["letter_2"]
      year = groups["year_2"]
  if response == "второйкурс":
    if step_check(user_id) == 33:
      course_letter = groups["course_2"] + groups["letter_3"]
      year = groups["year_2"]
  if response == "второйкурс":
    if step_check(user_id) == 34:
      course_letter = groups["course_2"] + groups["letter_4"]
      year = groups["year_2"]
  if response == "третийкурс":
    if step_check(user_id) == 31:
      course_letter = groups["course_3"] + groups["letter_1"]
      year = groups["year_3"]
  if response == "третийкурс":
    if step_check(user_id) == 32:
      course_letter = groups["course_3"] + groups["letter_2"]
      year = groups["year_3"]
  if response == "третийкурс":
    if step_check(user_id) == 33:
      course_letter = groups["course_3"] + groups["letter_3"]
      year = groups["year_3"]
  if response == "третийкурс":
    if step_check(user_id) == 34:
      course_letter = groups["course_3"] + groups["letter_4"]
      year = groups["year_3"]
  if response == "четвертыйкурс":
    if step_check(user_id) == 31:
      course_letter = groups["course_4"] + groups["letter_1"]
      year = groups["year_4"]
  if response == "четвертыйкурс":
    if step_check(user_id) == 32:
      course_letter = groups["course_4"] + groups["letter_1"]
      year = groups["year_4"]
  if response == "четвертыйкурс":
    if step_check(user_id) == 33:
      course_letter = groups["course_4"] + groups["letter_1"]
      year = groups["year_4"]
  if response == "четвертыйкурс":
    if step_check(user_id) == 34: 
      course_letter = groups["course_4"] + groups["letter_1"]
      year = groups["year_4"]   
  try:
    keyboard = {
      "one_time": True,
      "buttons": [
      [get_button(label=f"{course_letter}1.{year}", color="primary"),
      get_button(label=f"{course_letter}2.{year}", color="primary"),
      get_button(label=f"{course_letter}3.{year}", color="primary"),]
      ]
    }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    update_step(user_id, step=35)
    vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какая группа?", 'random_id':0, "keyboard": keyboard})
  except: pass

def attendance_3(event, user_id, response):
  try:
    if step_check(user_id) == 35:
      if groupa(response) == "real":
        update_attendance(user_id, response)
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Введите слово!", 'random_id':0})
        update_step(user_id, step=36)
  except: pass

def attendance_3_world(event, user_id, response):
  try:
    if step_check(user_id) == 36:
      if groupa(response) != "real":
        update_attendance_world(user_id, response)
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Отлично !", 'random_id':0})
        id_user = all_user_ids()
        for i in range(len(id_user)):
          id_id = take_int_id(i, id_user)
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
        update_attendance_world(user_id, "")
    elif response != attendance_check_world(user_id):
      if step_check(user_id) == 37:
        update_step(user_id, step = 0)
        update_attendance(user_id, "прогул")
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
    vk_session.method('messages.send', {'peer_id': user_id, 'message':"Где вы хотите набрать команду ? \n в колледже/в группе", 'random_id':0, "keyboard": recruitment_team_keyboard})
    update_step(user_id, step = 50)

def recruitment_team_2(event, user_id, response):
  if response == "вгруппе":
    if step_check(user_id) == 50:
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Хорошо, в таком случае укажите следующие данные: \n\n 1. Номер группы\n2. Сообщение и ссылку на беседу", 'random_id':0})
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
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Теперь укажите сообщение с ссылкой на беседу", 'random_id':0})
  except: pass

def recruitment_team_31(event, user_id, response, bulk):
  try:
    if step_check(user_id) == 53:
      if groupa(response) != "real":
        if rang_check(user_id) < 0.050:
          update_recruitment(user_id, bulk)
          nullify_step(user_id, step=0)
          group = recruitment_group_check(user_id)
          id_user = all_user_ids()
          for i in range(len(id_user)):
            id_id = take_int_id(i, id_user)
            if group == group_check(id_id):
              if rang_check(id_id) >= 0.050:
                if recruitment_check(id_id) == "":
                  update_step(id_id, step=54)
                  update_recruitment(id_id, str(user_id))
                  vk_session.method('messages.send', {'peer_id': user_id, 'message':"Ваш запрос направлен на одобрение", 'random_id':0})
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':f"Сообщение на одобрение: {bulk}", 'random_id':0})
                  keyboard = {
                    "one_time": True,
                    "buttons": [
                    [get_button(label="Да", color="positive"),
                     get_button(label="Нет", color="negative")]
                    ]
                  }

                  keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                  keyboard = str(keyboard.decode('utf-8'))

                  vk_session.method('messages.send', {'peer_id': id_id, 'message':"\n\n Одобрить сообщение ? ", 'random_id':0, "keyboard": keyboard})
                elif recruitment_check(id_id) != "":
                  update_recruitment(user_id, "")
                  vk_session.method('messages.send', {'peer_id': user_id, 'message':"Сообщение другого пользователя пока не одобренно, поэтому попробуйте позже", 'random_id':0})

        if rang_check(user_id) >= 0.050:
          group = recruitment_group_check(user_id)
          id_user = all_user_ids()
          for i in range(len(id_user)):
            id_id = take_int_id(i, id_user)
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
        nullify_step(user_id, 0)
        message_id = recruitment_check(user_id)
        vk_session.method('messages.send', {'peer_id': message_id, 'message':"Ваш запрос одобрен", 'random_id':0})
        group = recruitment_group_check(message_id)
        id_user = all_user_ids()
        for i in range(len(id_user)):
          id_id = take_int_id(i, id_user)
          if group == group_check(id_id):
            vk_session.method('messages.send', {'peer_id': id_id, 'message':recruitment_check(message_id), 'random_id':0})
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
          id_user = all_user_ids()
          for i in range(len(id_user)):
            id_id = take_int_id(i, id_user)
            if id_id != user_id:
              vk_session.method('messages.send', {'peer_id': id_id, 'message':bulk,'random_id':0})
      if rang_check(user_id) < 0.050:
          update_recruitment(user_id, bulk)
          vk_session.method('messages.send', {'peer_id': user_id, 'message':"Ваш запрос направлен на одобрение", 'random_id':0})
          nullify_step(user_id, step=0)
          group = recruitment_group_check(user_id)
          id_user = all_user_ids()
          for i in range(len(id_user)):
            id_id = take_int_id(i, id_user)
            if group == group_check(id_id):
              if rang_check(id_id) >= 0.050:
                update_step(id_id, step=55)
                update_recruitment(id_id, str(user_id))
                vk_session.method('messages.send', {'peer_id': id_id, 'message':f"Сообщение на одобрение: {bulk}", 'random_id':0})
                vk_session.method('messages.send', {'peer_id': id_id, 'message':"\n\n Одобрить сообщение ? ", 'random_id':0, "keyboard": keyboard_yes_no})
  except: pass

def recruitment_team_42_check(event, user_id, response, bulk):
  if response == "да": 
    if step_check(user_id) == 55:
      if rang_check(user_id) >= 0.050:
        message_id = recruitment_check(user_id)
        vk_session.method('messages.send', {'peer_id': message_id, 'message':"Ваш запрос одобрен", 'random_id':0})
        id_user = all_user_ids()
        for i in range(len(id_user)):
          id_id = take_int_id(i, id_user)
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
        vk_session.method('messages.send', {'peer_id': message_id, 'message':"Ваш запрос отклонен", 'random_id':0})
        nullify_step(user_id, 0)
        update_recruitment(user_id, "")
        nullify_step(message_id, 0)
        update_recruitment(message_id, "")
    
def homework_send(event, user_id, response):
  if hw(response) == "real":
    if rang_check(user_id) >= 1:    
      keyboard = {
        "one_time": True,
        "buttons": [
        [get_button(label="Программисты", color="primary")],
        [get_button(label="Разроботчики", color="primary"),
         get_button(label="Коммерция", color="primary")],
        [get_button(label="Безопасники", color="primary")]
        ]
      }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=62)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Пожалуйста выберите специальность", 'random_id':0, "keyboard": keyboard})
    elif rang_check(user_id) < 1:
      if homework_check == "":
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Домашки пока нет", 'random_id':0})
      elif homework_check != "":
        try: 
          homework = homework_check(user_id)
          vk_session.method('messages.send', {'peer_id': user_id, 'message':f"{homework}", 'random_id':0})
        except:
          vk_session.method('messages.send', {'peer_id': user_id, 'message':"Домашки пока нет", 'random_id':0})

def homework_send_1(event, user_id, response):
  try: 
    if step_check(user_id) == 62:
      keyboard = {
        "one_time": True,
        "buttons": [
        [get_button(label="Первый курс", color="primary"),
        get_button(label="Второй курс", color="primary")],
        [get_button(label="Третий курс", color="primary"),
        get_button(label="Четвертый курс", color="primary")],
        [get_button(label="<<< Специальности", color="secondary")]
        ]
      }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
    if response == "программисты":
      update_step(user_id, step=63)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Введите курс", 'random_id':0, "keyboard": keyboard})
    if response == "разработчики":
      update_step(user_id, step=64)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Введите курс", 'random_id':0, "keyboard": keyboard})
    if response == "коммерция":
      update_step(user_id, step=65)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Введите курс", 'random_id':0, "keyboard": keyboard})
    if response == "безопасники":
      update_step(user_id, step=66)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Введите курс", 'random_id':0, "keyboard": keyboard})
  except: pass

def homework_send_1_2(event, user_id, response):
  if response == "ltспециальности":
    if step_check(user_id) == 63 or step_check(user_id) == 64 or step_check(user_id) == 65 or step_check(user_id) == 66:
      keyboard = {
        "one_time": True,
        "buttons": [
        [get_button(label="Программисты", color="primary")],
        [get_button(label="Разработчики", color="primary"),
         get_button(label="Коммерция", color="primary")],
        [get_button(label="Безопасники", color="primary")]
        ]
      }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=62)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Пожалуйста выберите специальность", 'random_id':0, "keyboard": keyboard})

  if response == "первыйкурс":
    if step_check(user_id) == 63:
      course_letter = groups["course_1"] + groups["letter_1"]
      year = groups["year_1"]
  if response == "первыйкурс":
    if step_check(user_id) == 64:
      course_letter = groups["course_1"] + groups["letter_2"]
      year = groups["year_1"]
  if response == "первыйкурс":
    if step_check(user_id) == 65:
      course_letter = groups["course_1"] + groups["letter_3"]
      year = groups["year_1"]
  if response == "первыйкурс":
    if step_check(user_id) == 66:
      course_letter = groups["course_1"] + groups["letter_4"]
      year = groups["year_1"]
  if response == "второйкурс":
    if step_check(user_id) == 63:
      course_letter = groups["course_2"] + groups["letter_1"]
      year = groups["year_2"]
  if response == "второйкурс":
    if step_check(user_id) == 64:
      course_letter = groups["course_2"] + groups["letter_2"]
      year = groups["year_2"]
  if response == "второйкурс":
    if step_check(user_id) == 65:
      course_letter = groups["course_2"] + groups["letter_3"]
      year = groups["year_2"]
  if response == "второйкурс":
    if step_check(user_id) == 66:
      course_letter = groups["course_2"] + groups["letter_4"]
      year = groups["year_2"]
  if response == "третийкурс":
    if step_check(user_id) == 63:
      course_letter = groups["course_3"] + groups["letter_1"]
      year = groups["year_3"]
  if response == "третийкурс":
    if step_check(user_id) == 64:
      course_letter = groups["course_3"] + groups["letter_2"]
      year = groups["year_3"]
  if response == "третийкурс":
    if step_check(user_id) == 65:
      course_letter = groups["course_3"] + groups["letter_3"]
      year = groups["year_3"]
  if response == "третийкурс":
    if step_check(user_id) == 66:
      course_letter = groups["course_3"] + groups["letter_4"]
      year = groups["year_3"]
  if response == "четвертыйкурс":
    if step_check(user_id) == 63:
      course_letter = groups["course_4"] + groups["letter_1"]
      year = groups["year_4"]
  if response == "четвертыйкурс":
    if step_check(user_id) == 64:
      course_letter = groups["course_4"] + groups["letter_1"]
      year = groups["year_4"]
  if response == "четвертыйкурс":
    if step_check(user_id) == 65:
      course_letter = groups["course_4"] + groups["letter_1"]
      year = groups["year_4"]
  if response == "четвертыйкурс":
    if step_check(user_id) == 66: 
      course_letter = groups["course_4"] + groups["letter_1"]
      year = groups["year_4"]   
  try:
    keyboard = {
      "one_time": True,
      "buttons": [
      [get_button(label=f"{course_letter}1.{year}", color="primary"),
      get_button(label=f"{course_letter}2.{year}", color="primary"),
      get_button(label=f"{course_letter}3.{year}", color="primary"),]
      ]
    }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    update_step(user_id, step=67)
    vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какая группа?", 'random_id':0, "keyboard": keyboard})
  except: pass

def homework_send_2(event, user_id, response):
  if groupa(response) == "real":
    if step_check(user_id) == 67:
      update_homework(user_id, response)
      update_step(user_id, 68)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"какое будет домашнее задание?", 'random_id':0})
      
def homework_send_3(event, user_id, response, bulk): 
  try:
    if step_check(user_id) == 68:
      if groupa(response) != "real":
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Домашнее задание отправленно!", 'random_id':0})
        grupa = homework_check(user_id)
        id_user = all_user_ids()
        for i in range(len(id_user)):
          id_id = take_int_id(i, id_user)
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
    vk_session.method('messages.send', {'peer_id': user_id, 'message':"Хотите ли вы получать домашнее задание сразу ?", 'random_id':0, "keyboard": keyboard_yes_no})

def homework_send_notification_2(event, user_id, response):
  try: 
    if response == "да":
      if step_check(user_id) == 70:
        update_chose_homework(user_id, 1)
        nullify_step(user_id, 0)
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Отлично! Теперь буду прислать вам домашнее задание ", 'random_id':0})
    if response == "нет":
      if step_check(user_id) == 70:
        update_chose_homework(user_id, 0)
        nullify_step(user_id, 0)
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Хорошо, не буду беспокоить", 'random_id':0})   
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
          vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какой ранг ?", 'random_id':0})
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
        