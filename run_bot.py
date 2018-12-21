import random

import requests
import vk_api
from config import *


def write_msg(user_id, text):
 vk_bot.method('messages.send', {'user_id': user_id, 'message': text, 'random_id': random.randint(0, 1000)})

vk_bot = vk_api.VkApi(token=TOKEN)
long_poll = vk_bot.method('messages.getLongPollServer', {'need_pts': 1, 'lp_version': 3})
server, key, ts = long_poll['server'], long_poll['key'], long_poll['ts']
print("готов к работе")
def write_msg_attach(user_id, text, att_url):
    vk_bot.method('messages.send',
                  {'user_id': user_id,
                   'attachment': att_url,
                   'message': text,
                   'random_id': random.randint(0,1000)})


class Else(object):
    pass


def last_post(group_id, param, param1, param2):
    pass


while True:
    long_poll = requests.get(
        'https://{server}?act={act}&key={key}&ts={ts}&wait=500'.format(server=server,
                                                                       act='a_check',
                                                                       key=key,
                                                                       ts=ts)).json()
    update = long_poll['updates']
    if update[0][0] == 4:
        print(long_poll)
        # print(update)
        user_id = update[0][3]
        user_name = vk_bot.method('users.get', {'user_ids': user_id})
        if 'картинк' in update[0][6]:
            write_msg_attach(user_id,
                             'вот тебе огненная картинка',
                             'photo-30026037_456275881')
        elif 'мем' in update[0][6]:
            write_msg_attach(user_id,
                             'вот тебе твой мем',)

        else:
         write_msg(user_id, 'привет,' + (user_name[0]['first_name']))  # сообщение пользователю
         write_msg(user_id, 'Есть разные команды')
         write_msg(user_id, 'напиши "мем" и я оправлю тебе крутой мем')
         write_msg(user_id, 'так же есть команда "картинка" если её напишеш то  отправлю тебе картинку' )

         print(str(user_name[0]['first_name']) + '' +
               str(user_name[0]['last_name']) + 'написал(а) боту -' + str(update[0][6]))  # сообщение нам

    # Меняем ts для следущего запроса
    ts = long_poll['ts']
    value = 'переменная для проверки git'
