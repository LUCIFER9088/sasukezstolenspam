from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/ba87c58f01a6fcb5ef512.jpg"
  

          
rizoel = "☯︎ 𝗟𝗨𝗫𝗖𝗟𝗨𝗕 𝗦𝗣𝗔𝗠𝗠𝗘𝗥 𝗦𝗔𝗦𝗨𝗞𝗘 ☯︎\n\n"

rizoel += f"┏━━━━━━━━━━━━━━━━━━━\n"

rizoel += f"┣⍟ **Python Version** : `3.9.6`\n"

rizoel += f"┣⍟ **Telethon Version** : `{version.__version__}`\n"

rizoel += f"┣⍟ **SASUKE 's Version**  : `{rizoelversion}`\n"

rizoel += f"┗━━━━━━━━━━━━━━━━━━━\n\n"
         
                                    
@Riz.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel,
                                  buttons=[
        [
        Button.url("CREATOR", "https://t.me/RichRealm"),
        Button.url("CHANNEL", "https://t.me/LUXCLUB_SERGIO")
        ],
        [
        Button.url("OFFICIAL GROUP", "https://t.me/LUXCLUB_SERGIO")
        ]
        ]
        )
    
