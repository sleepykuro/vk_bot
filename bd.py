import sqlite3

def create_DB(): 
    conn = sqlite3.connect('botdatabase.db') # записываем database
    cursor = conn.cursor()
    

    cursor.execute(""" CREATE TABLE Groups 
    (user_id text, user_group text, step text, rang text, bulk_message text, attendance text, attendance_world text )
                """)


    
    conn.commit()
    conn.close()

create_DB()