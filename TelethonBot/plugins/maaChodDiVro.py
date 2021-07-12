from .. import BotzHub
from telethon import events, Button, client

SMEX_USER = [1809900087]

@BotzHub.on(
    events.NewMessage(pattern="^/add ?(.*)")
)
async def _(event):
  if event.sender_id in SMEX_USER:
    text = event.pattern_match.group(1)
    k = [[Button.text(text)]]
    await BotzHub.send_message(event.chat_id, f"Done added {text}")
    await event.reply("PERU HERE",
                    buttons=[
                        [Button.url("𝙼𝚢 𝙾𝚠𝚗𝚎𝚛", "t.me/R2K_VENOM")]
                    ])
  else:
    await event.reply("**BHAI YAAR THUM GAAND MARAO**")
    
@BotzHub.on(
    events.NewMessage(pattern="^/skem ?(.*)")
)
async def amdddd(event):
  if event.is_private:
    return await event.reply("vro use this cmd in group not in pm")
  else:
      text = event.pattern_match.group(1)
      k = [[Button.text(text)]]
      await BotzHub.send_message(event.chat_id, "**SEMX STARTED**", buttons=k)    
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@BotzHub.on(events.callbackquery.CallbackQuery(data="creator"))
async def creator(event):
    await event.edit("𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴  @R2K_VENOM")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
