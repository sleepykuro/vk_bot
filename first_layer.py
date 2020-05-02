from second_layer import *
from new_db import *
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import time
import random
import sqlite3
import re

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
  pass

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
            regular = re.compile("сообщение колледжу:")
            response = regular.sub('' , response)
            regular = re.compile("сообщение группе:")
            response = regular.sub('' , response)
            return response
def user_message(event,user_id, response):
  if event.type == VkEventType.MESSAGE_NEW:
    print('Сообщение от ' + str(user_id) + ' пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
    print('Текст сообщения: ' + str(response))

def hello(event,user_id, response):
  response = hello_check(response)
  if response == 'привет':
    hi_answer = hi_answer_random('hi')
    vk_session.method('messages.send', {'user_id': user_id, 'message':hi_answer, 'random_id':0}) 

def regestration_info(event,user_id, response):
  if response == 'какзарегистрироваться':
    vk_session.method('messages.send', {'user_id': user_id, 'message':'Что бы зарегестрироваться: \n 1.Напишите номер вашей группы \n 2.Напишите ваш статус в колледже (доступен только "ученик")', 'random_id':0}) 

def regestration_one(event, user_id, response):
  if user_id != check_db(user_id):
    enter = groupa(response)
    if enter == 'real':
      step = 1
      database(user_id, response, step, rang = '0', bulk = '')
      vk_session.method('messages.send', {'user_id': user_id, 'message':'Введите пожалуйста ваш статус в колледже', 'random_id':0})

def regestration_two(event, user_id, response):
    if response == "ученик":
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
          vk_session.method('messages.send', {'user_id': user_id, 'message':'Поменять статус, можно только после одобрения Куратора', 'random_id':0})
      except IndexError:
        vk_session.method('messages.send', {'user_id': user_id, 'message':'сначала введите вашу группу', 'random_id':0})

def help_user(event,user_id, response):
  if response == "help" :
    vk_session.method('messages.send', {'user_id': user_id, 'message':"""1. Привет 
    \n2. Help (Список комманд доступный вашему статусу)
    \n3. Как зарегестрироваться ? (Дает всю информацию о том как зарегестрировать себя в боте)
    \n4. сообщение колледжу: тут ваше сообщение (писать так же как в примере, одним сообщением, и ваше сообщение будет отправленно всему колледжу)
    \n5. сообщение группе: тут ваше сообщение (писать так же как в примере, одним сообщением, и ваше сообщение будет отправленно всей группе(в разроботке))
    сообщение колледжу: тут ваше сообщение (писать так же как в примере, одним сообщением, и ваше сообщение будет отправленно всему колледжу)
    \n6. Игра (простая игра) 
    \n7. Время(показывает время до конца пары)""", 'random_id':0})

def bulk_message(event,user_id, response, bulk):
  try:
    if "сообщениеколледжу" in response:
      if rang_check(user_id) >= 0.100:
        conn = sqlite3.connect('botdatabase.db')
        cursor = conn.cursor()
        data = (" SELECT user_id FROM Groups")
        id_user = cursor.execute(data)
        id_user = id_user.fetchall()

        for i in range(len(id_user)):
            id_id = id_user[i]
            id_id = id_id[0]
            id_id = int(id_id)
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
                update_step(id_id, step=6)
                update_bulk(id_id, str(user_id))
                vk_session.method('messages.send', {'peer_id': id_id, 'message':f"Сообщение на одобрение: {bulk}", 'random_id':0})
                vk_session.method('messages.send', {'peer_id': id_id, 'message':"\n\n Одобрить сообщение ? ", 'random_id':0})
                break
  except: pass
def bulk_message_check(event,user_id, response):
  if response == "да": 
        if step_check(user_id) == 6:
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
  elif response == "нет": 
          if step_check(user_id) == 6:
            message_id = int(bulk_check(user_id))
            vk_session.method('messages.send', {'peer_id': message_id, 'message':"Отправка вашего сообщения отклонена", 'random_id':0})
            nullify_step(user_id, step = 0)
            update_bulk(user_id, "")
            update_bulk(message_id, "")

def group_message(event,user_id, response, bulk):
  try:
    if "сообщениегруппе" in response:
      if rang_check(user_id) >= 0.050:
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
                update_step(id_id, step=6)
                update_bulk(id_id, str(user_id))
                vk_session.method('messages.send', {'peer_id': id_id, 'message':f"Сообщение на одобрение: {bulk}", 'random_id':0})
                vk_session.method('messages.send', {'peer_id': id_id, 'message':"\n\n Одобрить сообщение ? ", 'random_id':0})
  except: pass
def group_message_check(event,user_id, response):
      if response == "да": 
        if step_check(user_id) == 6:
          message_id = bulk_check_id(user_id)
          # message_id = int(message_id)
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
      elif response == "нет": 
        if step_check(user_id) == 6:
          message_id = int(bulk_check(user_id))
          vk_session.method('messages.send', {'peer_id': message_id, 'message':"Отправка вашего сообщения отклонена", 'random_id':0})
          nullify_step(user_id, step = 0)
          update_bulk(user_id, "")
          update_bulk(message_id, "")

def game_1(event,user_id, response):
  if response == 'игра':
    update_step(user_id, step = 5)
    vk_session.method('messages.send', {'peer_id': user_id, 'message':"Я загадал число от 1 до 5, попробуй угадать!", 'random_id':0})

def game_2(event,user_id, response):
  if response != "игра":
    try:
      if step_check(user_id) == 5:
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
      update_step(user_id, step=9)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"пожалуйста укажите номер группы", 'random_id':0})
    else: vk_session.method('messages.send', {'peer_id': user_id, 'message':"Вы не являетесь преподователем ", 'random_id':0})

def attendance_2(event, user_id, response):
  try:
    if step_check(user_id) == 9:
      if groupa(response) == "real":
        update_attendance(user_id, response)
        update_step(user_id, step=10)
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Напишите слово для проверки", 'random_id':0})
  except: pass


def attendance_3(event, user_id, response):
  try:
    if step_check(user_id) == 10:
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
                  update_step(id_id, step=12)
                  update_attendance_world(id_id, response)
                  vk_session.method('messages.send', {'peer_id': id_id, 'message':"Введите слово!", 'random_id':0})
  except: pass


def attendance_world_check(event, user_id, response):
  try:
    if response == attendance_check_world(user_id):
        if step_check(user_id) == 12:
            update_attendance(user_id, attendance = str(datetime.strftime(datetime.now(), "%H:%M")))
            vk_session.method('messages.send', {'peer_id': user_id, 'message':"Отлично вы отметелись !", 'random_id':0})
        if response != attendance_check_world(user_id): 
            vk_session.method('messages.send', {'peer_id': user_id, 'message':"Не верное слово:(", 'random_id':0})
  except: pass



  