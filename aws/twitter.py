#!/usr/bin/env python
import os
import pickle,sys
#import sys
#sys.stdout = open('/home/ubuntu/data/scripts/output.log', 'a')
#print 'test'
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#binary = FirefoxBinary('/opt/firefox/firefox')
#http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html
#http://winscp.net/eng/docs/guide_amazon_ec2
#sudo wget https://ftp.mozilla.org/pub/mozilla.org/firefox/releases/23.0b10/linux-x86_64/en-US/	firefox-23.0b10.tar.bz2
#http://www.cyberciti.biz/faq/howto-install-firefox-15-0-tar-bz2-in-linux/
#sudo apt-get install xvfb
#sudo easy_install pyvirtualdisplay
#sudo apt-get install python-dev
#pip install pillow
#sudo apt-get install libmysqlclient-dev
# sudo easy_install  MySQLdb
#easy_install unidecode
#http://stackoverflow.com/questions/20753607/while-upgrading-python-imaging-library-pil-it-tells-me-jpeg-support-not-avai
'''

http://raspberrypi.stackexchange.com/questions/9361/how-do-i-enable-jpeg-support-with-pil
http://stackoverflow.com/questions/20060096/installing-pil-with-pip
sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib
sudo ln -s /usr/lib/arm-linux-gnueabihf/libjpeg.so /usr/lib/

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os
import pdb, traceback,os
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.chrome.options import Options

import datetime
import ftpUpl
import awsPost
import rds
import urllib
def launchFb():
	if os.name!="nt":
		firefoxProfile = FirefoxProfile("/home/ubuntu/.mozilla/firefox/96zm8eem.default")
	else:
		firefoxProfile = FirefoxProfile("C:\Users\kubansal\AppData\Roaming\Mozilla\Firefox\Profiles\9ib58hax.default")
	wd = webdriver.Firefox(firefoxProfile)
	wd.implicitly_wait(15)
	wd.maximize_window()
	wd.get("http://www.twitter.com")
	print "loaded Twitter page"
	return wd

def getTopicElements(wd):
	time.sleep(2)
	trending=wd.find_element_by_class_name("trend-items")
	trendingList=trending.find_elements_by_class_name("trend-item")
	linkList=[]
	for i in trendingList:
		linkElement=i.find_element_by_tag_name("a")
		link=linkElement.get_attribute("href")
		linkList=linkList+[link]
	return linkList
def scrollDown(browser,times):
	for i in range(times):
		browser.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN);
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(2)	
def openFBlinksNewTab(browser,linkList):
	main_window = browser.current_window_handle
	fr=open("/home/ubuntu/data/scripts/data.txt","a")
	# Open the link in a new tab by sending key strokes on the element
	count=1
	for first_link in linkList:
		try:
			count=count+1
			browser.set_page_load_timeout(130)
			browser.get(first_link)
			time.sleep(5)
			scrollDown(browser,15)
			
			results=browser.find_element_by_id("initial_browse_result")
			brief=results.find_element_by_css_selector('._4-u2._3csh._4-u8')
			briefHeading=brief.find_element_by_class_name("_32lj")
			briefD=brief.find_element_by_class_name("_32lk")
			

			heading=escapechars(briefHeading.text)
			Description=escapechars(briefD.text)
			posthash=heading.encode("utf-8")[::3]
			posthash=posthash.replace(" ","")
			posthash=str(posthash)

			time.sleep(5)
			#pdb.set_trace()
			#print "art1 data",
			articles=results.find_elements_by_css_selector("._4-u2._2avg._2_wj._4-u8")
			try:
				art1=articles[0].find_elements_by_class_name("_22p7")[0]
				articles=articles[0]
			except:
				art1=articles[1].find_elements_by_class_name("_22p7")[0]
				articles=articles[1]
			imgTag=art1.find_element_by_tag_name("img")
			imgSrc=imgTag.get_attribute("src")
			imgFile = urllib.URLopener()
			if "jpg" in imgSrc or "jpeg" in imgSrc:
				imageType=".jpg"
			else:
				imageType=".png"
			imgFile.retrieve(imgSrc, "1"+posthash+imageType)
			cropImage("1"+posthash+imageType)
			ftpUpl.uploadFileToFtp("1"+posthash+".png")
			art1=art1.find_element_by_css_selector(".mbs._6m6").find_element_by_tag_name("a")
			link1=art1.get_attribute("href")
			art1=escapechars(art1.text)
			#print "art2 data",
			art2=articles.find_elements_by_class_name("_22p7")[1]
			imgTag=art2.find_element_by_tag_name("img")
			imgSrc=imgTag.get_attribute("src")
			if "jpg" in imgSrc or "jpeg" in imgSrc:
				imageType=".jpg"
			else:
				imageType=".png"
			imgFile = urllib.URLopener()
			imgFile.retrieve(imgSrc, "2"+posthash+imageType)
			cropImage("2"+posthash+imageType)
			ftpUpl.uploadFileToFtp("2"+posthash+".png")
			art2=art2.find_element_by_css_selector(".mbs._6m6").find_element_by_tag_name("a")
			link2=art2.get_attribute("href")
			art2=escapechars(art2.text)
			l1=link1[30:]
			
			l1=urllib.unquote(l1).decode('utf8')
			l1=l1.split("&h=")[0]
			l2=link2[30:]
			l2=urllib.unquote(l2).decode('utf8')
			l2=l2.split("&h=")[0]			
		except Exception,e:
			#print '\033[1;31mGetting Stories:\033[1;m',
			f=open("Tracebacklogs.log","a")
			f.write(traceback.format_exc())
			f.close()
			stories=wd.find_elements_by_class_name("fbStoryAttachmentImage")
			story1=getstory(stories,0,posthash)
			story2=getstory(stories,1,posthash)
			if story2!=None and story1!=None:
				(art1,l1)=story1
				(art2,l2)=story2
				if l1.count("http")>1:
					l1=l1[30:]
					l1=l1.split("&h=")[0]
				l1=urllib.unquote(l1).decode('utf8')
				if l2.count("http")>1:
					l2=l2[30:]
					l2=l2.split("&h=")[0]
				l2=urllib.unquote(l2).decode('utf8')
			else:
				print '\033[1;31mUnable to get stories:\033[1;m',
				return
		finally:
	
			lf=open("links.text","a")
			lf.write(first_link)
			lf.write("\n")
			lf.close()
			
			'''
			postSuccess=awsPost.main(heading.encode("utf-8")[::3],heading.encode("utf-8"), Description.encode("utf-8"), art1.encode("utf-8"),l1.encode("utf-8"),art2.encode("utf-8"),l2.encode("utf-8"))			
			
			if postSuccess:
			'''
			
			postSuccess=rds.main(posthash,heading.encode("utf-8"), Description.encode("utf-8"), art1.encode("utf-8"),l1.encode("utf-8"),art2.encode("utf-8"),l2.encode("utf-8"))			
			
			t = datetime.datetime.utcnow()
			postTime=t.strftime('%Y%m%d %H:%M:%S')
			fr.write("\n"+str(postTime)+":"+heading.encode("utf-8")[::3])
				
				#break
			#updateResults(briefHeading.text, briefD.text, art1.text,link1,art2.text,link2)
		#break
		# Put focus on current window which will be the window opener
		#browser.switch_to_window(main_window)
		#body = wd.find_element_by_tag_name("body")
		#body.send_keys(Keys.CONTROL + 't')
		#break
		#pdb.set_trace()
	fr.close()
def getstory(webelement,index,posthash):
	try: 
		elem=webelement[index].find_element_by_xpath("../../../../../..")
		link=elem.find_element_by_tag_name("a").get_attribute("href")
		imgTag=elem.find_element_by_tag_name("a").find_element_by_tag_name("img")
		imgSrc=imgTag.get_attribute("src")
		imgFile = urllib.URLopener()
		if "jpg" in imgSrc or "jpeg" in imgSrc:
			imageType=".jpg"
		else:
			imageType=".png"
		imgFile.retrieve(imgSrc, str(index+1)+posthash+imageType)
		resizeImage(str(index+1)+posthash+imageType)
		ftpUpl.uploadFileToFtp(str(index+1)+posthash+".png")
		art=elem.find_element_by_css_selector(".mbs._6m6").find_element_by_tag_name("a")
		art=escapechars(art.text)
		return (art,link)
	except:
		#print traceback.format_exc()
		print "Cannot get stories"


def cropImage(filename):
	from PIL import Image

	test_image = "Fedora_19_with_GNOME.jpg"
	original = Image.open(filename)
	width, height = original.size   # Get dimensions
	left = 0
	top = 10
	right = width
	bottom =60
	cropped_example = original.crop((left, top, right, bottom))
	os.remove(filename)
	cropped_example.save(".".join(filename.split(".")[:-1])+".png", "PNG")

def resizeImage(filename):	
	from PIL import Image
	size = 196,100
	im = Image.open(filename)
	im_resized = im.resize(size, Image.ANTIALIAS)
	os.remove(filename)
	im_resized.save(".".join(filename.split(".")[:-1])+".png", "PNG")
	#print "File saved as "+(".".join(filename.split(".")[:-1])+".png")

def escapechars(ll):
	import unicodedata
	from unidecode import unidecode
	ll.replace("'","\\'")
	ll.replace('"','\\"')
	ll.replace("<","")
	ll.replace(">","")
	unicodedata.normalize('NFKD', ll).encode('ascii', 'ignore')
	return ll

wd=launchFb()
linkList=getTopicElements(wd)
print linkList
'''
try:
	if os.path.exists("Tracebacklogs.log"):
		os.remove("Tracebacklogs.log")
	if os.path.exists("links.text"):
		os.remove("links.text")
	if os.name!="nt":
		from pyvirtualdisplay import Display
		display = Display(visible=0, size=(1024, 768))
		display.start()
	count=1
	while 1:
	
		try:
			wd=launchFb()
		
			time.sleep(5)
			print '\033[1;32mcount#'+str(count)+'\033[1;m',
			count=count+1
			linkList=getTopicElements(wd)
			openFBlinksNewTab(wd,linkList)
			
		except:
			print traceback.format_exc()
			time.sleep(10)

		wd.quit()
		t = datetime.datetime.utcnow()
		postTime=t.strftime('%Y%m%d %H:%M:%S')
		print "\033[1;33mpostTime:"+postTime+'\033[1;m'
		#print '\033[1;33mNow Sleeping for 5 minutes\033[1;m'
		time.sleep(1500)
		del wd
		
		#print os.system("pkill firefox")

	#uploadLogToFtp()
	#updateResults("a","b")
except:
	print "XXXX EXception XXXXX"
finally:
	display.stop()
	wd.quit()
'''
