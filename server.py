def command_get_specify_apk(bot, update):
    if active_chats.get(update.from_user.id).get('link') is None:
        search_query = active_chats.get(update.from_user.id).get('search_query')
    query = " ".join(search_query) 
    try:
        sent = update.reply(fetching_download_link.format(query),
        quote=True, disable_web_page_preview=True)
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
        time.sleep(2)
    
    
        inline_keyboard = []
    
        if len(APPS) > 0:
            sent.delete()
            items = ""
            for idx, app in enumerate(APPS):
                items +=  ("[{:02d}]  -  {}".format(idx, app[0]))
        
                start_string = "{}|{}".format(idx, app[0])
            ikeyboard = [InlineKeyboardButton(items, callback_data=start_string.encode("UTF-8"))]
            inline_keyboard.append(ikeyboard)
            user_chat = active_chats.get(update.from_user.id, None)
            user_chat['Aps'] = APPS
            user_chat['Apps'] = None      
        
            num=len(APPS)
            reply_markup = InlineKeyboardMarkup(inline_keyboard)
            update.reply("📱 <b>Apk Downloader Premium</b> __Step 2 of  2__: <b>{}</b> Results \n\n".format(num), reply_markup=reply_markup, parse_mode="html", disable_web_page_preview=True, quote=True)
            
        else:
            sent.edit("**📱 Apk Downloader Premium**\n\n__Step 1 of  2__\n"
                              "\n\n❗️ Search Not Found.. Try again")
            return

    except Exception as e:
        update.reply(str(e))
    except:
      traceback.print_exc()

