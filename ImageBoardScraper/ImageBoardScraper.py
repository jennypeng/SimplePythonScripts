import sys
import os
import urllib
import urllib2
from os.path import basename
from urlparse import urlsplit
from bs4 import BeautifulSoup

#Requesting page source data of thread
url = raw_input("Enter the link you wish to scrape here: ").strip()
page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page)
soup.prettify()
	
#Search through the thread to look for posted img urls
for link in soup.find_all('a', {'target': "_blank", 'class': "fileThumb"}):
	imgUrl = link.get('href')
	#Trying to download image
	try:
		imgData = urllib2.urlopen('http:' + imgUrl).read()
		fileName = basename(urlsplit('http:' + imgUrl)[2])
		output = open(fileName, 'wb')
		output.write(imgData)
		output.close()
		os.rename('C:/Users/.../YOURROOTFOLDERNAMEHERE' + fileName,'C:/Users/.../YOUROUTPUTFOLDERHERE/' + fileName)
		print('Downloaded image at ' + imgUrl[2:])
	#If image already exists in output folder, control is directed to except 
	except:
		print('Image at' + imgUrl[2:] + 'is already downloaded into directory')
		pass