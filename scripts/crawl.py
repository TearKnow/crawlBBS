from bs4 import BeautifulSoup
from urllib.request import urlopen


listUrl = "http://bbs.xinjs.cn/thread.php?fid=45"


html = urlopen(listUrl)

soup = BeautifulSoup(html.read(), "html.parser")

list = soup.find(attrs={"id": "threadlist"})
posts = list.findAll(attrs={"class": "tr3"})
for post in posts:
	nameObj = post.find(attrs={"class": "subject_t"})
	authAndDate = post.find(attrs={"class": "author"})
	
	name = nameObj.string
	auth = authAndDate.find(attrs={"class": "_cardshow"}).string
	date = authAndDate.find("p").string
	
	
	print(name)
	print(auth)
	print(date)
	#exit()
	
	#print(type(authAndDate))
	#authAndDateObj = BeautifulSoup(authAndDate, "html.parser")
	#auth = authAndDateObj.find(attrs={"class": "_cardshow"})
	#print(auth)