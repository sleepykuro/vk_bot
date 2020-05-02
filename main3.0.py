keyboard = {
                "one_time": False,
                "buttons": [
                    [{
                            "action": {
                                "type": "text",
                                "payload": "{\"button\": \"1\"}",
                                "label": "Negative"
                            },
                            "color": "negative"
                        },
                        {
                            "action": {
                                "type": "text",
                                "payload": "{\"button\": \"2\"}",
                                "label": "Positive"
                            },
                            "color": "positive"
                        },
                        {
                            "action": {
                                "type": "text",
                                "payload": "{\"button\": \"2\"}",
                                "label": "Primary"
                            },
                            "color": "primary"
                        },
                        {
                            "action": {
                                "type": "text",
                                "payload": "{\"button\": \"2\"}",
                                "label": "Secondary"
                            },
                            "color": "secondary"
                        }
                    ]
                ]
            }
            
            keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))
            
            
            while True:
                for event in longpoll.listen():
                    if event.type == VkBotEventType.MESSAGE_NEW:
                        if event.object.text.lower() == "новые кнопки":
                            vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Новые кнопки", "random_id": 0,
                                                        "keyboard": keyboard})
                        if "Negative" in event.object.text:
                            vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Красная кнопка", "random_id": 0
                                                        })
                        if "Positive" in event.object.text:
                            vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Зелёная кнопка", "random_id": 0
                                                        })
                        if "Primary" in event.object.text:
                            vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Синяя кнопка", "random_id": 0
                                                        })
                        if "Secondary" in event.object.text:
                            vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Обычная кнопка", "random_id": 0
                                                        })
