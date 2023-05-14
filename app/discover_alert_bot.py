from telethon import TelegramClient, events
from telethon import connection

from app.db_communicate import switch_air_alert_of

bot_id = 27490482
bot_hash = "baea47d73acbae94860d6251be799b4d"
key_words = ["Відбій", "Повітряна"]

client = TelegramClient(
    'anon', bot_id, bot_hash,
    connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
    proxy=('http://dimanova12.pythonanywhere.com/', 2002, 'secret')
)

# client = TelegramClient("AirListener", bot_id, bot_hash)


@client.on(events.NewMessage(chats=[-1001766138888, 583221084, 1071971976]))
async def air_alert_handler(event):
    for i in range(len(key_words)):
        if key_words[i] in event.message.message:
            region = event.message.message.split()[5]
            print(region)
            if key_words[1] in event.message.message:
                switch_air_alert_of(region_name=region, isAlert=True)
            else:
                switch_air_alert_of(region_name=region, isAlert=False)
            print(event.message.message)


# 🟢 11:08 Відбій тривоги в Дніпропетровська область.
# Слідкуйте за подальшими повідомленнями.
# #Дніпропетровська_область

client.start()
client.run_until_disconnected()
