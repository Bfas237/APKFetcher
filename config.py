
from pyrogram import Client, Filters
import os
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


class Config(object):
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 14000000000
    CHUNK_SIZE = 8192
    LOGS_GROUP = -1001139726492
    TOKEN = os.environ.get("TOKEN")
    SESSION_NAME = os.environ.get("TOKEN")
    API_ID = os.environ["APP_ID"]
    API_HASH = os.environ["API_HASH"]
app = Client(
    Config.SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH)