from first_layer import *
database_connection()
while bot_on() != 'off': 
    delete_homework()
    for event in longpoll.listen():      
        user_id = take_event_user_id(event)
        response = take_user_response(event)
        bulk = take_user_response_not_general_reg(event)
        user_message(event,user_id, response)
        if event.from_user and not (event.from_me):
            
            start(event, user_id, response)
            
            hello(event,user_id, response)

            regestration_info(event,user_id, response) 

            regestration(event,user_id, response) 

            regestration_2(event, user_id, response)                                

            regestration_for_kurator(event, user_id, response)

            regestration_for_starosta(event, user_id, response) 
    
            help_user(event,user_id, response) 

            bulk_message(event, user_id, response, bulk)

            start_game(event,user_id, response)

            timetable(event,user_id, response)

            attendance_1(event, user_id, response)

            send_attendance_in_alldaydb(event, user_id, response)

            attendance_1_keyboard_2(event, user_id, response)

            attendance_2(event, user_id, response)

            attendance_3(event, user_id, response)

            attendance_3_world(event, user_id, response)

            attendance_world_check(event, user_id, response)

            regestration_for_teacher(event, user_id, response)

            regestration_for_teacher_step_two(event, user_id, response)

            recruitment_team(event, user_id, response, bulk)

            clean_homework(event, user_id, response)

            homework_send(event, user_id, response)

            homework_send_1(event, user_id, response)

            homework_send_1_2(event, user_id, response)

            homework_send_2(event, user_id, response)

            homework_send_3(event, user_id, response, bulk)

            homework_send_notification(event, user_id, response)

            homework_send_notification_2(event, user_id, response)

            delete_starosta_rang(event, user_id, response)


#_________________________________________________________________________________________________________________________

#                                            Административные функции
#_________________________________________________________________________________________________________________________

            rang_update(event, user_id, response)

            rang_update_step_two(event, user_id, response)

            rang_update_step_3(event, user_id, response, bulk)

            
#________________________________________________________________________________________________________________________

#                                           Функции для абитуриентов
#_________________________________________________________________________________________________________________________

            entrance_enrollee(event, user_id, response)

            specialty_enrollee(event, user_id, response)

            master_enrollee(event, user_id, response)

            dod_enrollee(event, user_id, response)

            


            