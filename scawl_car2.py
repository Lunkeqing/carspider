from lxml import etree
from StringIO import StringIO
import requests
ll = [
	"http://www.autohome.com.cn/grade/carhtml/A.html",
	"http://www.autohome.com.cn/grade/carhtml/B.html",
	"http://www.autohome.com.cn/grade/carhtml/C.html",
	"http://www.autohome.com.cn/grade/carhtml/D.html",
	"http://www.autohome.com.cn/grade/carhtml/F.html",
	"http://www.autohome.com.cn/grade/carhtml/G.html",
	"http://www.autohome.com.cn/grade/carhtml/H.html",
	"http://www.autohome.com.cn/grade/carhtml/J.html",
	"http://www.autohome.com.cn/grade/carhtml/K.html",
	"http://www.autohome.com.cn/grade/carhtml/L.html",
	"http://www.autohome.com.cn/grade/carhtml/M.html",
	"http://www.autohome.com.cn/grade/carhtml/N.html",
	"http://www.autohome.com.cn/grade/carhtml/O.html",
	"http://www.autohome.com.cn/grade/carhtml/P.html",
	"http://www.autohome.com.cn/grade/carhtml/Q.html",
	"http://www.autohome.com.cn/grade/carhtml/R.html",
	"http://www.autohome.com.cn/grade/carhtml/S.html",
	"http://www.autohome.com.cn/grade/carhtml/T.html",
	"http://www.autohome.com.cn/grade/carhtml/W.html",
	"http://www.autohome.com.cn/grade/carhtml/X.html",
	"http://www.autohome.com.cn/grade/carhtml/Y.html",
	"http://www.autohome.com.cn/grade/carhtml/Z.html",
]
def get_type(url):
	#print url
	t = requests.get(url)
	#print t.text
	parser = etree.HTMLParser()
	tree   = etree.parse(StringIO(t.text), parser)
	item_list = tree.xpath('//li[@id]')

	#print len(item_list)
	res = []
	for item in item_list:
		res.append(item.get('id')[1:])
	return res



if __name__ == "__main__":
	id_list = []
	for url in ll:
		id_list.extend(get_type(url))
	for id in id_list:
		print id	





