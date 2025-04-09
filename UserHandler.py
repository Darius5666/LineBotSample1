from linebot.models import *
def get_user_profile(user_id,line_bot_api):
    return line_bot_api.get_profile(user_id)