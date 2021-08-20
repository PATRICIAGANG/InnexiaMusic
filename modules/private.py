from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey, I'm {bn} 🔥⚡
I Cᴀɴ Pʟᴀʏ Mᴜsɪᴄ Iɴ Yᴏᴜʀ Sᴇxʏ Gʀᴏᴜᴩ Vᴏɪᴄᴇ Cʜᴀᴛ. Dᴇᴠᴇʟᴏᴩᴇᴅ Bʏ [G
TGBᴏᴛXD](https://t.me/TGBotXD).


Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴩ Aɴᴅ Pʟᴀʏ Mᴜsɪᴄ Fʀᴇᴇʟʏ!**



   ==>COMMNADS ARE<==
❍ /play  - play song you requested
❍ /dplay  - play song you requested via deezer
❍ /splay  - play song you requested via jio saavn
❍ /playlist - Show now playing list
❍ /current - Show now playing
❍ /song  - download songs you want quickly
❍ /search  - search videos on youtube with details
❍ /deezer  - download songs you want quickly via deezer
❍ /saavn  - download songs you want quickly via saavn
❍ /video  - download videos you want quickly
=>> *Admins only*
❍ /player - open music player settings panel
❍ /pause - pause song play
❍ /resume - resume song play
❍ /skip - play next song
❍ /end - stop music play
❍ /userbotjoin - invite assistant to your chat
❍ /admincache - Refresh admin list
"""
        ),
     
