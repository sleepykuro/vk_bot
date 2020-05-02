def bas_for_mass_masseg(iddd):
    
    iddd = str(iddd)
    bas_for_mass_masseg_open = open('bas_for_mass_masseg.txt', encoding='utf_8')
    if iddd + '\n' in bas_for_mass_masseg_open:
        pass
    else:
        bas_for_mass_masseg = open('bas_for_mass_masseg.txt', 'a' , encoding='utf_8')
        bas_for_mass_masseg.write(iddd + '\n')
        bas_for_mass_masseg.close()
    
def groupa(grupa):
    a = ["1ат19","1ат219","1иб119","1иб219","1к119",
    "1к219","1п119","1п219","1п319","1р119","1р219","1са119",
    "1ф119","2ат118","2иб118","2к118","2к218","2п118","2п218","2п318",
    "2р118","2р218","1са118","3ат118","3иб117","3к117","3п117","3р117",
    "3са117","4п117"] 
    if grupa in a: 
        return 'real'

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





