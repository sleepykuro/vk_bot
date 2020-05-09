def attendance_1(event, user_id, response):
  if response == "посещаемость":
    if rang_check(user_id) >= 1:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="Первый курс", color="primary")],
            [
              get_button(label="Второй курс", color="primary"),
              get_button(label="Третий курс", color="primary")
            ],
            [get_button(label="Четвертый курс", color="primary")
            ]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=30)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Пожалуйста выберите Курс", 'random_id':0, "keyboard": keyboard})
    if rang_check(user_id) >= 0.050 and rang_check(user_id) < 0.070:
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
    if rang_check(user_id) == 0.070:
      group = group_for_startsta_check(user_id)
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
  if response == "первыйкурс":
    if step_check(user_id) == 30:
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
      update_step(user_id, step=31)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Пожалуйста выберите специальность'random_id':0, "keyboard": keyboard})
  if response == "второй курс":
    if step_check(user_id) == 30:
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
      update_step(user_id, step=32)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Пожалуйста выберите специальность", 'random_id':0, "keyboard": keyboard})
  if response == "комерция":
    if step_check(user_id) == 30:
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
      update_step(user_id, step=33)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Пожалуйста выберите специальность", 'random_id':0, "keyboard": keyboard})
  if response == "безопасники":
    if step_check(user_id) == 30:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="Програмисты", color="primary"),
              get_button(label="Разроботчики", color="primary")],
            [get_button(label="Безопасники", color="primary")]
            ]
        }
      keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
      keyboard = str(keyboard.decode('utf-8'))
      update_step(user_id, step=34)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Пожалуйста выберите специальность", 'random_id':0, "keyboard": keyboard}))

def attendance_2(event, user_id, response):
  if response == "ltкурсы":
    if step_check(user_id) == 31 or step_check(user_id) == 32 or step_check(user_id) == 33 or step_check(user_id) == 34:
      keyboard = {
            "one_time": True,
            "buttons": [
            [
            get_button(label="Первый курс", color="primary")],
            [
              get_button(label="Второй курс", color="primary"),
              get_button(label="Третий курс", color="primary")
            ],
            [get_button(label="Четвертый курс", color="primary")
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
  except: pass

def attendance_3_world(event, user_id, response):