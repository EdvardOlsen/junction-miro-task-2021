token='...'
import telebot
from PIL import Image, ImageDraw, ImageFont
from urllib.request import urlretrieve
import requests
from random import choice, randint
import os
import random
import telebot
import easyocr
reader = easyocr.Reader(['en','en'])
i = 0
whiteboard_id = '...'
bot = telebot.TeleBot(token)
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer ..."
}
def post_text(whiteboard_id='o9J_lhpZ7K0=', text='hello'):
  payload = {
    "data": {"content": f"<p>{text}</p>"},
    "style": {
        "backgroundColor": choice(["#e6e6e6", "#9477d9", "#d977b5", "#cfd977"]),
        "backgroundOpacity": "1.0",
        "fontFamily": "arial",
        "textAlign": "center",
        "fontSize": "100"
    },
    "geometry": {
        "x": str(randint(0,10000)),
        "y": str(randint(0,10000)),
        "width": "1000",
        "rotation": "0"
    }}
  url = f'https://api.miro.com/v2/boards/{whiteboard_id}/texts'
  response = requests.request("POST", url, json=payload, headers=headers)
  print(response.text)
  return response.text.split(',')[0].split(':')[1][2:-1]

