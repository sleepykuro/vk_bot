import sqlite3

def database(user_id = 0, user_group='', step = 1, rang = '', bulk = '', attendance = "", attendance_world = "", recruitment_group = "", recruitment = "", homework = "", chose_homework = "", group_for_startsta = ""):
    
    data = [user_id, user_group, step, rang, bulk, attendance, attendance_world, recruitment_group, recruitment, homework, chose_homework, group_for_startsta]
    
    conn = sqlite3.connect('botdatabase.db')
    cursor = conn.cursor()
    
    cursor.execute(" INSERT INTO Groups VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ", data)

    conn.commit()
    cursor.close()
    conn.close()

def all_user_ids():
    conn = sqlite3.connect('botdatabase.db')
    cursor = conn.cursor()
    data = (" SELECT user_id FROM Groups")
    id_user = cursor.execute(data)
    id_user = id_user.fetchall()
    
    conn.commit()
    conn.close()
    return id_user    

def group_for_startsta_check(user_id=0):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    group_for_startsta = cursor.execute(f"""
    SELECT group_for_startsta 
    FROM Groups
    WHERE user_id = {user_id}
    """)
    
    group_for_startsta = list(group_for_startsta)[0][0]
    
    connect.commit()
    connect.close()
    return group_for_startsta

def update_group_for_startsta(user_id=0, group_for_startsta = ""):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    cursor.execute(f""" 
    UPDATE Groups 
    SET group_for_startsta = '{group_for_startsta}'
    WHERE user_id = {user_id};
    """)
    connect.commit()
    connect.close()

def homework_check(user_id=0):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    homework = cursor.execute(f"""
    SELECT homework 
    FROM Groups
    WHERE user_id = {user_id}
    """)
    
    homework = list(homework)[0][0]
    
    connect.commit()
    connect.close()
    return homework

def attendance_check_world(user_id=0):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    attendance_world = cursor.execute(f"""
    SELECT attendance_world 
    FROM Groups
    WHERE user_id = {user_id}
    """)
    
    attendance_world = list(attendance_world)[0][0]
    
    connect.commit()
    connect.close()
    return attendance_world

def attendance_check(user_id=0):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    attendance = cursor.execute(f"""
    SELECT attendance 
    FROM Groups
    WHERE user_id = {user_id}
    """)
    
    attendance = list(attendance)[0][0]
    
    connect.commit()
    connect.close()
    return attendance

def recruitment_group_check(user_id=0):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    recruitment_group = cursor.execute(f"""
    SELECT recruitment_group 
    FROM Groups
    WHERE user_id = {user_id}
    """)
    
    recruitment_group = list(recruitment_group)[0][0]
    
    connect.commit()
    connect.close()
    return recruitment_group

def recruitment_check(user_id=0):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    recruitment = cursor.execute(f"""
    SELECT recruitment 
    FROM Groups
    WHERE user_id = {user_id}
    """)
    
    recruitment = list(recruitment)[0][0]
    
    connect.commit()
    connect.close()
    return recruitment

def update_attendance_world(user_id=0, attendance_world = ""):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    cursor.execute(f""" 
    UPDATE Groups 
    SET attendance_world = '{attendance_world}'
    WHERE user_id = {user_id};
    """)
    connect.commit()
    connect.close()

def update_recruitment_group(user_id=0, recruitment_group = ""):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    cursor.execute(f""" 
    UPDATE Groups 
    SET recruitment_group = '{recruitment_group}'
    WHERE user_id = {user_id};
    """)
    connect.commit()
    connect.close()

def update_recruitment(user_id=0, recruitment = ""):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    cursor.execute(f""" 
    UPDATE Groups 
    SET recruitment = '{recruitment}'
    WHERE user_id = {user_id};
    """)
    connect.commit()
    connect.close()


def update_homework(user_id=0,  homework= ""):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    cursor.execute(f""" 
    UPDATE Groups 
    SET homework = '{homework}'
    WHERE user_id = {user_id};
    """)
    connect.commit()
    connect.close()

def day_homework(user_id=0,  homework= "", subject = ""):
    
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    old_homework = cursor.execute(f"""
    SELECT homework 
    FROM Groups
    WHERE user_id = {user_id}
    """)
    
    old_homework = old_homework.fetchall()[0][0]
    new_homework = "\n" + subject + ": " + homework
    homework = old_homework + new_homework

    cursor.execute(f""" 
    UPDATE Groups 
    SET homework = '{homework}'
    WHERE user_id = {user_id};
    """)
    connect.commit()
    connect.close()

def update_attendance(user_id=0, attendance = ""):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    cursor.execute(f""" 
    UPDATE Groups 
    SET attendance = '{attendance}'
    WHERE user_id = {user_id};
    """)
    connect.commit()
    connect.close()

def check_db(user_id=0):
    conn = sqlite3.connect('botdatabase.db')
    cursor = conn.cursor()
    data = (" SELECT user_id FROM Groups")
    id_user = cursor.execute(data)
    id_user = id_user.fetchall()

    for i in range(len(id_user)):
        id_id = id_user[i]
        id_id = id_id[0]
        id_id = int(id_id)
        if id_id == user_id:
            return user_id

    conn.commit()
    cursor.close()
    conn.close()

def step_check(user_id=0):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    step = cursor.execute(f"""
    SELECT step
    FROM Groups
    WHERE user_id = {user_id}
    """)
    
    step = int(list(step)[0][0])
    
    connect.commit()
    connect.close()
    return step

def update_rang(user_id=0, rang = ""):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    cursor.execute(f""" 
    UPDATE Groups 
    SET rang = '{rang}'
    WHERE user_id = {user_id};
    """)
    connect.commit()
    connect.close()

def nullify_step(user_id=0, step = 0):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    cursor.execute(f""" 
    UPDATE Groups 
    SET step = '{step}'
    WHERE user_id = {user_id};
    """)
    connect.commit()
    connect.close()

def rang_check(user_id=0):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    rang = cursor.execute(f"""
    SELECT rang 
    FROM Groups
    WHERE user_id = {user_id}
    """)
    
    rang = float(list(rang)[0][0])
    
    connect.commit()
    connect.close()
    return rang

def update_step(user_id=0, step = 0):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    cursor.execute(f""" 
    UPDATE Groups 
    SET step = '{step}'
    WHERE user_id = {user_id};
    """)
    connect.commit()
    connect.close()

def update_bulk(user_id=0, bulk_message = ""):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    cursor.execute(f""" 
    UPDATE Groups 
    SET bulk_message = '{bulk_message}'
    WHERE user_id = {user_id};
    """)
    connect.commit()
    connect.close()

def group_check(user_id=0):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    user_group = cursor.execute(f"""
    SELECT user_group 
    FROM Groups
    WHERE user_id = {user_id}
    """)
    
    user_group = list(user_group)[0][0]
    
    connect.commit()
    connect.close()
    return user_group

def bulk_check_id(user_id=0):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    bulk_message = cursor.execute(f"""
    SELECT bulk_message 
    FROM Groups
    WHERE user_id = {user_id}
    """)
    
    bulk_message = bulk_message.fetchall()[0][0]
    
    connect.commit()
    connect.close()
    return bulk_message

def bulk_check(user_id=0):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    bulk_message = cursor.execute(f"""
    SELECT bulk_message
    FROM Groups
    WHERE user_id = {user_id}
    """)
    
    bulk_message = list(bulk_message)[0][0]
    
    connect.commit()
    connect.close()
    return bulk_message

def update_group(user_id=0,  user_group= ""):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    cursor.execute(f""" 
    UPDATE Groups 
    SET user_group = '{user_group}'
    WHERE user_id = {user_id};
    """)
    connect.commit()
    connect.close()

def chose_homework_check(user_id=0):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    chose_homework = cursor.execute(f"""
    SELECT chose_homework 
    FROM Groups
    WHERE user_id = {user_id}
    """)
    
    chose_homework = chose_homework.fetchall()[0][0]
    
    connect.commit()
    connect.close()
    return chose_homework

def update_chose_homework(user_id=0,  chose_homework= ""):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    cursor.execute(f""" 
    UPDATE Groups 
    SET chose_homework = '{chose_homework}'
    WHERE user_id = {user_id};
    """)
    connect.commit()
    connect.close()
