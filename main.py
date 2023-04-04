from telethon import TelegramClient
import asyncio

# Remember to use your own values from my.telegram.org!
api_id = 8648589
api_hash = '7aa57461d8234044fa62c39d4f315d3b'
client = TelegramClient('anon', api_id, api_hash)

async def main():
    # Getting information about yourself
    me = await client.get_me()
    # rbc = await client.get_entity(1099860397)

    messa = await client.get_messages('https://t.me/market_marketplace', 3) # last 3 messages

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    # print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    username = me.username
    print(username)
    print(me.phone)

    for mess in messa:
        print(mess.message)

    
    # await client.send_message('me', 'Hello, myself!')

    # Does it have a username? Use it!
    # entity = await client.get_entity(username)


    # Do you have a conversation open with them? Get dialogs.
    # await client.get_dialogs()

    # Are they participant of some group? Get them.
    # await client.get_participants('https://t.me/rbc_news')

    # Is the entity the original sender of a forwarded message? Get it.
    # await client.get_messages('https://t.me/rbc_news', 10)

    # # # NOW you can use the ID, anywhere!
    # # await client.send_message(123456, 'Hi!')

    # entity = await client.get_entity('1099860397')
    # print(entity)

with client:
    client.loop.run_until_complete(main())
