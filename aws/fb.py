#!/usr/bin/env python
import os
import pickle,sys
#import sys
#sys.stdout = open('/home/ubuntu/data/scripts/output.log', 'a')
#print 'test'
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#binary = FirefoxBinary('/opt/firefox/firefox')

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
def getmd5(title):
	import hashlib
	m = hashlib.md5()
	m.update(title)
	return m.hexdigest()	

def launchFb():

	## get the Firefox profile object
	#chromedriver = "/home/ubuntu/data/scripts/firefoxprofile/chromedriver"
	#os.environ["webdriver.chrome.driver"] = chromedriver
	#chrome_options = Options()
	#chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:28282")
	#webDriver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
	
	if os.name!="nt":
		#print os.listdir("/home/ubuntu/.mozilla/firefox")
		firefoxProfile = FirefoxProfile("/home/ubuntu/.mozilla/firefox/Profiles/96zm8eem.default")
		#print os.listdir("/home/ubuntu/.mozilla/firefox")
	else:
		firefoxProfile = FirefoxProfile("C:\Users\kubansal\AppData\Roaming\Mozilla\Firefox\Profiles\9ib58hax.default")
	
	## Disable CSS
	#firefoxProfile.set_preference('permissions.default.stylesheet', 2)
	## Disable images
	#firefoxProfile.set_preference('permissions.default.image', 2)
	## Disable Flash
	#firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')
	## Set the modified profile while creating the browser object 
	#http://kb.mozillazine.org/About:config_entries
	#http://unix.stackexchange.com/questions/9107/how-can-i-run-firefox-on-linux-headlessly-i-e-without-requiring-libgtk-x11-2-0
	wd = webdriver.Firefox(firefoxProfile)
	#wd = webdriver.PhantomJS()
	#wd.set_window_size(1120, 550)
	#wd=webdriver.Firefox()
	#jajafitufa123
	wd.implicitly_wait(15)
	wd.switch_to_default_content()
	wd.maximize_window()
	'''
	if os.path.exists("cookies.pkl"):
		cookies = pickle.load(open("cookies.pkl", "rb"))
		for cookie in cookies:
			print str(cookies.index(cookie))+ " of "+str(len(cookies))
			wd.add_cookie(cookie)
	'''
	#pdb.set_trace()
	wd.get("http://www.facebook.com")
	#pdb.set_trace()
	#wd.find_element_by_id("loginbutton").click()
	#print "Logged in"
	#wd.save_screenshot("xx2.png")
	
	#wd.get("https://www.facebook.com/?sk=nf")
	#time.sleep(10)
	#wd.get("https://www.facebook.com/?ref=tn_tnmn")
	#time.sleep(10)
	print "loaded facebook page"
	#wd.find_element_by_id("u_0_e").click()
	#wd.find_element_by_id("u_0_e").click()
	
	return wd
def getTopicElements(wd):
	#top=wd.find_element_by_id("pagelet_trending_tags_and_topics")
	#top.find_element_by_class_name("uiHeaderTitle").click()
	time.sleep(2)
	#print "getting getTopicElements"
	top=wd.find_element_by_id("pagelet_trending_tags_and_topics")
	#print top.get_attribute("innerHTML")
	#pdb.set_trace()
	#top.find_element_by_class_name("uiHeaderTitle").click()
	#pdb.set_trace()
	left=top.find_elements_by_tag_name("a")
	left[-1].click()
	time.sleep(2)
	top=wd.find_element_by_id("pagelet_trending_tags_and_topics")
	left=top.find_elements_by_tag_name("a")
	linkList=[]
	for i in left:
		
		
		link=i.get_attribute("href")
		#print i
		if link.find("#")!=-1:
			#print i
			continue
		g= i.find_element_by_xpath('../../../../..')
		#print g.get_attribute("data-position")
		#pdb.set_trace()
		linkList=linkList+[i.get_attribute("href")]
		#print i.text
	#print linkList
	return linkList
	
def openFBlinksNewTab(browser,linkList):
	main_window = browser.current_window_handle
	fr=open("/home/ubuntu/data/scripts/data.txt","a")
	# Open the link in a new tab by sending key strokes on the element
	count=1
	for first_link in linkList:
		try:
			
			print " "+str(count),
			# Use: Keys.CONTROL + Keys.SHIFT + Keys.RETURN to open tab on top of the stack 
			#first_link.send_keys(Keys.CONTROL + Keys.RETURN)
			#body = browser.find_element_by_tag_name("body")
			#body.send_keys(Keys.CONTROL + 't')
			# Switch tab to the new tab, which we will assume is the next one on the right
			#browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

			# Put focus on current window which will, in fact, put focus on the current visible tab
			#browser.switch_to_window(main_window)
			count=count+1
			#print "Link"+str(count)+":"+str(first_link)
			#print count,
			browser.set_page_load_timeout(130)
			browser.get(first_link)
			# do whatever you have to do on this page, we will just got to sleep for now
			#time.sleep(10)
			#break
			# Close current tab
			time.sleep(5)

			browser.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN);
			browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(2)
			browser.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN);
			browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(2)
			browser.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN);
			browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(2)
			browser.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN);
			browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(2)
			browser.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN);
			browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(2)
			browser.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN);
			#wd.save_screenshot(os.path.join("/home/ubuntu/data/scripts",(str(count)+".png")))
			#print "User scroll now"
			#time.sleep(160)
			
			results=browser.find_element_by_id("initial_browse_result")
			brief=results.find_element_by_css_selector('._4-u2._3csh._4-u8')
			briefHeading=brief.find_element_by_class_name("_32lj")
			briefD=brief.find_element_by_class_name("_32lk")
			

			heading=escapechars(briefHeading.text)
			Description=escapechars(briefD.text)
			
			
			posthash=str(heading)
			posthash=getmd5(posthash)
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
		
	
		lf=open("links.text","a")
		lf.write(first_link)
		lf.write("\n")
		lf.close()
		
		'''
		postSuccess=awsPost.main(getmd5(heading),heading.encode("utf-8"), Description.encode("utf-8"), art1.encode("utf-8"),l1.encode("utf-8"),art2.encode("utf-8"),l2.encode("utf-8"))			
		
		if postSuccess:
		'''
		
		postSuccess=rds.main(posthash,heading.encode("utf-8"), Description.encode("utf-8"), art1.encode("utf-8"),l1.encode("utf-8"),art2.encode("utf-8"),l2.encode("utf-8"))			
		
		#t = datetime.datetime.utcnow()
		#postTime=t.strftime('%Y%m%d %H:%M:%S')
			#fr.write("\n"+str(postTime)+":"+getmd5(heading))
				
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
		print traceback.format_exc()
		print "Cannot get stories"


def cropImage(filename):
	from PIL import Image
	pass
	original = Image.open(filename)
	width, height = original.size
	size = 196,110   # Get dimensions
	left = 0
	top = 10
	right = width
	bottom =60
	cropped_example = original.resize(size, Image.ANTIALIAS)
	os.remove(filename)
	cropped_example.save(".".join(filename.split(".")[:-1])+".png", "PNG")
	
def resizeImage(filename):	
	from PIL import Image
	size = 196,110
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
			wd.quit()
		except:
			#pdb.set_trace()
			print traceback.format_exc()
			time.sleep(10)

		
		t = datetime.datetime.utcnow()
		postTime=t.strftime('%Y%m%d %H:%M:%S')
		print "\033[1;33mpostTime:"+postTime+'\033[1;m'
		#print '\033[1;33mNow Sleeping for 5 minutes\033[1;m'
		time.sleep(600)
		try:
			del wd
		except:
			pass
		
		#print os.system("pkill firefox")

	#uploadLogToFtp()
	#updateResults("a","b")
except:
	print "XXXX EXception XXXXX"
finally:
	display.stop()
	wd.close()
