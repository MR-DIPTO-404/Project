#WRITTEN BY MR.DIPTO
#FOLLOW MY GITHUB : https://github.com/MR-DIPTO-404
#----------import----------#
import os
try:
    import httpx
except ModuleNotFoundError:
    os.system('pip install httpx >/dev/null')
try:
    from bs4 import BeautifulSoup as bb
except ModuleNotFoundError:
    os.system('pip install bs4 >/dev/null')
#----------user input----------#
url=input(' ENTER YOUR URL : ')
#----------extract----------#
soup=bb(httpx.get(url).content,'html.parser')
for link in soup.find_all('a'):
    hrefx=link.get('href')
    print(' YOUR EXTRACT LINK IS : '+hrefx)
    
#WAIT FOR NEXT TOPIC 