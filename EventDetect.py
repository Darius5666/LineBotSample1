from WhatDay import what_day_today
import random
from UserHandler import get_user_profile
def event_detect(input_text,reply,user_id):
    if 'whoami' in input_text:
        reply.AddText(f"{get_user_profile(user_id)}")
        
    if '今天星期幾' in input_text:
        reply.AddText(f"今天是{what_day_today()}")
        return reply
    
    if '把我小過消掉' in input_text:
        reply.AddText("不要，笑死")
        reply.AddImage("https://stickershop.line-scdn.net/stickershop/v1/product/17811/LINEStorePC/main.png?v=2")
        return reply
    
    if '今天吃什麼' in input_text:
        reply.CreateTemplate(title="今天吃什麼",content="請選擇",mode="Bottom")
        foods = ["牛肉麵","雞腿飯","炸雞","義大利麵","炒飯","水餃","漢堡","披薩","沙拉","壽司"]
        random.shuffle(foods)
        reply.template.AddMessageButton(label = "1", text = foods[0])
        reply.template.AddMessageButton(label = "2", text = foods[1])
        reply.template.AddMessageButton(label = "3", text = foods[2])
        reply.AddTemplate()
        return reply