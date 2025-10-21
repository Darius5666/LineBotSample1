from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import *
from PostRequest import post_handler
from MessageHandler import message_handler
app = Flask(__name__)
channel_token = ''
channel_secret =''
# Channel Access Token
line_bot_api = LineBotApi(channel_token)
# Channel Secret
handler = WebhookHandler(channel_secret)
post_handler(app = app, handler = handler)
message_handler(handler = handler, line_bot_api = line_bot_api)
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
