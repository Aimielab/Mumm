import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7434143584:AAFE9kCx0EJTN4DVcUzB0OtNZzjDkI0Vk3w")
    API_ID = int(os.environ.get("API_ID", "20763817"))
    API_HASH = os.environ.get("API_HASH", "07186e8f2ffe607e99eedf7eaa5e630b")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1002457281221")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
