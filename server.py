
import time
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
from bs4 import BeautifulSoup
#from pyaxmlparser import APK
from shutil import copyfile
import subprocess
import math
import requests
from requests import exceptions
import sys, os, re, sys, io
import warnings, random
from random import randint
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pyrogram import Client, Filters, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, ForceReply
from contextlib import redirect_stdout
from translation import Translation


active_chats = {}

import os
class Config(object):
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 14000000000
    # chunk size that should be used with requests
    CHUNK_SIZE = 128
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = "https://placehold.it/90x90"
app = Client(
    os.environ.get("TOKEN"),
    api_id=os.environ["APP_ID"],
    api_hash=os.environ["API_HASH"])

from pyrogram.api.errors import (
    BadRequest, Flood, InternalServerError,
    SeeOther, Unauthorized, UnknownError
)
import sys
try:
    from urllib.parse import quote_plus
    import urllib.request
    python3 = True
except ImportError:
    from urllib import quote_plus
    import urllib2
    python3 = False
import traceback
from pyrogram import Client, Filters

import requests
import threading
import io
import urllib
import subprocess

import traceback
def exec_thread(target, *args, **kwargs):
  t = threading.Thread(target=target, args=args, kwargs=kwargs)
  t.daemon = True
  t.start()

from hurry.filesize import size, alternative
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
def prog(client, current, total, message_id, chat_id, required_file_name):
 if round(current/total*100, 0) % 5 == 0:
  try:
   file_size = os.stat(required_file_name).st_size
   client.send_chat_action(chat_id,'UPLOAD_DOCUMENT')
   client.edit_message_text(
    chat_id,
    message_id,
    text = "{}% of {}".format(round(current/total*100, 0), str(pretty_size(file_size)))
   )
  except:
   pass
def progress(client, current, total, message_id, chat_id):
 if round(current/total*100, 0) % 5 == 0:
  try:
   client.edit_message_text(
    chat_id,
    message_id,
    text = "**⬇️ Download Progress:**  `{}%`".format(round(current/total*100, 0))
   )
  except:
   pass
    
def shuffle(word):
    wordlen = len(word)
    word = list(word)
    for i in range(0,wordlen-1):
        pos = randint(i+1,wordlen-1)
        word[i], word[pos] = word[pos], word[i]
    word = "".join(word)
    return word

def pretty_size(sizes):
    units = ['B', 'KB', 'MB', 'GB']
    unit = 0
    while sizes >= 1024:
        sizes /= 1024
        unit += 1
    return '%0.2f %s' % (sizes, units[unit])
def dosomething(buf):
    """Do something with the content of a file"""
    sleep(0.01)
    pass

    
    
        
def get_filename_from_cd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]


def dynamic_data(data):
    return Filters.create(
        name="DynamicData",
        func=lambda filter, callback_query: filter.data == callback_query.data,
        data=data  # "data" kwarg is accessed with "filter.data"
    )
def DownLoadFile(url, file_name):
    if not os.path.exists(file_name):
        r = requests.get(url, allow_redirects=True, stream=True)
        with open(file_name, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=Config.CHUNK_SIZE):
                fd.write(chunk)
    return file_name

fetching_download_link = "🔍 Searching for **{}** in progress."
download_job_started = "\n ⬇️ **Download Server** [{}]({})"
download_successfull = "Download was completed in `{}` seconds\n\nNow Uploading to telegram in progres and that should not take long."
no_result_found = "Oops! There was an error!!!"
def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    #2**10 = 1024
    if not size:
      return ""
    power = 2**10
    n = 0
    Dic_powerN = {0 : ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /=  power
        n += 1
    return str(math.floor(size)) + " " + Dic_powerN[n] + 'B'


import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


## The telegram Specific Functions
def error(bot, update, error):
    # TRChatBase(update.from_user.id, update.text, "error")
    logger.warning('Update "%s" caused error "%s"', update, error)

def messages(bot, update):
        global active_chats

        user_chat = active_chats.get(update.from_user.id, None)
        if user_chat is None:
            bot.send_message(chat_id=update.from_user.id,text="**INVALID ACTION:** 😩 Kindly send /search to initiate your session", parse_mode="Markdown")
            return

        actions = user_chat.get('actions', None)
        if actions is None:
            bot.send_message(chat_id=update.from_user.id, text="**UNKNOWN ACTIVITY:** 👀 I have no clue on what you mean.", parse_mode="Markdown")
            return
        if len(actions) == 0:
            bot.send_message(chat_id=update.from_user.id,
                             text="**ERROR:** 😏 You seem to be a stranger. Use /help to learn more about me", parse_mode="Markdown")
            return
        
        
        recent_action = actions[-1]
        #bot.send_message(chat_id=update.from_user.id, text="DEBUG: last action: {}".format(recent_action))
        if recent_action == 'apks':
            if len(update.text) < 5:
              
                apk_string = "{}".format("apks")
                bot.send_message(
        chat_id=update.from_user.id,
        text="**📱 Apk Downloader**\n\n__Step 2 of 3__\n\n"
                                      "🔎 **Search Query too short!** Please try again.",
        reply_markup=InlineKeyboardMarkup(
        [
          
            [  
                InlineKeyboardButton("⬅️ Go Back", callback_data=apk_string.encode("UTF-8")),
            ]
        ]
    ),
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True)
              
                return
            

            user_chat['search_query'] = ' '.join(map(lambda x: x.capitalize(),
                                                 update.text.split(' ')))
            user_chat['link'] = None
            command_get_specify_apk(bot, update)
        else:
            home_string = "{}".format("start")
            bot.edit_message_text(text="This action is not supported :(",
                         chat_id=update.from_user.id,
                         message_id=update.message_id,
                         reply_markup=InlineKeyboardMarkup(
        [
          
            [  
                InlineKeyboardButton("⬅️ Go Back", callback_data=home_string.encode("UTF-8")),
            ]
        ]
    ))


def start(bot, update):
    global active_chats
    if update.from_user.id not in active_chats:
        active_chats[update.from_user.id] = {'actions': []}
    active_chats[update.from_user.id]['actions'].append('apks')
    audio_string = "{}".format("downl")
    
    services = "{}".format("services")
    
    info_string = "{}".format("help")
    
    join_string = "{}".format("join")
    
  
    sent = bot.send_message(update.chat.id, 
        text=Translation.START_TEXT,
        reply_markup=InlineKeyboardMarkup(
        [
            [  # First row
                # Generates a callback query when pressed
                InlineKeyboardButton("🚸 Join Beta group ", callback_data=join_string.encode("UTF-8")),
                # Opens a web URL
                InlineKeyboardButton("♻️ Services", callback_data=services.encode("UTF-8")),
            ],
            [  
                InlineKeyboardButton("🆘 Help and Usage", callback_data=info_string.encode("UTF-8")),
            ]
        ]
    ),
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True).message_id

    
    
def ft(bot, update):
    global active_chats
    if update.from_user.id not in active_chats:
        active_chats[update.from_user.id] = {'actions': []}
    active_chats[update.from_user.id]['actions'].append('filetransfer')
    audio_string = "{}".format("downl")
    
    services = "{}".format("services")
    
    info_string = "{}".format("help")
    
    join_string = "{}".format("join")
    if update.reply_to_message is not None:
        reply_message = update.reply_to_message
        download_location = Config.DOWNLOAD_LOCATION + "/"
        a = bot.send_message(
            chat_id=update.from_user.id,
            text=Translation.DOWNLOAD_START,
            reply_to_message_id=update.message_id
        )
        
        after_download_file_name = bot.download_media(
            message=reply_message,
            file_name=download_location, progress = progress, progress_args = (a.message_id, update.from_user.id)
        )
        filename_w_ext = os.path.basename(after_download_file_name)
        filename, download_extension = os.path.splitext(filename_w_ext)
        filename = filename.strip('\n').replace(' ','_')
        bot.edit_message_text(
            text=Translation.SAVED_RECVD_DOC_FILE,
            chat_id=update.from_user.id,
            message_id=a.message_id
        )
        url = "https://transfer.sh/{}{}".format(str(filename), str(download_extension))
        max_days = "5"
        command_to_exec = [
            "curl",
            # "-H", 'Max-Downloads: 1',
            "-H", 'Max-Days: 5', # + max_days + '',
            "--upload-file", after_download_file_name,
            url
        ]
        bot.edit_message_text(
            text=Translation.UPLOAD_START,
            chat_id=update.from_user.id,
            message_id=a.message_id
        )
        try:
            logger.info(command_to_exec)
            t_response = subprocess.check_output(command_to_exec, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as exc:
            logger.info("Status : FAIL", exc.returncode, exc.output)
            bot.edit_message_text(
                chat_id=update.from_user.id,
                text=exc.output.decode("UTF-8"),
                message_id=a.message_id
            )
        else:
            t_response_arry = t_response.decode("UTF-8").split("\n")[-1].strip()
            bot.edit_message_text(
                chat_id=update.from_user.id,
                text=Translation.FILETRANSFER_GET_DL_LINK.format(t_response_arry, max_days),
                parse_mode=pyrogram.ParseMode.HTML,
                message_id=a.message_id,
                disable_web_page_preview=True
            )
            try:
                os.remove(after_download_file_name)
            except:
                pass
    else:
        bot.send_message(
            chat_id=update.from_user.id,
            text=Translation.REPLY_TO_DOC_GET_LINK,
            reply_to_message_id=update.message_id
        )
    
def fo(bot, update):
    global active_chats
    if update.from_user.id not in active_chats:
        active_chats[update.from_user.id] = {'actions': []}
    active_chats[update.from_user.id]['actions'].append('fileio')
    audio_string = "{}".format("downl")
    
    services = "{}".format("services")
    
    info_string = "{}".format("help")
    
    join_string = "{}".format("join")
    if update.reply_to_message is not None:
        reply_message = update.reply_to_message
        download_location = Config.DOWNLOAD_LOCATION + "/"
        a = bot.send_message(
            chat_id=update.from_user.id,
            text=Translation.DOWNLOAD_START,
            reply_to_message_id=update.message_id
        )
        
        after_download_file_name = bot.download_media(
            message=reply_message,
            file_name=download_location, progress = progress, progress_args = (a.message_id, update.from_user.id)
        )
        filename_w_ext = os.path.basename(after_download_file_name)
        filename, download_extension = os.path.splitext(filename_w_ext)
        filename = filename.strip('\n').replace(' ','_')
        bot.edit_message_text(
            text=Translation.SAVED_RECVD_DOC_FILE,
            chat_id=update.from_user.id,
            message_id=a.message_id
        )
        expires = "1w"
        
        bot.edit_message_text(
            text=Translation.UPLOAD_START,
            chat_id=update.from_user.id,
            message_id=a.message_id
        )
      
        url = "https://file.io/?expires={expires}"
        fin = open(after_download_file_name, 'rb')
        files = {'file': fin}
        try:
          max_days = "7"
          r = requests.post(url, files=files).json()
          print(r['link'])
          bot.edit_message_text(
                chat_id=update.from_user.id,
                text=Translation.FILEIO_GET_DL_LINK.format(r['link'], max_days),
                parse_mode=pyrogram.ParseMode.HTML,
                message_id=a.message_id,
                disable_web_page_preview=True
            )
        except:
                bot.edit_message_text(
                chat_id=update.from_user.id,
                text="Error uploading file",
                message_id=a.message_id
            )
                os.remove(after_download_file_name)
                pass
        finally:
          os.remove(after_download_file_name)
          fin.close()
    else:
        bot.send_message(
            chat_id=update.from_user.id,
            text=Translation.REPLY_TO_DOC_GET_LINK,
            reply_to_message_id=update.message_id
        )
    

    

   
def help(bot, update):
    global active_chats
    active_chats[update.from_user.id] = {'actions': []}
    
    
    start_string = "{}".format("start")
   
    sent = bot.send_message(update.chat.id, 
        text=Translation.HELP_TEXT,
        reply_markup=InlineKeyboardMarkup(
        [
            [  
                InlineKeyboardButton("🏡  Return Back Home", callback_data=start_string.encode("UTF-8")),
            ]
        ]
    ),
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True).message_id
    
def search(bot, update):
    global active_chats
    if update.from_user.id not in active_chats:
        active_chats[update.from_user.id] = {'actions': []}
    active_chats[update.from_user.id]['actions'].append('apks')
    
    start_string = "{}".format("downl")
   
    sent = bot.send_message(update.chat.id, 
        text="**📱 Apk Downloader Premium**\n\n__Step 1 of  2__\n"
                              "\nOK! Send me search query in next message.",
        reply_markup=InlineKeyboardMarkup(
        [
            [  
                InlineKeyboardButton("⬅️  Retrun to Previous menu", callback_data=start_string.encode("UTF-8")),
            ]
        ]
    ),
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True).message_id    
    
@app.on_callback_query(dynamic_data("start"))
def start_data(bot, update):
    global active_chats
    if update.from_user.id not in active_chats:
        active_chats[update.from_user.id] = {'actions': []}
    active_chats[update.from_user.id]['actions'].append('apks')
    audio_string = "{}".format("downl")
    
    services = "{}".format("services")
    
    info_string = "{}".format("help")
    
    join_string = "{}".format("join")
    
  
    
    bot.edit_message_text(
        chat_id=update.from_user.id,
        text=Translation.START_TEXT,
        reply_markup=InlineKeyboardMarkup(
        [
            [  # First row
                # Generates a callback query when pressed
                InlineKeyboardButton("🚸 Join Beta group ", callback_data=join_string.encode("UTF-8")),
                # Opens a web URL
                InlineKeyboardButton("♻️ Services", callback_data=services.encode("UTF-8")),
            ],
            [  
                InlineKeyboardButton("🆘 Help and Usage", callback_data=info_string.encode("UTF-8")),
            ]
        ]
    ),
        message_id=update.message.message_id,
        disable_web_page_preview=True
    
    )

    
@app.on_callback_query(dynamic_data("join"))
def pyrogram_data(bot, update):
    global active_chats
    active_chats[update.from_user.id] = {'actions': []}
    
    start_string = "{}".format("start")
    bot.edit_message_text(
        text="⚠️ Please Before you join the group bare in mind that its not a group to spam with links and sfw. Hope you understand",
        chat_id=update.from_user.id,
        reply_markup=InlineKeyboardMarkup(
        [
            [  # First row
                # Generates a callback query when pressed
                InlineKeyboardButton("🚹  Join Beta group" , url="https://t.me/joinchat/C74PmEPu2JymxxnUCbPytw"),
                # Opens a web URL
                InlineKeyboardButton("⬅️  Retrun to Main menu" , callback_data=start_string.encode("UTF-8")),
            ],
        
        
        ]
    ),
        message_id=update.message.message_id
    )        

@app.on_callback_query(dynamic_data("services"))
def start_data(bot, update):
    global active_chats
    if update.from_user.id not in active_chats:
        active_chats[update.from_user.id] = {'actions': []}
    active_chats[update.from_user.id]['actions'].append('services')
    
    start_string = "{}".format("start")
    bot.edit_message_text(
        text=Translation.SERVICES,
        chat_id=update.from_user.id,
        parse_mode=pyrogram.ParseMode.HTML,
        
        reply_markup=InlineKeyboardMarkup(
        [
            
            [  
                InlineKeyboardButton("⬅️ " + "Go Back" , callback_data=start_string.encode("UTF-8"))
            ]
        ]
    ),
        message_id=update.message.message_id,
        disable_web_page_preview=True
    )        

@app.on_callback_query(dynamic_data("downl"))
def pyrogram_data(bot, update):
    global active_chats
    active_chats[update.from_user.id] = {'actions': []}
    
    start_string = "{}".format("start")
    apk_string = "{}".format("apks")
    bot.edit_message_text(
        text=Translation.DOWNLOAD_TOOLS_TEXT,
        chat_id=update.from_user.id,
        reply_markup=InlineKeyboardMarkup(
        [
            [  # First row
                # Generates a callback query when pressed
                InlineKeyboardButton("🔎 " + " Search Android Apps " , callback_data=apk_string.encode("UTF-8"))
            ],
            [ 
                InlineKeyboardButton("🚫  Cancel" , callback_data=start_string.encode("UTF-8"))
            ]
        
        
        ]
    ),
        message_id=update.message.message_id
    ) 
@app.on_callback_query(dynamic_data("apks"))
def pyrogram_data(bot, update):
    global active_chats
    if update.from_user.id not in active_chats:
        active_chats[update.from_user.id] = {'actions': []}
    active_chats[update.from_user.id]['actions'].append('apks')
    
    
    start_string = "{}".format("downl")
    bot.edit_message_text(
        text="**📱 Apk Downloader Premium**\n\n__Step 1 of  2__\n"
                              "\nOK! Send me search query in next message.",
        chat_id=update.from_user.id,
        reply_markup=InlineKeyboardMarkup(
        [
            [  
                # Opens a web URL
                InlineKeyboardButton("⬅️  Retrun to Previous menu" , callback_data=start_string.encode("UTF-8")),
            ],
        
        
        ]
    ),
        message_id=update.message.message_id
    )    
def command_get_specify_apk(bot, update):
    if active_chats.get(update.from_user.id).get('link') is None:
      search_query = active_chats.get(update.from_user.id).get('search_query')
    query = " ".join(search_query) 
    sent = bot.send_message(update.from_user.id, 
        text=fetching_download_link.format(query),
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True)
    print('Searching for: {}'.format(query))
    options={}
    base_headers = {
        'User-Agent':  'Mozilla/6.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
    headers = dict(base_headers, **options)
    res = requests.get('https://apkpure.com/search?q={}&region='.format(quote_plus(query)), headers=headers).text
    APPS = []
    soup = BeautifulSoup(res, "html.parser")
    for i in soup.find('div', {'id':'search-res'}).findAll('dl', {'class':'search-dl'}):
        app = i.find('p', {'class':'search-title'}).find('a')
        APPS.append((app.text,
                    i.findAll('p')[1].find('a').text,
                    'https://apkpure.com' + app['href']))
    time.sleep(5)
    if len(APPS) == 0:
      bot.edit_message_text(text="**📱 Apk Downloader Premium**\n\n__Step 2 of  2__\n"
                              "\n\n🔍 Search for **{}** Returned (`0`) results\n\n You may try again by entering an altenative search and i will find it for you".format(search_query),
                         chat_id=update.from_user.id,
                         parse_mode="Markdown",
                         message_id=sent.chat_id,
                         #reply_markup=reply_markup,
                         disable_web_page_preview=True)
      return
      
    
    inline_keyboard = []
    if len(APPS) > 0:
      for idx, app in enumerate(APPS):
        
        start_string = "{}|{}".format(idx, app[0])
        ikeyboard = [
                            InlineKeyboardButton(
                                "[{:02d}]  -  {}".format(idx, app[0]),
                                callback_data=start_string.encode("UTF-8")
                            )
                        ]
        user_chat = active_chats.get(update.from_user.id, None)
        user_chat['Aps'] = APPS
        user_chat['Apps'] = None      
        inline_keyboard.append(ikeyboard)
        num=len(APPS)
        reply_markup = InlineKeyboardMarkup(inline_keyboard)
        bot.edit_message_text(
        text="**📱 Apk Downloader Premium**\n\n__Step 2 of  2__\n"
                              "\n\n🔍 Search for **{}** Returned (`{}`) results\n\n Click on your app and i will download it right away".format(search_query, num),
        chat_id=update.from_user.id,
        
        reply_markup=reply_markup,
        message_id=sent.message_id,
        disable_web_page_preview=True)
        
@app.on_callback_query(dynamic_data("help"))
def pyrogram_data(bot, update):
    global active_chats
    active_chats[update.from_user.id] = {'actions': []}
    
    
    start_string = "{}".format("start")
    bot.edit_message_text(
        text=Translation.HELP_TEXT,
        chat_id=update.from_user.id,
        
        reply_markup=InlineKeyboardMarkup(
        [
            
            [  
                InlineKeyboardButton("⬅️ " + "Go Back" , callback_data=start_string.encode("UTF-8"))
            ]
        ]
    ),
        message_id=update.message.message_id
    )        
    
            
@app.on_callback_query(dynamic_data("getapk"))
def pyrogram_data(bot, update):
    if active_chats.get(update.from_user.id).get('link') is None:
      search_query = active_chats.get(update.from_user.id).get('search_query')
    searchs = " ".join(search_query) 
    sent = bot.send_message(update.from_user.id, fetching_download_link.format(searchs), reply_to_message_id=update.message.message_id).message_id 
    print('Searching for: {}'.format(searchs))
    search(searchs)
    time.sleep(5)
    if len(APPS) == 0:
      bot.edit_message_text(text='Your search returned No results',
                         chat_id=update.message.chat_id,
                         parse_mode="Markdown",
                         message_id=update.message.chat_id,
                         #reply_markup=reply_markup,
                         disable_web_page_preview=True)
      return
    
    bot.delete_messages(update.from_user.id, update.message.message_id)
    inline_keyboard = []
    if len(APPS) > 0:
      for idx, app in enumerate(APPS):
        
        start_string = "{}|{}".format(idx, app[0])
        ikeyboard = [
                            InlineKeyboardButton(
                                "[{:02d}]  -  {}".format(idx, app[0]),
                                callback_data=start_string.encode("UTF-8")
                            )
                        ]
        user_chat = active_chats.get(update.from_user.id, None)
        user_chat['Aps'] = APPS
        user_chat['Apps'] = None        
        inline_keyboard.append(ikeyboard)
        num=len(APPS)
        reply_markup = InlineKeyboardMarkup(inline_keyboard)
        bot.edit_message_text(
        text="🔍 Search for *{}* Returned (`{}`) results\n\n Click on your app and i will download it right away".format(search_query, num),
        chat_id=update.from_user.id,
        
        reply_markup=reply_markup,
        message_id=sent,
        disable_web_page_preview=True
    )        
        
        
        
        
        

        
def button(bot, update):
    if active_chats.get(update.from_user.id).get('Apps') is None:
      APPS = active_chats.get(update.from_user.id).get('Aps')
    chat_id = update.from_user.id
    rnd = "123456789abcdefgh-_"
    servers = shuffle(rnd)  
    if update.data.find("|") == -1:
        return ""
    app_num, app_name = update.data.split("|")
    app_num = int(app_num)
    options={}
    link = APPS[app_num][2]
    first_time = time.time()
    
    try:
        bot.edit_message_text(update.from_user.id, update.message.message_id, download_job_started.format(servers, APPS[app_num][2]))
        time.sleep(5)
        base_headers = {
        'User-Agent':  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
        headers = dict(base_headers, **options)
        res = requests.get(link + '/download?from=details', headers=headers).text
        soup = BeautifulSoup(res, "html.parser").find('a', {'id':'download_link'})
        if soup['href']:
            r = requests.get(soup['href'], stream=True, headers=headers)
            required_file_nam = get_filename_from_cd(r.headers.get('content-disposition'))
            required_file_name = required_file_nam.strip('\n').replace('\"','')
            with open(required_file_name, 'wb') as file:
                for chunk in r.iter_content(chunk_size=8192):
                    total_length = r.headers.get('content-length')
                    dl = 0
                    total_length = int(total_length)
                    if chunk:
                        dl += len(chunk)
                        done = int(100 * dl / total_length)
                        file.write(chunk)
                        file.flush()
                        
        time.sleep(3)
        second_time = time.time()
        t1 = time.time()
        bot.edit_message_text(update.from_user.id, update.message.message_id, download_successfull.format(str(second_time - first_time)[:5]))
        time.sleep(3)
        
        #bot.delete_messages(update.from_user.id, update.message.message_id)
        
        
        t2 = time.time()
        
        description = " " + " \r\n ❤️ @Bfas237Bots "
        sent = bot.send_document(update.from_user.id, required_file_name, progress = prog, progress_args = (update.message.message_id, update.from_user.id, required_file_name), caption='**File Size**: {}\n\n**Completed in**:  `{}` **Seconds**\n'.format(str(pretty_size(total_length)), str(int(t2 - t1))), reply_to_message_id=update.message.message_id)
        
        time.sleep(2)
         
        bot.edit_message_caption(update.from_user.id,sent.message_id, caption='{}'.format(description))
     
        os.remove(required_file_name)
    except (BadRequest, Flood, InternalServerError, SeeOther, Unauthorized, UnknownError) as Err:
        bot.edit_message_text(update.from_user.id, update.message.message_id, Err)
        return None
      
if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    app.add_handler(pyrogram.MessageHandler(start, pyrogram.Filters.command(["start"])))
    app.add_handler(pyrogram.MessageHandler(ft, pyrogram.Filters.command(["ft"])))
    app.add_handler(pyrogram.MessageHandler(fo, pyrogram.Filters.command(["fo"])))
    app.add_handler(pyrogram.MessageHandler(search, pyrogram.Filters.command(["search" , "s"])))
    app.add_handler(pyrogram.MessageHandler(help, pyrogram.Filters.command(["help"])))
    app.add_handler(pyrogram.MessageHandler(messages, pyrogram.Filters.text))
    app.add_handler(pyrogram.CallbackQueryHandler(button))
    app.run()

    
