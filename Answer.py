import requests
import json

def addToDic(word):
	if word in words:
		words[word]= words[word]+1
	else:
		words[word]= 1

url = 'https://api.namefake.com'
words = {}

requests.packages.urllib3.disable_warnings() 
for x in range(100):
	try:
		response = requests.get(url, verify=False)
		jData = json.loads(response.text)	
		x = jData['name']
		newName = ""
		for c in x:
			newName = newName + str(c)
		y = newName.split()
		if "." in y[0] or "Miss" in y[0]:
			addToDic(y[2])
		else:
			addToDic(y[0])
		addToDic(y[1])
	except:
		continue
newA = sorted(words, key=words.get, reverse=True)[:5]
print (newA)