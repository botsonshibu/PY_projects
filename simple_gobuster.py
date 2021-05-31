#simplegobutser type program

#wordlist importing

import requests

#with open("wordlist",'r') as w:

_
while 1:
	try:
		url = input("Enter the url you wanna test : ")
		response = requests.get(url)
		print("Connection success : ",response)
		break
	except ValueError:
		print("Not an url Try another")

	except Exception as e:
		print("Url not valid..!!!!")
		print(e)
