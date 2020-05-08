import sqlite3

def create_DB(): 
    conn = sqlite3.connect('.db') 
    cursor = conn.cursor()
    

    cursor.execute(""" CREATE TABLE Groups 
    (user_id text, user_group text, step text, rang text, bulk_message text, attendance text, attendance_world text, recruitment_group text, recruitment text, homework text, chose_homework text )
                """)


    
    conn.commit()
    conn.close()

create_DB()