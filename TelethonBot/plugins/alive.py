from .. import BotzHub
from telethon import events, Button

@BotzHub.on(events.NewMessage(incoming=True, pattern="/alive"))
async def alibe(event):
  SMEX_PIC = "https://telegra.ph/file/3979593187378b2b54057.jpg"
  but = [[Button.url("Mʏ ᴍᴀsᴛᴇʀ »»", "t.me/R2K_VENOM")]]
  pm_caption = """
•**I'M ALIVE AND READY TO SMEX**\n\n
•**Mʏ sʏsᴛᴇᴍ ɪs ᴘᴇʀғᴇᴄᴛʟʏ ʀᴜɴɴɪɴɢ**\n\n
• Aʙᴏᴜᴛ ᴍʏ sʏsᴛᴇᴍ ✗\n\n
• 𝙎𝙈𝙀𝙓 𝙓 𝙑𝙀𝙍𝙎𝙄𝙊𝙉: 1.1\n• 𝙏𝙀𝙇𝙀𝙏𝙃𝙊𝙉 𝙑𝙀𝙍𝙎𝙄𝙊𝙉 ☞ {version.__version__}\n
(• 𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔 ☞ [𓆩𝙑𝙀𝙉𝙊𝙈𓆪](t.me/R2K_VENOM)\n\n
    )
• 𝙊𝙒𝙉𝙀𝙍 ☞ [𓆩𝙑𝙀𝙉𝙊𝙈𓆪](t.me/R2K_VENOM)\n

"""
  await BotzHub.send_file(event.chat_id, file=SMEX_PIC, caption=pm_caption, buttons=but, link_preview=False)
