
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
from utils.typing import *
from utils.handlers import *
from utils.dbmanager import loadDB
import logging
 # Enable logging
 

APP_FOLDER = os.path.dirname(os.path.realpath(__file__))

#Iprint(f)     
logger = logging.getLogger(__name__) 
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from pyrogram import Client, Filters
import os
plugins = dict(
    root="plugins"
) 
def exception_hook(exc_type, exc_value, exc_traceback):
    logging.error(
        "Uncaught exception",
        exc_info=(exc_type, exc_value, exc_traceback)
    )  

sys.excepthook = exception_hook
logger = logging.getLogger(__name__)  
APP_FOLDER = os.path.dirname(os.path.realpath(__file__))
app = Client("mybot", bot_token=os.environ.get("TOKEN"), api_id=os.environ.get("api_id"), api_hash=os.environ.get("api_hash"))
#Iprint(f)     
sadmin = "off"
madmin = "off"
sudoers = [197005208, 409257769, 440287996]
help_text = "📥 <b> Welcome to Apkfetcher Download Portal </b>\n\n " \
            "This bot keeps a database of a large collection of android " \
            "apps and games, obb, modded apps, cracked apps and games.\n\n" \
            "To search for something specific use the method below.\n\n" \
            "<b>Search Tips:</b>\n\n" \
            "Simple Search! -  <code> /search </code> OR <code> /s </code>\n\n" \
             "Advanced Search! - <code> /find 'hint' </code> OR <code> /find 'hint' 'source'  </code>  \n\n" \
            "Example 1: <code> /find whatsapp</code>\n" \
            "Example 2: <code> /find facebook lite apkpure</code>\n" \
            "Example 3: <code> /find netflix apptoide</code>\n" \
            "Example 4: <code> /find telegram x apkpure.com</code>\n" \
            "Example 5: <code> /find telegram apptoide.com</code>" \
            "\n\n" \
            "<b>Basic commands:</b>\n" \
            "/Search - Search for apps and games\n" \
            "/find - Advanced search with params and regex support\n" \
            "/help - Get this message\n" \
            "/feedback - Send your feedback\n" \
            "/about - Display Bots basic info\n" \
            "/cancel - Cancel current operation\n\n" \
            "💌 Contributions via @Bfas237botdevs" 


admin_help_text = "\n\n" \
                  "<b>Admin commands:</b>\n" \
                  "/track - Track an app and view stats\n" \
                  "/edit - Edit an existing app or game\n" \
                  "/delete - Delete an app or game from db\n" \

super_admin_help_text = "\n\n" \
                        "<b>Super Admin commands:</b>\n" \
                        "/add_admin - Register a new admin\n" \
                        "/remove_admin - Remove an admin\n" \
                        "/Upgrade - Upgrade bot\n" \
                        "/restart - Restart Bot\n" \
                        "/download_database - Download complete database"

ADMINS = {}
APK = {}

TMP_FOLDER = os.path.join(APP_FOLDER, 'tmp/')
 
BANNED = ()
ADMINS = open(os.path.join(APP_FOLDER, 'admins.secret'), 'r') 
SUPER_ADMINS = open(os.path.join(APP_FOLDER, 'super_admins.secret'), 'r')
active_chats = {
}
downloads = {} 
tmp = {
}
dic = {} 

l_in = list(ADMINS)
l_out = [e for e in l_in if e.isalnum()] 
l_out = [string for string in l_out]
it = " "
for item in l_in:   
  it += item.rstrip()
words = it.split()

l_ins = list(SUPER_ADMINS)
l_outs = [es for es in l_ins if es.isalnum()] 
l_outs = [strings for strings in l_outs]
its = " "
for items in l_ins:   
  its += items.rstrip()
wordss = its.split()

def is_admin(user_id):  
    if str(user_id) in words:   
        dic['user'] = True
        return True
    else: 
        dic['user'] = False
        return False
 
    return dic


def is_super_admin(user_id):  
    if str(user_id) in wordss:   
        dic['user'] = True
        return True
    else: 
        dic['user'] = False
        return False
 
    return dic


def command_chats(bot, update):
        update.reply("Chats: {}".format(json.dumps(active_chats)))


blocker = SpamFilter()




fetching_download_link = "🔍 Searching for **{}** in progress."
download_job_started = "⬇️ **Downloading from the best location on:**\n\n [{}]({})"
download_successfull = "Download was completed in `{}` seconds\n\nNow Uploading to telegram in progres and that should not take long."
no_result_found = "Oops! There was an error!!!"




def error_handler(bot, update, e): 
        try:
            raise e
            logger.warning('Update "%s" caused error "%s"', update, e)
            bot.send_message("bfaschat", "**DETAILED ERROR:** \n\nUpdate {} caused error {}".format(update, e), parse_mode="Markdown")
        except UnknownError:
            pass
        # remove update.message.chat_id from conversation list
        except BadRequest:
            pass
        # handle malformed requests - read more below!
        except FloodWait:
            pass
        # handle slow connection problems
        except Unauthorized:
            pass
        # handle other connection problems
        except SeeOther:
            pass
        # the chat_id of a group has changed, use e.new_chat_id instead
        except InternalServerError:
            pass
        # the chat_id of a group has changed, use e.new_chat_id instead
        except FileIdInvalid:
            pass
        # the chat_id of a group has changed, use e.new_chat_id instead
        except UserIsBlocked:
            pass
        # the chat_id of a group has changed, use e.new_chat_id instead
        except Flood:
            pass
        # the chat_id of a group has changed, use e.new_chat_id instead
        except MessageNotModified:
            pass
    # TRChatBase(update.from_user.id, update.text, "error")
#DownL("https://www.rspcansw.org.au/wp-content/themes/noPhotoFound.png")
def compDom(URL1,URL2):
  URL1Split = URL1.split(".")
  URL2Split = URL2.split(".")
  a = URL1Split[::-1]
  b = URL2Split[::-1]
  domain1 = a[1] + "." + a[0]
  domain2 = b[1] + "." + b[0]
  if domain1 == domain2:
      return 1
  else:
      return 0
#print(compDom("https://www.rspcansw.org.au", "rspcansw.org.au"))   
@blocker.wrapper
def button_query_handler(bot, query):
        global active_chats
        update = query
        user_chat = active_chats.get(query.message.chat.id, None)
        if user_chat is None:
            bot.send_message(query.message.chat.id, "**SESSION EXPIRED:** 😩 Kindly send /search to initiate your session", parse_mode="Markdown")
            return
        elif query.data:
            try:
              if active_chats.get(query.message.chat.id).get('Apps') is None:
                  ss = active_chats.get(query.message.chat.id).get('ss')
                  APPS = active_chats.get(query.message.chat.id).get('Aps')
              if query.data.find(b"|") == -1:
                return ""
              app_num, app_name = query.data.split(b"|")
              app_num = int(app_num)
              title = APPS[app_num][0]
              link = APPS[app_num][2]
            
              dev = APPS[app_num][3]
              if (ss == 1):
                thumb = Imgsrc(basename(link))
              elif (ss == 2):
                thumb = APPS[app_num][1]
              thmb = DownL(thumb)
       
              if thmb:
                thumb = thmb
              else:
                thumb = "noPhotoFound.png"
              lr = checkUserLastNews(query.message.chat.id)
              tr = apkID()
              tnews = 0
              rd = 0
              size = 0  
            
              if(tr == 0):
                tnews = 0
              elif(lr < tr):
                lr = tr
              if(tr != 0):
                dom = urlparse(link).hostname.split('.')[1]
                doms = urlparse(link).hostname.split('.')[1]
                
                tnews, size = afileid(link) 
              apk = ""
        
              des = "ℹ️ **File name:** {}\n\n👨‍💻 **Developer**: {}"
              description = "ℹ️ **File name:** {}\n\n👨‍💻 **Developer**: {}\n\n © Made with ❤️ by @Bfas237Bots "
             
              if (ss == 1):
              
                if(tnews != 0):
                  query.answer('Sending your app...')
                  logger.debug(tnews)
                  bot.send_document(query.message.chat.id, tnews, caption=description.format(title, size))
                else:
                  apk = bot.send_photo(query.message.chat.id, thumb, caption=des.format(title, dev), parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(
        [
          
            [  
                InlineKeyboardButton("📥 Download Now", callback_data=b"apkpure_dl"),
            ]
        ]
    ))
                user_chat['url'] = link
                user_chat['thumb'] = thumb
                user_chat['title'] = title
                user_chat['dev'] = dev
                user_chat['apk'] = apk
                user_chat['size'] = 0
            
            
              elif (ss == 2): 
                if(tnews != 0):
                  query.answer('Sending your app...')
                  logger.debug(tnews)
                  bot.send_document(query.message.chat.id, tnews, caption=description.format(title, size))
                else:
                  apk = bot.send_photo(query.message.chat.id, thumb, caption=des.format(title, dev), parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(
        [
          
            [  
                InlineKeyboardButton("📥 Download Now", callback_data=b"apptoide_dl"),
            ]
        ]
    ))
                user_chat['url'] = link
                user_chat['thumb'] = thumb
                user_chat['title'] = title
                user_chat['dev'] = dev
                user_chat['apk'] = apk
                user_chat['size'] = 0
                
            except FileIdInvalid as e: 
                bot.send_message(query.message.chat.id, "**Button callback error by**: {}\n\n**Details:**\n\n".format(query.message.chat.id, e), parse_mode="Markdown")
                
            except Exception as e: 
                bot.send_message(query.message.chat.id, "**INVALID SESSION:** This session has ended. try again by searching", parse_mode="Markdown")
                bot.send_message("bfaschat", "**Button callback error**", parse_mode="Markdown")
                error_handler(bot, update, e)  
                pass
              
            
            
            
            
@blocker.wrapper
def messages(bot, update):
        global active_chats
        
        chat_id = update.from_user.id
        bot.send_chat_action(chat_id,'TYPING')

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
        if active_chats.get(update.from_user.id).get('msg') is None:
            src = active_chats.get(update.from_user.id).get('msgid')
        
        
        recent_action = actions[-1]
        #bot.send_message(chat_id=update.from_user.id, text="DEBUG: last action: {}".format(recent_action))
        if recent_action == 'apks':
            if len(update.text) < 5:
              
                apk_string = "{}".format("apks")
                src.edit("**📱 Apk Downloader**\n\n__Step 1 of 2__\n\n"
                                      "⚠️ **Search Query too short!** Please try again.",
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
            choose_source(bot, update)
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
@app.on_message(Filters.command("start"))  
@blocker.wrapper
def start(bot, update, *args, **kwargs):
    global active_chats
    if update.from_user.id not in active_chats:
        active_chats[update.from_user.id] = {'actions': []}
    active_chats[update.from_user.id]['actions'].append('apks')
    audio_string = "{}".format("downl")
    
    services = "{}".format("services")
    
    info_string = "{}".format("help")
    
    join_string = "{}".format("join")
    
  
    sent = bot.send_message(update.from_user.id, 
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
                InlineKeyboardButton("🆘 Help and Usage", callback_data=info_string.encode("UTF-8")),InlineKeyboardButton(  # Opens the inline interface in the current chat
                        "Inline here",
                        switch_inline_query_current_chat="pyrogram"
                    )
            ]
        ]
    ),
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True)

    

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
        logger.warning('Downloading with filetransfer')
        reply_message = update.reply_to_message
        download_location = Config.DOWNLOAD_LOCATION + "/"
        a = bot.send_message(
            chat_id=update.from_user.id,
            text=Translation.DOWNLOAD_START,
            reply_to_message_id=update.message_id
        )
        
        after_download_file_name = bot.download_media(
            message=reply_message,
            file_name=download_location, progress = progs, progress_args = (a.message_id, update.from_user.id)
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
                parse_mode="HTML",
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
            file_name=download_location, progress = progs, progress_args = (a.message_id, update.from_user.id)
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
                parse_mode="HTML",
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
    

    

@app.on_message(Filters.command("help"))  
@blocker.wrapper   
def help(bot, update):
    global active_chats
    active_chats[update.from_user.id] = {'actions': []}
    chat_id = update.from_user.id
    bot.send_chat_action(chat_id,'TYPING')
    
    start_string = "{}".format("start")
   
    from_user = update.from_user
    chat_id = update.chat.id

    admin = is_admin(from_user.id)
    sadmin = is_super_admin(from_user.id)
    logger.warning("checking privilledge %s and %s", admin, sadmin)
    text = help_text

    sent = bot.send_message(update.from_user.id, 
        text=text,
        
        reply_markup=InlineKeyboardMarkup(
        [
            [  
                InlineKeyboardButton("⬅️ " + "Go Back" , callback_data=start_string.encode("UTF-8"))
            ]
        ]
    ), parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True).message_id
    
    
    
    
    
    
    
    #####################
          # SEARCH
    ################"###
    

    
    
@app.on_callback_query(dynamic_data(b"ddd"))
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
@app.on_callback_query(dynamic_data(b"yy"))
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
    
@app.on_callback_query(dynamic_data(b"downl"))
def pyrogram_data(bot, update):
    global active_chats
    if update.from_user.id not in active_chats:
        active_chats[update.from_user.id] = {'actions': []}
    active_chats[update.from_user.id]['actions'].append('apks')
    
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
    
@app.on_message(Filters.command(["search" , "s" , "find"]))    
def search(bot, update):
    global active_chats
    if update.from_user.id not in active_chats:
        active_chats[update.from_user.id] = {'actions': []}
    active_chats[update.from_user.id]['actions'].append('apks')
    chat_id = update.from_user.id
    bot.send_chat_action(chat_id,'TYPING')
    start_string = "{}".format("downl")
   
    src = update.reply("**📱 Apk Downloader Premium**\n\n__Step 1 of  2__\n"
                              "\nOK! Send me search query in next message.",
        reply_markup=InlineKeyboardMarkup(
        [
            [  
                InlineKeyboardButton("⬅️  Retrun to Previous menu", callback_data=start_string.encode("UTF-8")),
            ]
        ]
    ),
        quote=True, disable_web_page_preview=True)
    user_chat = active_chats.get(update.from_user.id, None)
    user_chat['msg'] = None
    user_chat['msgid'] = src 
    
@app.on_callback_query(dynamic_data(b"start"))
def start_data(bot, update):
    global active_chats
    if update.from_user.id not in active_chats:
        active_chats[update.from_user.id] = {'actions': []}
    active_chats[update.from_user.id]['actions'].append('apks')
    audio_string = "{}".format("downl")
    chat_id = update.from_user.id
    bot.send_chat_action(chat_id,'TYPING')
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

    
@app.on_callback_query(dynamic_data(b"join"))
def pyrogram_data(bot, update):
    global active_chats
    active_chats[update.from_user.id] = {'actions': []}
    chat_id = update.from_user.id
    bot.send_chat_action(chat_id,'TYPING')
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

@app.on_callback_query(dynamic_data(b"services"))
def start_data(bot, update):
    global active_chats
    if update.from_user.id not in active_chats:
        active_chats[update.from_user.id] = {'actions': []}
    active_chats[update.from_user.id]['actions'].append('services')
    chat_id = update.from_user.id
    bot.send_chat_action(chat_id,'TYPING')
    start_string = "{}".format("start")
    bot.edit_message_text(
        text=Translation.SERVICES,
        chat_id=update.from_user.id,
        parse_mode="HTML",
        
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

def choose_source(bot, update):
    if active_chats.get(update.from_user.id).get('link') is None:
        search_query = active_chats.get(update.from_user.id).get('search_query')
    query = " ".join(search_query) 
    if active_chats.get(update.from_user.id).get('msg') is None:
      src = active_chats.get(update.from_user.id).get('msgid')
    start_string = "{}".format("apkpure")
    apk_string = "{}".format("apptoide")
    home_string = "{}".format("start")
    src.edit("Choose a source to search from below",
        reply_markup=InlineKeyboardMarkup(
        [ 
            [  # First row
                # Generates a callback query when pressed
                InlineKeyboardButton("🔎 " + " Search ApkPure 🔋" , callback_data=start_string.encode("UTF-8")), InlineKeyboardButton("🔎 " + " Search Apptoide 🛡" , callback_data=apk_string.encode("UTF-8"))
            ], [  
                InlineKeyboardButton("💣 " + "Kill Activity" , callback_data=home_string.encode("UTF-8"))
            ]
        
        
        ] 
    )
    )
    user_chat = active_chats.get(update.from_user.id, None)
    user_chat['msg'] = None
    user_chat['msgid'] = src 
    
    
@app.on_callback_query(dynamic_data(b"apkpure"))
@blocker.wrapper
def apkpure(bot, update):
    try:
        if active_chats.get(update.from_user.id).get('link') is None:
          search_query = active_chats.get(update.from_user.id).get('search_query')
        if active_chats.get(update.from_user.id).get('msg') is None:
          src = active_chats.get(update.from_user.id).get('msgid')
    except Exception as e:
          bot.send_message(update.from_user.id, "**INVALID SESSION:** This session has ended. try again by searching", parse_mode="Markdown")
          bot.send_document(-1001145151462, str(e), caption="**apkpure search_query error**", parse_mode="Markdown")
          error_handler(bot, update, e)
          os.remove('/tmp/foobar.log')
          pass  
    try:
        query = " ".join(search_query)
        sent = src.edit(fetching_download_link.format(query))
        logger.info('Searching for: {}'.format(query))
        options={}
        base_headers = {
        'User-Agent':  'Mozilla/6.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
        headers = dict(base_headers, **options)
        res = requests.get('https://apkpure.com/search?q={}&region='.format(quote_plus(query)), headers=headers).text
        APPS = []
        imgg = []
        soup = BeautifulSoup(res, "html.parser")
        for i in soup.find('div', {'id':'search-res'}).findAll('dl', {'class':'search-dl'}):
            img = i.find('dt').find('img')['src']
            app = i.find('p', {'class':'search-title'}).find('a')
            dev = i.findAll('p')[1].find('a').text
            name = app.text
            links = 'https://apkpure.com' + app['href']
            APPS.append((name, img, links, dev, "apkpure"))
    
    
        inline_keyboard = []
        time.sleep(1)
        if len(APPS) > 0:
            sent.delete()
            items = ""
            for idx, app in enumerate(APPS):
                start_string = "{}|{}".format(idx, app[0])
                ikeyboard = [
                            InlineKeyboardButton(
                                "[{:02d}]  -  {}".format(idx, app[0]),
                                callback_data=start_string.encode("UTF-8")
                            )
                        ]
                inline_keyboard.append(ikeyboard)
                
                num=len(APPS)
                reply_markup = InlineKeyboardMarkup(inline_keyboard)
            
              
            send = bot.send_message(update.from_user.id, "📱 <b>Apk Downloader Premium</b> <i>Step 2 of  2 </i>\n\n Your search returned <b>{}</b> Results \n\n".format(num), reply_markup=reply_markup, parse_mode="html", disable_web_page_preview=True)
           
            user_chat = active_chats.get(update.from_user.id, None)
            user_chat['Aps'] = APPS
            user_chat['Apps'] = None
            user_chat['Send'] = send
            user_chat['ss'] = 1
            user_chat['chatids'] = inline_keyboard
        else:
            sent.edit("**📱 Apk Downloader Premium**\n\n__Step 1 of  2__\n"
                              "\n\n❗️ Search Not Found.. Try again")
            return

    except Error as e:
        bot.send_message(-1001145151462, "**Apkpure Search error by**: {}\n\n**Details:**\n\n".format(update.from_user.id, e))
    except Exception as e: 
          
      bot.send_document(-1001145151462, str(e), caption="**Apkpure search error**", parse_mode="Markdown")
      error_handler(bot, update, e)
      os.remove('/tmp/foobar.log')
      pass

    
    
    
    
@app.on_callback_query(dynamic_data(b"apptoide"))
@blocker.wrapper
def apkpure(bot, update):
    try:
        if active_chats.get(update.from_user.id).get('link') is None:
          search_query = active_chats.get(update.from_user.id).get('search_query')
        if active_chats.get(update.from_user.id).get('msg') is None:
          src = active_chats.get(update.from_user.id).get('msgid')
    except Exception as e:
          bot.send_message(update.from_user.id, "**INVALID SESSION:** This session has ended. try again by searching", parse_mode="Markdown")
          bot.send_document(-1001145151462, str(e), caption="**Apptoide search_query error**", parse_mode="Markdown")
          error_handler(bot, update, e)
          os.remove('/tmp/foobar.log')
          pass  
      
    
    try:
        query = " ".join(search_query)
        sent = src.edit(fetching_download_link.format(query))
        logger.info('Searching for: {}'.format(query))
        options={}
        base_headers = {
        'User-Agent':  'Mozilla/6.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
        headers = dict(base_headers, **options)
        
       
        APPS = Search(search_query)
    
        inline_keyboard = []
    
        time.sleep(1)
        if len(APPS) > 0:
            sent.delete()
            items = ""
            for idx, app in enumerate(APPS):
                start_string = "{}|{}".format(idx, app[0])
                ikeyboard = [
                            InlineKeyboardButton(
                                "[{:02d}]  -  {}".format(idx, app[0]),
                                callback_data=start_string.encode("UTF-8")
                            )
                        ]
                inline_keyboard.append(ikeyboard)
                
                num=len(APPS)
                reply_markup = InlineKeyboardMarkup(inline_keyboard)
            
              
            send = bot.send_message(update.from_user.id, "📱 <b>Apk Downloader Premium</b> <i>Step 2 of  2 </i>\n\n Your search returned <b>{}</b> Results \n\n".format(num), reply_markup=reply_markup, parse_mode="html", disable_web_page_preview=True)
            
            user_chat = active_chats.get(update.from_user.id, None)
            user_chat['Aps'] = APPS
            user_chat['Apps'] = None
            user_chat['Send'] = send
            user_chat['ss'] = 2
            user_chat['chatids'] = inline_keyboard
        else:
            sent.edit("**📱 Apk Downloader Premium**\n\n__Step 1 of  2__\n"
                              "\n\n❗️ Search Not Found.. Try again")
            return

    except Error as e:
        bot.send_message(-1001145151462, "**Apptoide Search error by**: {}\n\n**Details:**\n\n".format(update.from_user.id, e))
    except Exception as e: 
          
      bot.send_document(-1001145151462, str(e), caption="**Apptoide search error**", parse_mode="Markdown")
      error_handler(bot, update, e)
      os.remove('/tmp/foobar.log')
          
      pass


def Search(query): 
    session = requests.Session()
    base_headers = {
        'User-Agent':  'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, sdch, ',
        'Accept-Language': 'zh-CN,zh,en-US,en,fr,fr-FR;q=0.8,ta;q=0.6',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive' 
    }
    response = session.get('https://ws75.aptoide.com/api/7/apps/search?query={}'.format(quote_plus(query)), headers=base_headers, params={
        'limit': 14  
    })
    APP=[]
    html = response.json()
    hi = html["datalist"]['list']
     
    g = [] 
    for i in hi:  
      name = i['name']
      icon = i['icon']
      id = i['id']
      
      link = "http://ws2.aptoide.com/api/7/app/get/app_id={}"
      res = session.get(link.format(id), headers=base_headers)   
      jsondata = res.json()
      dev = jsondata["nodes"]["meta"]["data"]["developer"]["name"]
      link = jsondata["nodes"]["meta"]["data"]["file"]["path"]
      g.append((name, icon, link, dev, "apptoide"))    
    
    
    return g   
  
  
  
  
  
  
def Imgsrc(query): 
    session = requests.Session()
    base_headers = {
        'User-Agent':  'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, sdch, ',
        'Accept-Language': 'zh-CN,zh,en-US,en,fr,fr-FR;q=0.8,ta;q=0.6',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive' 
    }
    response = session.get('https://ws75.aptoide.com/api/7/apps/search?query={}'.format(quote_plus(query)), headers=base_headers, params={
        'limit': 3  
    })
    html = response.json()
    hi = html["datalist"]['list']
     
    j = [] 
    for i in hi:  
      icon = i['icon']
       
    return icon              
     
#print(Imgsrc("com.facebook.lite")) 
@app.on_callback_query(dynamic_data(b"help"))
def pyrogram_data(bot, update):
    global active_chats
    active_chats[update.from_user.id] = {'actions': []}
    
    chat_id = update.from_user.id
    bot.send_chat_action(chat_id,'TYPING')
    from_user = update.from_user
    chat_id = update.message.chat.id
    admin = is_admin(from_user.id)
    sadmin = is_super_admin(from_user.id)
    logger.warning("checking privilledge %s and %s", admin, sadmin)
    text = help_text

    start_string = "{}".format("start")
    bot.edit_message_text(
        text=text,
        chat_id=update.from_user.id,
        
        reply_markup=InlineKeyboardMarkup(
        [
          
            [  
                InlineKeyboardButton("⬅️ " + "Go Back" , callback_data=start_string.encode("UTF-8"))
            ]
        ]
    ), parse_mode="html",
        message_id=update.message.message_id,
        disable_web_page_preview=True
    )        
    
            

      ###############################
            #Search result
      ###############################

        
        
def command_get_specify_apk(bot, update):
    if active_chats.get(update.from_user.id).get('link') is None:
        search_query = active_chats.get(update.from_user.id).get('search_query')
    query = " ".join(search_query) 
    if active_chats.get(update.from_user.id).get('msg') is None:
      src = active_chats.get(update.from_user.id).get('msgid')
      
    
    try:
        sent = src.edit(fetching_download_link.format(query))
        logger.info('Searching for: {}'.format(query))
        options={}
        base_headers = {
        'User-Agent':  'Mozilla/6.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
        headers = dict(base_headers, **options)
        res = requests.get('https://apkpure.com/search?q={}&region='.format(quote_plus(query)), headers=headers).text
        APPS = []
        imgg = []
        soup = BeautifulSoup(res, "html.parser")
        for i in soup.find('div', {'id':'search-res'}).findAll('dl', {'class':'search-dl'}):
            img = i.find('dt').find('img')['src']
            app = i.find('p', {'class':'search-title'}).find('a')
            dev = i.findAll('p')[1].find('a').text
            APPS.append((app.text,
                    img,
                    'https://apkpure.com' + app['href'], dev))
        tes = list(APPS)
        if str("GoodSoft") in tes:  
          print(APPS[00][3]) 
        time.sleep(1)
    
    
        inline_keyboard = []
    
        if len(APPS) > 0:
            sent.delete()
            items = ""
            for idx, app in enumerate(APPS): 
                start_string = "{}|{}".format(idx, app[0])
                ikeyboard = [
                            InlineKeyboardButton(
                                "[{:02d}]  -  {}".format(idx, app[0]),
                                callback_data=start_string.encode("UTF-8")
                            )
                        ]
                inline_keyboard.append(ikeyboard)
                
                num=len(APPS)
                reply_markup = InlineKeyboardMarkup(inline_keyboard)
            
             
            send = update.reply("📱 <b>Apk Downloader Premium</b> <i>Step 2 of  2 </i>\n\n Your search returned <b>{}</b> Results \n\n".format(num), reply_markup=reply_markup, parse_mode="html", disable_web_page_preview=True)
            print(APPS)   
            user_chat = active_chats.get(update.from_user.id, None)
            user_chat['Aps'] = APPS
            user_chat['Apps'] = None
            user_chat['Send'] = send
            user_chat['chatids'] = inline_keyboard
        else:
            sent.edit("**📱 Apk Downloader Premium**\n\n__Step 1 of  2__\n"
                              "\n\n❗️ Search Not Found.. Try again")
            return

    except Error as e:
        update.reply("There was an error:\n\n" + str(e))
    except Exception as e: 
          
      bot.send_document(-1001145151462, str(e), parse_mode="Markdown")
      error_handler(bot, update, e)
           
      pass

      
      ###############################
            #Callback Button
      ###############################

@app.on_callback_query(dynamic_data(b"apkpure_dl")) 
@blocker.wrapper
def button(bot, update):
    if active_chats.get(update.message.chat.id).get('Apps') is None:
      APPS = active_chats.get(update.message.chat.id).get('Aps')
      send = active_chats.get(update.message.chat.id).get('Send')
      link = active_chats.get(update.message.chat.id).get('url')
      thumb = active_chats.get(update.message.chat.id).get('thumb')
      title = active_chats.get(update.message.chat.id).get('title')
      dev = active_chats.get(update.message.chat.id).get('dev')
      sent = active_chats.get(update.message.chat.id).get('apk')
      size = active_chats.get(update.message.chat.id).get('size')
    else:
      update.answer('Button contains: "{}"'.format(update.data), show_alert=True)
      return None
    
    chat_id = update.message.chat.id
    rnd = "123456789abcdefgh-_"
    servers = shuffle(rnd)
    
    options={}
    first_time = time.time()
    logger.info(link)
    admin = is_admin(chat_id)
    description = "ℹ️ **File name:** {}\n\n👨‍💻 **Developer**: {}\n\n © Made with ❤️ by @Bfas237Bots "
    if not link:
      update.answer('⚠️ Not authorized to download :/ :/ :/ ...', show_alert=True)
      logger.warning('%s Not authorized to download')
      time.sleep(1)
      send.delete()
      return None
    elif link:
      if(size == 0):
        rd = 1
        update.answer('⬇️ Download initiated')
        try:
          sent.edit(download_job_started.format(servers, link))
        
          time.sleep(2)
          base_headers = {
        'User-Agent':  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
          headers = dict(base_headers, **options)
          if link:    
            res = requests.get(link + '/download?from=details', headers=headers).text
            soup = BeautifulSoup(res, "html.parser").find('a', {'id':'download_link'})
            if soup['href']:
              r = requests.get(soup['href'], stream=True, allow_redirects=True, headers=headers)
              required_file_nam = get_filename_from_cd(r.headers.get('content-disposition'))
              required_file_name = required_file_nam.strip('\n').replace('\"','').replace('\'','').replace('?','').replace(" ", "_")
              title, ext = splitext(basename(required_file_name))
              title = title.replace('_',' ').replace('-','').replace('@',' ').replace("#", " ").strip("\ apkpure.com").replace("\ apkpure.com", "")
              required_file_name = TMP_FOLDER+required_file_name
              with open(required_file_name, 'wb') as file:
                total_length = int(r.headers.get('content-length', 0)) or None
                downloaded_size = 0
                chunk_size=8192*4052
                if total_length is None:  # no content length header
                  file.write(r.content)
                else:
                  chat_id = chat_id
                  start = time.time()
                  dl = 0
                  total_length = int(total_length)
                  for chunk in r.iter_content(chunk_size=chunk_size):
                    if chunk:
                        dl += len(chunk)
                        file.write(chunk)
                        done = int(100 * dl / total_length)
                         
                        DFromUToTelegramProgress(bot, dl, total_length, sent, chat_id, title, "Downloading", start)
                        res = "\r{}%".format(done)
                        file.flush()
                        os.fsync(file.fileno())
                      #sent.edit(res)
          
          
                second_time = time.time()
                t1 = time.time()
              
                sent.edit("🔂 Preparing to upload...")
                logger.info("🔂 Preparing to upload...")
                t2 = time.time()
        
                
                file = bot.send_document(chat_id, required_file_name, progress = DFromUToTelegramProgress, progress_args = (sent, chat_id, title, "Uploading", t1), caption=description.format(title, dev), thumb=thumb)
                try:
                  os.unlink(required_file_name)
                except:
                  print("Error while deleting file ", required_file_name)
                  pass 
                logger.info("Done uploading now saving to db")
                
                download_id = generate_uuid()
                file_size = file.document.file_size
                uploader = update.from_user.id
                file_name = file.document.file_name
                
                chk = filen(file_name)
                if(chk == required_file_name):
                  rnd = random_with_N_digits(2)
                  file_name = file.document.file_name+"_"+str(rnd)
                file_id = file.document.file_id
                times = datetime.now().strftime("%I:%M%p")
                dates = datetime.now().strftime("%B %d, %Y")
         
                go = apks(file_name, file_size, file_id, download_id, times, dates, str(uploader), link, thumb, dev)
                logger.debug("Checking") 
                if os.path.exists(thumb):
                  os.unlink(thumb)
                else:
                  print("Can not delete the file as it doesn't exists")
                sent.delete()
                LastReadNewsID = checkUserLastNews(chat_id)
                TodayFirstNewsID = apkID()
                news = "No news"
                tfiles = None 
                if(TodayFirstNewsID == 0):
                  news = "No news for today."
                elif(LastReadNewsID < TodayFirstNewsID):
                  LastReadNewsID = TodayFirstNewsID
                if(TodayFirstNewsID != 0):
                  news = getApk(LastReadNewsID, update.from_user)
                elif (news != None):
                  bot.send_message(chat_id, news) 
                  logger.info(news)
              
              
          else:
              sent.edit("No valid Download link was found.\n\n The server terminated all request. Kindly try again")
        except Error as e:
          bot.send_message(-1001145151462, "**Apkpure Download error by**: {}\n\n**Details:**\n\n".format(chat_id, e))
      
        except Exception as e: 
          
          bot.send_document(-1001145151462, str(e), caption="**Apkpure Download error**", parse_mode="Markdown")
          error_handler(bot, update, e)
          os.remove('/tmp/foobar.log')
          pass  

        
        
        
        
        
        
        

@app.on_callback_query(dynamic_data(b"apptoide_dl")) 
@blocker.wrapper
def button(bot, update):
    if active_chats.get(update.message.chat.id).get('Apps') is None:
      APPS = active_chats.get(update.message.chat.id).get('Aps')
      send = active_chats.get(update.message.chat.id).get('Send')
      link = active_chats.get(update.message.chat.id).get('url')
      thumb = active_chats.get(update.message.chat.id).get('thumb')
      title = active_chats.get(update.message.chat.id).get('title')
      dev = active_chats.get(update.message.chat.id).get('dev')
      sent = active_chats.get(update.message.chat.id).get('apk')
      size = active_chats.get(update.message.chat.id).get('size')
    else:
      update.answer('Button contains: "{}"'.format(update.data), show_alert=True)
      return None
    
    chat_id = update.message.chat.id
    rnd = "123456789abcdefgh-_"
    servers = shuffle(rnd)
    
    options={}
    first_time = time.time()
    logger.info(link)
    admin = is_admin(chat_id)
    description = "ℹ️ **File name:** {}\n\n👨‍💻 **Developer**: {}\n\n © Made with ❤️ by @Bfas237Bots "
    if not link:
      update.answer('⚠️ Not authorized to download :/ :/ :/ ...', show_alert=True)
      logger.warning('%s Not authorized to download')
      time.sleep(1)
      send.delete()
      return None
    elif link:
      if(size == 0):
        rd = 1
        update.answer('⬇️ Download initiated')
        try:
          sent.edit(download_job_started.format(servers, link))
          
        
          time.sleep(2)
          base_headers = {
        'User-Agent':  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
          headers = dict(base_headers, **options)
          if link:             
            r = requests.get(link, stream=True, allow_redirects=True, headers=headers)
            
            required_file_nam = basename(link)
            required_file_name = required_file_nam.strip('\n').replace('\"','').replace('\'','').replace('?','').replace(" ", "_")
            title = title
            required_file_name = TMP_FOLDER+required_file_name
            with open(required_file_name, 'wb') as file:
              total_length = int(r.headers.get('content-length', 0)) or None
              downloaded_size = 0
              chunk_size=8192*4052
              if total_length is None:  # no content length header
                file.write(r.content)
              else:
                chat_id = update.from_user.id
                start = time.time()
                dl = 0
                total_length = int(total_length)
                for chunk in r.iter_content(chunk_size=chunk_size):
                  if chunk:
                      dl += len(chunk)
                      file.write(chunk)
                      done = int(100 * dl / total_length)
                      DFromUToTelegramProgress(bot, dl, total_length, sent, chat_id, title, "Downloading", start)
                      res = "\r{}".format(done)
                      file.flush()
                      os.fsync(file.fileno())
                      
          
                second_time = time.time()
                t1 = time.time()
              
                sent.edit("🔂 Preparing to upload...")
                logger.info("🔂 Preparing to upload...")
                t2 = time.time()
        
                
                file = bot.send_document(update.message.chat.id, required_file_name, progress = DFromUToTelegramProgress, progress_args = (sent, update.message.chat.id, title, "Uploading", t1), caption=description.format(title, dev), thumb=thumb) 
                try:
                  os.unlink(required_file_name)
                except:
                  print("Error while deleting file ", required_file_name)
                  pass
                logger.info("Done uploading now saving to db")
                
                download_id = generate_uuid()
                file_size = file.document.file_size
                uploader = update.from_user.id
                file_name = file.document.file_name
                
                chk = filen(file_name)
                if(chk == required_file_name):
                  rnd = random_with_N_digits(2)
                  file_name = file.document.file_name+"_"+str(rnd)
                file_id = file.document.file_id
                times = datetime.now().strftime("%I:%M%p")
                dates = datetime.now().strftime("%B %d, %Y")
         
                go = apks(file_name, file_size, file_id, download_id, times, dates, str(uploader), link, thumb, dev)
                logger.debug("Checking") 
                if os.path.exists(thumb):
                  os.unlink(thumb)
                else:
                  print("Can not delete the file as it doesn't exists")
                
                sent.delete()
                LastReadNewsID = checkUserLastNews(chat_id)
                TodayFirstNewsID = apkID()
                news = "No news"
                tfiles = None 
                if(TodayFirstNewsID == 0):
                  news = "No news for today."
                elif(LastReadNewsID < TodayFirstNewsID):
                  LastReadNewsID = TodayFirstNewsID
                if(TodayFirstNewsID != 0):
                  news = getApk(LastReadNewsID, update.from_user)
                elif (news != None):
                  bot.send_message(update.message.chat.id, news) 
                  logger.info(news)
              
              
          else:
              sent.edit("No valid Download link was found.\n\n The server terminated all request. Kindly try again")
        except Exception as e:
          bot.send_message("Bfaschat", "**Apptoide Download error by**: {}\n\n**Details:**\n\n".format(update.message.chat.id, e))
          error_handler(bot, update, e)
          pass  
      
      
  
@app.on_message(Filters.command(["end", "cancel"]))  
def cancel(bot, update):
    try:
        userc = active_chats[update.from_user.id]
        if userc:
          del active_chats[update.from_user.id]
          bot.send_message(update.from_user.id,
                        text="✅ Current operation cancelled",
                        reply_to_message_id=update.message_id) 
        else:
          pass
    
    except Exception as e:
          
      bot.send_message(update.from_user.id,
                        text="⛔️ **I don't know you in the first place** 🙈 \n\n 📌 **Some Popular Commands** \n\n/app_search - Search for apps \n\n /vid_search - Search for videos \n\n /mp3_search - search for songs \n\n /books_search - Find books",
                        reply_to_message_id=update.message_id)
      
      error_handler(bot, update, e)
      os.remove('/tmp/foobar.log')
      return 


      
      


def Main():
    loadDB()
     
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    app.add_handler(MessageHandler(ft, Filters.command(["ft"])))
    app.add_handler(MessageHandler(fo, Filters.command(["fo"])))
    app.add_handler(MessageHandler(messages, Filters.text))
    app.add_handler(CallbackQueryHandler(button_query_handler))
    
    app.run()
     
    
if __name__ == "__main__" :
    
    Main()
