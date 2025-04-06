from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import *
from GoogleDriveShareToHttps import Modify

class SetBottomTemplate:
    def __init__(self,title,content,img_url=None):
        self.template = TemplateSendMessage(
            alt_text = 'ButtonsTemplate',
            template = ButtonsTemplate(
                thumbnail_image_url = Modify(img_url) if img_url is not None else None,

                text =  content,
                actions = []
            )
        )
    def IsOverSize(self):
        if len(self.template.template.actions) >= 4:
            return True
        else:
            return False

    def AddUriButton(self,label,uri):
        if not self.IsOverSize():
            self.template.template.actions.append(URITemplateAction(label = label, uri = uri))

    def AddPostBackButton(self,label,data):
        if not self.IsOverSize():
            self.template.template.actions.append(PostbackTemplateAction(label = label, data = data))

    def AddMessageButton(self,label,text):
        if not self.IsOverSize():
            self.template.template.actions.append(MessageTemplateAction(label = label, text = text))

class SetConfirmTemplate:
    def __init__(self,title,content=None,img_url=None):
        self.template = TemplateSendMessage(
            alt_text = 'ConfirmTemplate',
            template = ConfirmTemplate(
                text = title,
                actions = []
            )
        )

    def IsOverSize(self):
        if len(self.template.template.actions) >= 2:
            return True
        else:
            return False
    
    def AddMessageConfirm(self,label,text):
        if not self.IsOverSize():
            self.template.template.actions.append(MessageAction(label = label, text = text))
    
    
class MessageSendHandler:
    def  __init__(self,reply_token,line_bot_api):
        self.line_bot_api = line_bot_api
        self.message = list()
        self.template=None
        self.reply_token = reply_token

    def AddText(self,text):
        self.message.append(TextSendMessage(text=text))
        return self.message

    def AddImage(self,img_url):
        img_url = Modify(img_url)
        self.message.append(ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
        return self.message


    def AddButtomTemplate(self):
        self.message.append(self.template.bottom_template)
        return self.message
    
    def CreateTemplate(self,title,content,mode,img_url=None):
        if mode == "Bottom":
            self.template = SetBottomTemplate(title=title,content=content,img_url=img_url)
        elif mode == "Confirm":
            self.template = SetConfirmTemplate(title=title,content=content,img_url=img_url)

    def AddTemplate(self):
        self.message.append(self.template.template)
        return self.message
    
    def SendMessage(self):
        self.line_bot_api.reply_message(self.reply_token, self.message)



