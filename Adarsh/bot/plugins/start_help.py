#Adarsh goel
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

                      
@StreamBot.on_message(filters.command('start') & filters.private)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        await m.reply_photo(
            photo="https://graph.org/file/d1aa884d79172a1f5587c.jpg",
            caption="**Hello...⚡\n\nI Am A Simple Telegram File/Video To Permanent Download Link And Stream Link Generator Bot.**\n\n**Use /help For More Details\n\nSend Me Any Video/File To See My Power...**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("⚡ UPDATES ⚡", url="https://t.me/Madflix_Bots"), InlineKeyboardButton("⚡ SUPPORT ⚡", url="https://t.me/MadflixBots_Support")],
                    [InlineKeyboardButton("👨‍💻 DEVELOPER 👨‍💻", url="https://t.me/CallAdminRobot")]
                ]
            ),
            
        )
    else:

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.id)

        msg_text = "**Your Link Is Generated...⚡\n\n📧 File Name :-\n{}\n {}\n\n💌 Download Link :- {}\n\n♻️ This Link Is Permanent And Won't Get Expired ♻️\n\n<b>❖ Madflix_Bots</b>**"
        await m.reply_text(            
            text=msg_text.format(file_name, file_size, stream_link),
            
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡ Download Now ⚡", url=stream_link2)]])
        )


@StreamBot.on_message(filters.command('help') & filters.private)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
              
    await message.reply_photo(
            photo="https://graph.org/file/d1aa884d79172a1f5587c.jpg",
            caption="**┣⪼ Send Me Any File/Video Then I Will You Permanent Shareable Link Of It...\n\n┣⪼ This Link Can Be Used To Download Or To Stream Using External Video Players Through My Servers.\n\n┣⪼ For Streaming Just Copy The Link And Paste It In Your Video Player To Start Streaming.\n\n┣⪼ This Bot Is Also Support In Channel. Add Me To Your Channel As Admin To Get Realtime Download Link For Every Files/Videos Post../\n\n┣⪼ For More Information :- /about\n\n\nPlease Share And Support**", 
  
        
        reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("⚡ UPDATES ⚡", url="https://t.me/Madflix_Bots"), InlineKeyboardButton("⚡ SUPPORT ⚡", url="https://t.me/MadflixBots_Support")],
                    [InlineKeyboardButton("👨‍💻 DEVELOPER 👨‍💻", url="https://t.me/CallAdminRobot")]
                ]
            ),
            
        )

@StreamBot.on_message(filters.command('about') & filters.private)
async def about_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    await message.reply_photo(
            photo="https://graph.org/file/d1aa884d79172a1f5587c.jpg",
            caption="""<b>Some Hidden Details 😁</b>

<b>╭━━━━━━━〔File To Link Bot〕</b>
┃
┣⪼<b>Bᴏᴛ Nᴀᴍᴇ</b> : File To Link
┣⪼<b>Updates</b> : <a href='https://t.me/Madflix_Bots'>Bot Updates</a>
┣⪼<b>Support</b> : <a href='https://t.me/MadflixBots_Support'>Bot Support</a>
┣⪼<b>Server</b> : Heroku
┣⪼<b>Library</b> : Pyrogram
┣⪼<b>Language</b> : Python 3
┃
<b>╰━━━━━━━━〔Please Support〕</b>""",
  
        
        reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("⚡ UPDATES ⚡", url="https://t.me/Madflix_Bots"), InlineKeyboardButton("⚡ SUPPORT ⚡", url="https://t.me/MadflixBots_Support")],
                    [InlineKeyboardButton("👨‍💻 DEVELOPER 👨‍💻", url="https://t.me/CallAdminRobot")]
                ]
            ),
            
        )
