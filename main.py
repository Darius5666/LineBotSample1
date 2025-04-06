from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import *
from PostRequest import post_handler
from MessageHandler import message_handler
app = Flask(__name__)
channel_token = 's0P/qx3ljDCsng1raHR+zZo15cgWDMDwzCquvvzLqkTpoLV3yru9g2WetZEyVpXs5h3w/ggfAQyKx3xrKKnVGP0Rt0hxE50zmaft4u0/xmCWZz+sRgfkaoUy8hKOZWPI8k8flOgsruQ8Ld/EwEtmFwdB04t89/1O/w1cDnyilFU='
channel_secret ='f6dc6646262524d0135774409a2c4f66'
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