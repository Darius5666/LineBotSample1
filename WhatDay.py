import datetime
def  what_day_today():
    today=datetime.date.today()
    day=today.isoweekday()
    if day==1:
        return "星期一"
    elif day==2:
        return "星期二"
    elif day==3:
        return "星期三"
    elif day==4:
        return "星期四"
    elif day==5:
        return "星期五"
    elif day==6:
        return "星期六"
    elif day==7:
        return "星期日"
