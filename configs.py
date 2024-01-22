# in & as LazyDeveloper
# Please Don't Remove Credit

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 22427155))
    API_HASH = os.environ.get("API_HASH", "e878d26d7912064d53f197474e72d4c5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6425587556:AAGS593_w0I-RyUu8x5-7_CuzKHP7r78oXM")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "TeraboxMovieSearch_bot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQFWNhMAMsIC8DyAjTQh4zg9RDYVqao4EAXoLf2aCwkzfOQP6VlkWu5QdxyHOEFpFyaqOY2HGQIfhhQDQ6jLlYMgFW6TDS_XoBy-WCnVnkfuclNby4TRBMK1YSbevMrsIH611U8Y5rra5dMk3OwRoMhP-6MDbwXBSadQzylhvfvjAm1NonbkT3akFF_6CXa5cyuvOOT092dJprczEbocPi6mtpMqCrTTUdfFK_1omjx6B_w7vUI8INg6XmxmFpKRh8UtSKsN5oe88qIPJJzBUuXeu9POP33U0Kq_7XRnllySV4H_TYJzbJOe5fdBFlbOMIjJqDhQxZNozkhMTeQ1gIIg0-n6kAAAAAF-_q9kAQ")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1002104849059))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TeraboxMovieSearch_bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "6267023743"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://linksearch72:ld1KhCKo9Yzbnczj@cluster0.lysnymj.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b> <a href='https://t.me/LazyUrlHunterrBOT'>Lazy Url Hunterr</a> is an open source project.

    Devs: 
        <a href='https://t.me/mRiderDM'>❤️ LazyDeveloper ❤️</a>
    
    
🤖 My Name: <a href='https://t.me/Official_Movies_Group'>Mdisk Search Robot</a>

📝 Language: <a href='https://www.python.org'>Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'>Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

📡 Server 2: <a href='https://heroku.com'>koyeb</a> <i>comming soon</i>

👨‍💻 Developer Channel: <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a></b>
"""

    ABOUT_HELP_TEXT = """<b>💋 Developer : <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hello Baby ! {}😅,

I'm the one and only fastest URL finder BOT. Add me to any Group and Give me Hunting rights !!

I will be only yours if you will restrict adding me to other groups.
Go to @BotFather to change settings.

Don't be sad ! Your all urls are in safe Hand.

»»» <b>Happy Hunting</b> «««

🔺Thank You <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a>🔺 </b>
"""


    START_MSG = """
<b>Hello Baby ! {}😅,

I'm the one and only fastest URL & post finder BOT. Add me to any Group and Give me Hunting rights !!

Don't be sad ! Your all urls are in safe Hand.</b>

   »»»» <b>Happy Hunting</b> ««««

💸<b>Donate us to Keep service Alive.💸</b>
»» A small amount of ₹5 - ₹20 - ₹50 - ₹100 will be great help !
🔺 Thank You 🔺 
"""

