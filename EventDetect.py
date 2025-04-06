from WhatDay import what_day_today
def event_detect(input_text,reply):
    if '今天星期幾' in input_text:
        reply.AddText(f"今天是{what_day_today()}")
        return reply
    
    if '把我小過消掉' in input_text:
        reply.AddText("不要，笑死")
        reply.AddImage("https://stickershop.line-scdn.net/stickershop/v1/product/17811/LINEStorePC/main.png?v=2")
        return reply