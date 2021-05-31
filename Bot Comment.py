try:
        import requests
        import sys
        import time
        from time import sleep
        from instabot import Bot
        import colorama
        from colorama import Fore
        colorama.init(autoreset=True)
except Exception as lib:
        print(lib)
        input()
        sys.exit()
bot = Bot
r = requests.session()
count = 0
username = input("username>: ")
password = input("password>: ")
url_login = 'https://www.instagram.com/accounts/login/ajax/'
headers_login = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '259',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=A8F12857-A12B-4E23-B5D1-B40169809504; mid=YDtfbAALAAE6JNkFQPVp6Xqj9f0s; ig_nrcb=1; shbid=10475; shbts=1614503840.6921477; rur=FTW; csrftoken=T2tmvgY4ZcVStZWf2t2kFg5SkLMyeCdf',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
        'x-csrftoken': 'T2tmvgY4ZcVStZWf2t2kFg5SkLMyeCdf',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR2zRYl4QYaWW3AluGpM9gi7a8iKcQSNEpfuwqOqpEcqpuio',
        'x-instagram-ajax': '0edc1000e5e7',
        'x-requested-with': 'XMLHttpRequest',
        }
data_login = {
        'username': f'{username}',
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}'
        }
r1 = r.post(url_login, headers=headers_login, data=data_login)
if '"authenticated":true' in r1.text:
        print(Fore.GREEN+f"[+] Logged In >> @{username}")
else:
        print(Fore.RED+f'[-] Failed Login >> @{username}')
        input()
        sys.exit()
sessionid = r1.cookies['sessionid']
url = input("post url>: ")
post_id = bot.get_media_id_from_link(self='',link=url)
url_comment = f'https://www.instagram.com/web/comments/{post_id}/add/'
headers_comment = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '42',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=A8F12857-A12B-4E23-B5D1-B40169809504; mid=YDtfbAALAAE6JNkFQPVp6Xqj9f0s; ig_nrcb=1; shbid=10475; shbts=1614503840.6921477; csrftoken=Iytc0tyd1BTP4vRe1pi8caxVBLqPehpp; ds_user_id=434977737; sessionid='+sessionid,
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/p/CL4c1-BBUD8/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
        'x-csrftoken': 'Iytc0tyd1BTP4vRe1pi8caxVBLqPehpp',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR2zRYl4QYaWW3AluGpM9gi7a8iKcQSNEpfuwqOqpEcqpgGf',
        'x-instagram-ajax': '0edc1000e5e7',
        'x-requested-with': 'XMLHttpRequest',
        }
comment = input("comment>: ")
sleep = int(20)
data_comment = {
    'comment_text': f'{comment}',
    'replied_to_comment_id': ''
}
while True:
 r2 = r.post(url_comment, headers=headers_comment, data=data_comment)
 if '"status":"ok"' in r2.text:
  count +=1
  print(Fore.GREEN+f"[{count}] Comment sent")
  time.sleep(sleep)





