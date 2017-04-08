from urllib2 import Request, urlopen, URLError

# creating the request with desired image 
request_api = "https://api.ocr.space/parse/imageurl?apikey=helloworld&url="
image_url = "http://3.bp.blogspot.com/-Sn54Nua_DSk/VbQm7mTeyaI/AAAAAAAAEo4/dUd_FMvJEsM/s1600/tjs.jpg"
request_language = "&language=chs&isOverlayRequired=true"
request = Request(request_api + image_url + request_language)

try:
	response = urlopen(request)
	receipt_text = response.read()
	print receipt_text
except URLError, e:
    print 'something went wrong here: ', e