
#!/usr/bin/python
# -*- coding: utf-8 -*-

from ezprint import *
import random
import time
import sys
import vk

peerId = None
token = ''
session = vk.Session(access_token = token)
vkapi = vk.API(session)
r = random.randrange(1, 1000000)
mes = ''


def main():
	global peerId
	global token
	global mes

	cls()
	print('SpamBot VK 1.0')
	print('1.Start')
	print('2.Author')
	print('3.Help')
	print('4.Exit')
	value = input('>>>')
	if value == '1':
		try:
			token = input('Input your token: ')
		except:
			print('incorrect data!')
			main()
		try:
			n = int(input('Number of messages: '))
		except:
			print('incorrect data!')
			main()
		try:
			peerId = input('Input user id for spam: ')
		except:
			print('incorrect data!')
			main()
		try:
			mes = input('Text for message: ')
		except:
			print('incorrect data!')
			main()
		try:
			sl = float(input('Input delay: '))
		except:
			print('incorrect data!')
			main()
		i = 0
		if n < 1:
			print('incorrect data!')
			main()
		else:
			while i < n:
				try:
					i+=1
					r = random.randrange(1, 1000000)
					vkapi.messages.send(v = '5.85', peer_id = peerId, message = mes + str(r))
					sys.stdout.write('\r\r' + 'Messages number: ' + (str(i)))
					time.sleep(sl)
				except:
					print('Input capcha!')
					time.sleep(10)
					main() 
	elif value == '2':
		print('Programmer: Midaef')
		print('            Stdian')
		time.sleep(5)
		main()
	elif value == '3':
		print('HElP: ')
		print('How to get your token?')
		print('	1)https://vkhost.github.io')
		print('	2)Choose button "VK API"')
		print('	3)Copy the token from the address bar')
		print('How to get id user for spam?')
		print('	1)Go to the user profile for spam')
		print('	2)Choose your photo')
		print('	3)Copy the id from the address bar')
	elif value == '4':
		exit()


if __name__ == '__main__':
	main()