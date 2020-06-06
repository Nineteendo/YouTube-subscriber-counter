import urllib.request, ssl, json
name=USERNAME_OR_ID
key=API_KEY
url="https://www.googleapis.com/youtube/v3/channels?part=statistics&key="+key
subs=urllib.request.urlopen(url+"&forUsername="+name,context=ssl._create_unverified_context()).read()
if not "subscriberCount" in str(subs):
	subs=urllib.request.urlopen(url+"&id="+name,context=ssl._create_unverified_context()).read()
print(name + " has " + "{:,d}".format(int(json.loads(subs)["items"][0]["statistics"]["subscriberCount"])) + " subscribers!")