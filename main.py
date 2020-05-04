from first_layer import *
database_connection()
while bot_on() != 'off': 
    for event in longpoll.listen():      
        user_id = take_event_user_id(event)
        response = take_user_response(event)
        bulk = take_user_response_not_general_reg(event, response)
        user_message(event,user_id, response)
        if event.from_user and not (event.from_me):
            
            hello(event,user_id, response)

            regestration_info(event,user_id, response) 

            regestration_one(event,user_id, response) 
            
            regestration_two(event,user_id, response)
            
            help_user(event,user_id, response) 
            
            bulk_message(event,user_id, response, bulk)

            bulk_message_check(event,user_id, response)

            group_message(event,user_id, response, bulk)

            group_message_check(event,user_id, response)

            game_1(event,user_id, response)

            game_2(event,user_id, response)
            
            timetable(event,user_id, response)

            attendance_1(event, user_id, response)

            attendance_2(event, user_id, response)

            attendance_3(event, user_id, response)

            attendance_world_check(event, user_id, response)

            regestration_for_teacher(event, user_id, response)

            regestration_for_teacher_step_two(event, user_id, response)

#_________________________________________________________________________________________________________________________

#                                            Административные функции
#_________________________________________________________________________________________________________________________

            rang_update(event, user_id, response)

            rang_update_step_two(event, user_id, response)

            rang_update_step_3(event, user_id, response, bulk)

            
            
            


            