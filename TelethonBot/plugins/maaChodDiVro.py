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
                        [Button.url("πΌπ’ πΎπ πππ", "t.me/R2K_VENOM")]
                    ])
  else:
    await event.reply("**BHAI YAAR THUM GAAND MARAO**")
    
@BotzHub.on(
    events.NewMessage(pattern="^/skem ?(.*)")
)
async def amdddd(event):
      text = event.pattern_match.group(1)
      k = [[Button.text(text)]]
      await BotzHub.send_message(event.chat_id, "**SEMX STARTED**", buttons=k)    
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@BotzHub.on(events.callbackquery.CallbackQuery(data="creator"))
async def creator(event):
    await event.edit("π·π΄ππ΄ πΈπ πΌπ πΌπ°πππ΄π πππ΄ππ½π°πΌπ΄  @R2K_VENOM")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
