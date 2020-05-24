def recruitment_team(event, user_id, response, bulk):
  if user_id == check_db(user_id):
    if response == "наборвкоманду":   
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Где вы хотите набрать команду ?", 'random_id':0, "keyboard": recruitment_team_keyboard})
      update_step(user_id, step = 50)
    if response == "вгруппе" and step_check(user_id) == 50:
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Хорошо, в таком случае укажите следующие данные: \n\n 1. Номер группы\n2. Сообщение и ссылку на беседу", 'random_id':0, "keyboard": keyboard_profilse})
      update_step(user_id, step = 505)
    if response == "программисты" and step_check(user_id) == 505:
        update_step(user_id, step=501)
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Введите курс", 'random_id':0, "keyboard": keyboard_course})
    if response == "разработчики" and step_check(user_id) == 505:
        update_step(user_id, step=502)
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Введите курс", 'random_id':0, "keyboard": keyboard_course})
    if response == "коммерция" and step_check(user_id) == 505:
        update_step(user_id, step=503)
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Введите курс", 'random_id':0, "keyboard": keyboard_course})
    if response == "безопасники" and step_check(user_id) == 505:
        update_step(user_id, step=504)
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Введите курс", 'random_id':0, "keyboard": keyboard_course})
    if response == "ltспециальности":
      if step_check(user_id) == 501 or step_check(user_id) == 502 or step_check(user_id) == 503 or step_check(user_id) == 504:
        update_step(user_id, step=505)
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"Пожалуйста выберите специальность", 'random_id':0, "keyboard": keyboard_profilse})
    if response == "первыйкурс" and step_check(user_id) == 501:
        course_letter = groups["course_1"] + groups["letter_1"]
        year = groups["year_1"]
    if response == "первыйкурс" and step_check(user_id) == 502:
        course_letter = groups["course_1"] + groups["letter_2"]
        year = groups["year_1"]
    if response == "первыйкурс" and step_check(user_id) == 503:
        course_letter = groups["course_1"] + groups["letter_3"]
        year = groups["year_1"]
    if response == "первыйкурс" and step_check(user_id) == 504:
        course_letter = groups["course_1"] + groups["letter_4"]
        year = groups["year_1"]
    if response == "второйкурс" and step_check(user_id) == 501:
        course_letter = groups["course_2"] + groups["letter_1"]
        year = groups["year_2"]
    if response == "второйкурс" and step_check(user_id) == 502:
        course_letter = groups["course_2"] + groups["letter_2"]
        year = groups["year_2"]
    if response == "второйкурс" and step_check(user_id) == 503:
        course_letter = groups["course_2"] + groups["letter_3"]
        year = groups["year_2"]
    if response == "второйкурс" and step_check(user_id) == 504:
        course_letter = groups["course_2"] + groups["letter_4"]
        year = groups["year_2"]
    if response == "третийкурс" and step_check(user_id) == 501:
        course_letter = groups["course_3"] + groups["letter_1"]
        year = groups["year_3"]
    if response == "третийкурс" and step_check(user_id) == 502:
        course_letter = groups["course_3"] + groups["letter_2"]
        year = groups["year_3"]
    if response == "третийкурс" and step_check(user_id) == 503:
        course_letter = groups["course_3"] + groups["letter_3"]
        year = groups["year_3"]
    if response == "третийкурс" and step_check(user_id) == 504:
        course_letter = groups["course_3"] + groups["letter_4"]
        year = groups["year_3"]
    if response == "четвертыйкурс" and step_check(user_id) == 501:
        course_letter = groups["course_4"] + groups["letter_1"]
        year = groups["year_4"]
    if response == "четвертыйкурс" and step_check(user_id) == 502:
        course_letter = groups["course_4"] + groups["letter_1"]
        year = groups["year_4"]
    if response == "четвертыйкурс" and step_check(user_id) == 503:
        course_letter = groups["course_4"] + groups["letter_1"]
        year = groups["year_4"]
    if response == "четвертыйкурс" and step_check(user_id) == 504:
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
      update_step(user_id, step=51)
      vk_session.method('messages.send', {'peer_id': user_id, 'message':"Какая группа?", 'random_id':0, "keyboard": keyboard})
    except: pass
    if response == "вколледже" and step_check(user_id) == 50:
        vk_session.method('messages.send', {'peer_id': user_id, 'message':"хорошо, в таком случае напишите сообщение которое нужно отправить вместе с ссылкой на беседу", 'random_id':0})
        update_step(user_id, step = 52)
    try: 
      if groupa(response) == "real" and step_check(user_id) == 51:
          update_recruitment_group(user_id, response)
          update_step(user_id, step = 53)
          vk_session.method('messages.send', {'peer_id': user_id, 'message':"Теперь укажите сообщение с ссылкой на беседу", 'random_id':0})
    except: pass
    try:
      if step_check(user_id) == 53 and groupa(response) != "real"  :
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
            vk_session.method('messages.send', {'peer_id': user_id, 'message':"Надеюсь в скором времени к вам подключаться люди!(или нет)", 'random_id':0})
    except: pass
    if response == "да" and step_check(user_id) == 54:
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
    if response == "нет" and step_check(user_id) == 54:
        if rang_check(user_id) >= 0.050:
          message_id = recruitment_check(user_id)
          vk_session.method('messages.send', {'peer_id': message_id, 'message':"Ваш запрос откланен", 'random_id':0})
          nullify_step(user_id, 0)
          update_recruitment(user_id, "")
          nullify_step(message_id, 0)
          update_recruitment(message_id, "")
          update_recruitment_group(message_id, "")
    try: 
      if step_check(user_id) == 52:
        if rang_check(user_id) >= 0.050:
          if response != "вколледже":
            vk_session.method('messages.send', {'peer_id': user_id, 'message':"Отлично, надеюсь скоро к вам кто нибудь подключиться", 'random_id':0})
            id_user = all_user_ids()
            nullify_step(user_id)
            for i in range(len(id_user)):
              id_id = take_int_id(i, id_user)
              if id_id != user_id:
                vk_session.method('messages.send', {'peer_id': id_id, 'message':bulk,'random_id':0})  
      if rang_check(user_id) < 0.050:
        if response != "вколледже":
          update_recruitment(user_id, bulk)
          nullify_step(user_id) 
          for i in range(len(all_user_ids())):
            id_id = take_int_id(i, id_user)
            if group_check(user_id) == group_check(id_id):
              if rang_check(id_id) >= 0.050:
                update_step(id_id, step=55)
                update_recruitment(id_id, str(user_id))
                vk_session.method('messages.send', {'peer_id': id_id, 'message':f"Сообщение на одобрение: {bulk}", 'random_id':0})
                vk_session.method('messages.send', {'peer_id': id_id, 'message':"\n\n Одобрить сообщение ? ", 'random_id':0, "keyboard": keyboard_yes_no})
          vk_session.method('messages.send', {'peer_id': user_id, 'message':"Ваш запрос направлен на одобрение!", 'random_id':0})
    except: pass
    if response == "да" and step_check(user_id) == 55:
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
    if response == "нет" and step_check(user_id) == 55:
        if rang_check(user_id) >= 0.050:
          message_id = recruitment_check(user_id)
          vk_session.method('messages.send', {'peer_id': message_id, 'message':"Ваш запрос отклонен", 'random_id':0})
          nullify_step(user_id, 0)
          update_recruitment(user_id, "")
          nullify_step(message_id, 0)
          update_recruitment(message_id, "")
    