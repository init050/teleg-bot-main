

#? You must log in to use any function,
#?  and after logging in, you do not need to log in again. 
#? (the session file will not be deleted).



import asyncio
from http import client
import json
from telethon import TelegramClient



#?########## API_ID & API_HASH ##########
            #! TOKEN >>>
API_ID= 00000   #! >>>>INT.
API_HASH = ''
TOKEN = ''
            #! TOKEN >>>
#?########## API_ID & API_HASH ##########





              

            

async def dialogs():   #! Get dialogs. Run in debugger.


    client=TelegramClient('usetBot', API_ID, API_HASH)
    await client.start()
    dialogs=await client.get_dialogs()
    

    bots = []
    groups = []
    chanels = []
    users = []


    for dialog in dialogs:
        title = dialog.title
        if getattr(dialog.entity, 'bot', None):
            bots.append(title)
        elif dialog.is_group:
            groups.append(title)
        elif dialog.is_channel:
            chanels.append(title)
        else:
            users.append(title)


    print(bots, groups, chanels, users)
    print(dialogs)

    
# asyncio.run(dialogs())   


#! <><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>><><><><><><<><><><><><><><><><><><>><>
#? <><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>><><><><><><<><><><><><><><><><><><>><>


async def send():


    client = TelegramClient("userBot", API_ID, API_HASH)
    await client.start()


    RECIVER = ''   #! >>> Username(contact, chanel, bot, group) (Example:BotFather)
    MESSAGE = ''   #! Message(str)
    LINK = ''         
    FILE = ['', ''] 


    await client.send_message(RECIVER, MESSAGE)
    # await client.send_message(RECIVER, LINK)
    # await client.send_message(RECIVER, LINK, link_preview=False)
    # await client.send_message(RECIVER, file=FILE)
    # await client.send_message(RECIVER, file=FILE, force_document=True)
    # await client.send_message(RECIVER, 'from internet', file=LINK)
    

#asyncio.run(send())   


#! <><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>><><><><><><<><><><><><><><><><><><>><>
#? <><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>><><><><><><<><><><><><><><><><><><>><>


async def get_id():


    client = TelegramClient('userBot', API_ID, API_HASH)
    await client.start()


    USERNAME_FOR_GET_ID = ''
    ID_MESSAGE = 10  #! >>>>INT. Default 10
    LIMIT_FOR_GET_ID = ''


    message= await client.get_messages(USERNAME_FOR_GET_ID, ids=ID_MESSAGE, limit=LIMIT_FOR_GET_ID)
    with open(f'{USERNAME_FOR_GET_ID}.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(message.to_dict(), default = str))
            
        
# asyncio.run(get_id())   
    

#! <><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>><><><><><><<><><><><><><><><><><><>><>
#? <><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>><><><><><><<><><><><><><><><><><><>><>


async def get_message():
    client = TelegramClient('userBot', API_ID, API_HASH)
    await client.start()


    USERNAME = ''
    LIMIT = 10  #! >>>>INT. Default 10


    messages = await client.get_messages(USERNAME, lmit=LIMIT)
    all_message={}


    for message in messages:
        
        message_dict = {
        'views': message.views,
        'sender_id': message.sender_id,
        'forwards': message.forwards,
        'messages': getattr(message, 'message', ''),
    }
        all_message[message.id] = message_dict


    with open(f'{USERNAME}.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(all_message))


    await client.run_until_disconnected()



# asyncio.run(get_message())   


#! <><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>><><><><><><<><><><><><><><><><><><>><>
#? <><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>><><><><><><<><><><><><><><><><><><>><>


async def download_profile_user():
    client = TelegramClient('userBot', API_ID, API_HASH)
    await client.start()


    USERNAME = ''
    await client.download_profile_photo(USERNAME)


    await client.run_until_disconnected()

    
#asyncio.run(download_profile_user())   


#! <><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>><><><><><><<><><><><><><><><><><><>><>
#? <><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>><><><><><><<><><><><><><><><><><><>><>


async def download_profile_grupe():
    client=TelegramClient('userBot', API_ID, API_HASH)
    await client.start()


    USERNAME = ''
    LIMIT = 10  #! >>>>INT. Default 10
    INDEX = 5  #! >>>>INT. Default 5


    users = await client.get_participants(USERNAME, limit=LIMIT, aggressive=True)
    print(users)   #! Run in debugger.
    await client.download_profile_photo(users[INDEX])
    
    
#asyncio.run(download_profile_grupe())  


#! <><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>><><><><><><<><><><><><><><><><><><>><>
#? <><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>><><><><><><<><><><><><><><><><><><>><>


async def download_media():
    client=TelegramClient('userBoot', API_ID, API_HASH)
    await client.start()


    USERNAME = ''
    LIMIT = 10  #! >>>>INT. Default 10 


    message = await client.get_messages(USERNAME, limit=LIMIT)


    for messages in message:
        await client.download_media(messages)

    
#asyncio.run(download_media())   
    

#! <><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>><><><><><><<><><><><><><><><><><><>><>
#? <><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>><><><><><><<><><><><><><><><><><><>><>


async def uplode_media():


    client = TelegramClient('userBot', API_ID, API_HASH)
    await client.start()  


    USERNAME = 'init050'
    ADRESS = r''   #! (Example:( D:\mu\python.mp3 ))


    await client.send_file(USERNAME, ADRESS)  


    await client.run_until_disconnected()


# asyncio.run(uplode_media())   
    

    


