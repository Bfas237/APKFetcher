
from os import path
import logging, urllib, os, re, sys, sqlite3, json, io, requests, datetime, requests, shutil, traceback, os.path, urllib.request, time, fnmatch, subprocess, math
#shutil.rmtree('/screenshots/') 
from pyrogram import Client, Filters, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, ForceReply, MessageHandler, CallbackQueryHandler
from pyrogram.api import types, functions
try:
    from urllib.parse import quote_plus
    import urllib.request
    python3 = True
except ImportError:
    from urllib import quote_plus
    import urllib2
    python3 = False
import warnings, random
from random import randint
from translation import Translation
from pyrogram import Error

from uuid import uuid4 
from functools import wraps
from difflib import SequenceMatcher
import random as r
from requests import get
import sqlite3 as lite
from utils.guess import *
logger = logging.getLogger(__name__)

  
req_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.A.B.C Safari/525.13',
        'Referer': 'http://python.org'}
from urllib.request import urlopen


from bs4 import BeautifulSoup
from datetime import datetime, timezone, date
from urllib.parse import unquote, urlparse
from os.path import splitext, basename
APP_FOLDER = os.path.dirname(os.path.realpath(__file__))
options={}
base_headers = {   
        'User-Agent':  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
headers = dict(base_headers, **options) 
from utils.dbmanager import *
