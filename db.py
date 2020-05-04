import sqlite3

def create_DB(): 
    conn = sqlite3.connect('botdatabase.db') # записываем database
    cursor = conn.cursor()
    

    cursor.execute(""" CREATE TABLE Groups 
    (user_id text, user_group text, step text, rang text, bulk_message text, attendance text, attendance_world text, recruitment_group text, recruitment text )
                """)


    
    conn.commit()
    conn.close()

create_DB()


def rang_check(user_id=0):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    user_rang = cursor.execute(f"""
    SELECT rang 
    FROM Groups
    WHERE user_id = {user_id}
    """)
    
    rang = float(list(user_rang)[0][0])
    
    connect.commit()
    connect.close()
    return rang

def alert_users(user_id=0):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    user_group = cursor.execute(f"""
    SELECT user_group 
    FROM Groups
    WHERE user_id = {user_id}
    """)
    
    user_group = list(user_group)[0][0]

    user_id =  cursor.execute(f"""
    SELECT user_id 
    FROM Groups
    WHERE user_group = '{user_group}'
    """)

    ids = list(user_id)
    

    connect.commit()
    connect.close()
    return ids


def update_DB(id_user_=0, ans_user='', user_group=''):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    cursor.execute(f""" 
    UPDATE Groups 
    SET user_answer = '{ans_user}'
    WHERE user_id = {id_user_};
    """)

    cursor.execute(f""" 
    UPDATE Groups 
    SET user_group = '{user_group}'
    WHERE user_id = {id_user_};
    """)

    connect.commit()
    connect.close()




def rang_update(user_id=0, rang=0):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    cursor.execute(f""" 
    UPDATE Groups 
    SET rang = '{rang}'
    WHERE user_id = {user_id};
    """)

    connect.commit()
    connect.close()



def update_DB_rang(id_user_=0, user_rang=''):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    cursor.execute(f""" 
    UPDATE Groups 
    SET rang = '{user_rang}'
    WHERE user_id = {id_user_};
    """)

    connect.commit()
    connect.close()


def update_DB_group(id_user_=0, user_group=''):
    connect = sqlite3.connect('botdatabase.db')
    cursor = connect.cursor()

    cursor.execute(f""" 
    UPDATE Groups 
    SET user_group = '{user_group}'
    WHERE user_id = {id_user_};
    """)

    connect.commit()
    connect.close()
