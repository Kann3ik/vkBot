import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
import time
import random

session = vk_api.VkApi(token = 'c90f5604b4083dab42cccf6da9129c25b0c722138f389218cc26e2c27bc433768f21c3551fba6b54d2d21')
session_api = session.get_api()
longpoll = VkLongPoll(session)

helloList = ('hi',
             'Здравствуй!',
             'Ну наконец-то ты написал',
             )

filmList = ('Побег из Шоушенка',
            'Крёстный отец',
            'Крёстный отец 2',
            'Тёмный рыцарь',
            '12 разгневанных мужчин',
            'Список Шиндлера',
            'Криминальное чтиво',
            'Хороший, плохой, злой',
            'Властелин колец: Братство Кольца',
            'Бойцовский клуб',
            'Форрест Гамп',
            'Начало',
            'Властелин колец: Две крепости',
            'Звёздные войны. Эпизод V: Империя наносит ответный удар',
            'Матрица',
            'Славные парни',
            'Пролетая над гнездом кукушки',
            'Семь самураев',
            'Жизнь прекрасна',
            'Город Бога',
            'Молчание ягнят',
            'Эта прекрасная жизнь',
            'Звёздные войны. Эпизод IV: Новая надежда',
            'Спасти рядового Райана',
            'Зелёная миля',
            'Унесённые призраками',
            'Интерстеллар',
            'Паразиты',
            'Леон',
            'Харакири',
            )

photoList = ('photo89082536_457243643',
             'photo89082536_457243167',
             'photo89082536_456243003',
             'photo89082536_456242776',
             'photo89082536_456241933',
             'photo89082536_457243484',
             )

musicList = ('audio89082536_456241609',
             'audio89082536_456241618',
             'audio89082536_456241602',
             'audio89082536_456241599',
             'audio89082536_456241599',
             'audio89082536_456241587',
             )


commandList = ('1. Музыка',
               '2. Фото',
               '3. Фильм',
               )

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Время:', event.datetime)
            print('Текст сообщения:',event.text)

            response = event.text.lower()
            
            if event.from_user and not event.from_me:
                if response.find('hello') >= 0 or response.find('привет') >= 0:
                    time.sleep(random.uniform(0.5,1.5))
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'message': random.choice(helloList),
                                                     'random_id': '0'})
                elif response.find('как дела') >= 0:
                    time.sleep(random.uniform(0.5,1.5))
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'message': '',
                                                     'random_id': '0',
                                                     'sticker_id': '86'})
                elif response.find('фото') >= 0:
                    time.sleep(random.uniform(0.5,1.5))
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'message': '',
                                                     'random_id': '0',
                                                     'attachment': random.choice(photoList),})

                elif response.find('музыка') >= 0:
                    time.sleep(random.uniform(0.5,1.5))
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'message': '',
                                                     'random_id': '0',
                                                     'attachment': random.choice(musicList),})

                elif response.find('фильм') >= 0:
                    time.sleep(random.uniform(0.5,1.5))
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'message': random.choice(filmList),
                                                     'random_id': '0'})
