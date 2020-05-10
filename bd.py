import sqlite3

def create_DB(): 
    conn = sqlite3.connect('alldayattendance.db') 
    cursor = conn.cursor()
    

    cursor.execute(""" CREATE TABLE Groups 
    (user_id text, lessons1 text, lessons2 text, lessons3 text, lessons4 text, lessons5 text)
                """)


    
    conn.commit()
    conn.close()

create_DB()