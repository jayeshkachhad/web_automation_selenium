from urllib.parse import urlencode
from urllib.request import Request, urlopen
import base64

# remote image from url
url = 'https://www.pushsafer.com/api'
post_fields = {
	"t" : 'Alert',
	"m" : 'Test Message',
	"s" : 11,
	"v" : 3,
	"i" : 33,
	"c" : '#FF0000',
	"d" : 'a',
	"u" : 'https://www.pushsafer.com',
	"ut" : 'Open Pushsafer',
	"k" : '6bXm7ePPLStqqnzhLXrh',
	}

request = Request(url, urlencode(post_fields).encode())
json = urlopen(request).read().decode()
print(json)