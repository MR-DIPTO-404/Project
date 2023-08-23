#FOLLOW OUR PAGE : https://www.facebook.com/PING.WORLD.404
#FOLLOW MY GITHUB : https://github.com/MR-DIPTO-404
import os
try:
    import pyshorteners
except ModuleNotFoundError:
    os.system('pip install pyshorteners > /dev/null')
url=input(' ENTER YOUR LONG URL : ')
shortx=pyshorteners.Shortener()
short_url=shortx.tinyurl.short(url)
print(' YOUR SHORT URL IS : '+short_url)
#BYE GUYS TAKE LOVE 💕