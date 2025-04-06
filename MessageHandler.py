
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import *
from MessageSendHandler import MessageSendHandler
from EventDetect import event_detect


def message_handler(handler,line_bot_api):
    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        reply = MessageSendHandler(event.reply_token,line_bot_api)
        event_text = event.message.text
        reply = event_detect(event_text,reply)
        if reply != None:
            reply.SendMessage()

    @handler.add(PostbackEvent)
    def handle_postback(event):
        data = event.postback.data
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='Postback data: {}'.format(data))
)
    