from RiZoeLXSpam import Riz, Riz2, Riz3, Riz4, Riz5, Riz6, Riz7, Riz8, Riz9, Riz10, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from RiZoeLXSpam import CMD_HNDLR as hl
    
HELP_PIC = "https://telegra.ph/file/8e1140c9e3661df624b9a.jpg"

Riz_Help = "__Use The Following Buttons For HELP__"


@Riz.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Riz_Help,
                                  buttons=[
           [
            Button.inline("⍟ SPAM ⍟", data="spam"),
            Button.inline("⍟ RAID ⍟", data="raid"),
           ],
           [
            Button.inline("✰ EXTRA ✰", data="extra"),
           ],
           [    
            Button.url("OFFICIAL GROUP", "https://t.me/luxclub_sergio")
           ],
           ],
           )              

  
  
extra_msg = f"""
**Help Extra Cmds**

**Userbot**: BASIC COMMANDS
command:
・{hl}ping 
・{hl}alive
・{hl}restart
・{hl}addsudo <reply to user> : (This Command Is Only For Owner)

**Echo**: To Activate ECHO On Any USER
command:
・{hl}addecho <reply to user>
・{hl}rmechk <reply to user>

**Leave**: To Leave The GROUP or CHANNEL
command:
・{hl}leave <group/chat id>
・{hl}leave : Type in the Group bot will auto leave that group

**Packspam**: To Spam STICKER From A Pack
・{hl}packspam ( Replying To Any Sticker Of The Pack )

**Credits @RichRealm @LUXCLUB_SERGIO**
"""

                 
raid_msg = f"""
**Help Raid Cmds**


**raid:** Activates RAID On Mentioned User For Given Ranges.
command:
 • {hl}raid <count> <username
 • {hl}raid <count> <reply to user>

**Delayraid**: Activates RAID On Mentioned User With Short Time DELAYs.
Command:
 • {hl}delayraid <delay> <count> <Username Of User>
 • {hl}delayraid <delay> <count> <Reply To The User>

**replyraid:** Activates REPLY RAID On Mentioned User.
command:
 • {hl}replyraid <replying to user>
 • {hl}dreplyraid <username>

**dreplyraid:** Deactivates REPLY RAID.
command:
 • {hl}dreplyraid <replying to user>
 • {hl}dreplyraid <username>


**Credits @RichRealm @LUXCLUB_SERGIO**
"""

spam_msg = f"""
**Help Spam Cmds**

**spam**: Spams a message for given counter(<= 100).
command:
 • {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
 • {hl}spam <count> <replying any message>

**bigspam**: Spams a message for given counter.
command:
 • {hl}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
 • {hl}bigspam <count> <replying any message>

**delayspam**: Delay spam a text for given counter after given time.
command:
 • {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
 • {hl}delayspam <delay> <count> <replying any message>

**pornspam**: Pornography Spam [ DO NOT USE ON YOUR GROUP or CHANNEL ]
command:
 • {hl}pornspam <count>

**hang**: Spams hanging message for given counter.
command:
 • {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)

**Credits @RichRealm @LUXCLUB_SERGIO**
"""                     
           
           
@Riz.on(events.CallbackQuery(pattern=r"help_back"))
@Riz2.on(events.CallbackQuery(pattern=r"help_back"))
@Riz3.on(events.CallbackQuery(pattern=r"help_back"))
@Riz4.on(events.CallbackQuery(pattern=r"help_back"))
@Riz5.on(events.CallbackQuery(pattern=r"help_back"))
@Riz6.on(events.CallbackQuery(pattern=r"help_back"))
@Riz7.on(events.CallbackQuery(pattern=r"help_back"))
@Riz8.on(events.CallbackQuery(pattern=r"help_back"))
@Riz9.on(events.CallbackQuery(pattern=r"help_back"))
@Riz10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            Riz_Help,
            buttons=[
                [
            Button.inline("SPAM", data="spam"),
            Button.inline("RAID", data="raid"),
           ],
           [
            Button.inline("EXTRA COMMANDS", data="extra"),
           ],
           [    
            Button.url("OFFICIAL GROUP", "https://t.me/LUXCLUB_SERGIO")
           ],
           ],
        )           
   else:
        Alert = (
                "O Bete Jake POGO Dekh, Spam Bot Tere Bas Ke Nhi Hai !"
            )
        await event.answer(Alert, cache_time=0, alert=True)
      
           
                      
@Riz.on(events.CallbackQuery(pattern=r"spam"))
@Riz2.on(events.CallbackQuery(pattern=r"spam"))
@Riz3.on(events.CallbackQuery(pattern=r"spam"))
@Riz4.on(events.CallbackQuery(pattern=r"spam"))
@Riz5.on(events.CallbackQuery(pattern=r"spam"))
@Riz6.on(events.CallbackQuery(pattern=r"spam"))
@Riz7.on(events.CallbackQuery(pattern=r"spam"))
@Riz8.on(events.CallbackQuery(pattern=r"spam"))
@Riz9.on(events.CallbackQuery(pattern=r"spam"))
@Riz10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("<< BACK", data="help_back"),
            ],
            ],
            ) 
   else:
        Alert = (
                "O Bete Jake POGO Dekh, Spam Bot Tere Bas Ke Nhi Hai !"
            )
        await event.answer(Alert, cache_time=0, alert=True)
                 
                                                       
@Riz.on(events.CallbackQuery(pattern=r"raid"))
@Riz2.on(events.CallbackQuery(pattern=r"raid"))
@Riz3.on(events.CallbackQuery(pattern=r"raid"))
@Riz4.on(events.CallbackQuery(pattern=r"raid"))
@Riz5.on(events.CallbackQuery(pattern=r"raid"))
@Riz6.on(events.CallbackQuery(pattern=r"raid"))
@Riz7.on(events.CallbackQuery(pattern=r"raid"))
@Riz8.on(events.CallbackQuery(pattern=r"raid"))
@Riz9.on(events.CallbackQuery(pattern=r"raid"))
@Riz10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(
            raid_msg,
            buttons=[
            [
            Button.inline("<< BACK", data="help_back"),
            ],
            ],
            )  
     else:
        Alert = (
                "O Bete Jake POGO Dekh, Spam Bot Tere Bas Ke Nhi Hai !"
            )
        await event.answer(Alert, cache_time=0, alert=True)
       


@Riz.on(events.CallbackQuery(pattern=r"extra"))
@Riz2.on(events.CallbackQuery(pattern=r"extra"))
@Riz3.on(events.CallbackQuery(pattern=r"extra"))
@Riz4.on(events.CallbackQuery(pattern=r"extra"))
@Riz5.on(events.CallbackQuery(pattern=r"extra"))
@Riz6.on(events.CallbackQuery(pattern=r"extra"))
@Riz7.on(events.CallbackQuery(pattern=r"extra"))
@Riz8.on(events.CallbackQuery(pattern=r"extra"))
@Riz9.on(events.CallbackQuery(pattern=r"extra"))
@Riz10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("<< BACK", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "O Bete Jake POGO Dekh, Spam Bot Tere Bas Ke Nhi Hai !"
            )
        await event.answer(Alert, cache_time=0, alert=True)

