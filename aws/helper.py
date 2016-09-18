def updateResults(heading, Description, art1,link1,art2,link2):
	trr=time.strftime("%H:%M:%S")
	xmlfilestr = r'/home/ubuntu/data/result.xml'
	import os
	import xml.etree.cElementTree as ET
	if os.path.exists(xmlfilestr):
		rootx= ET.parse(xmlfilestr).getroot()
	else:
		rootx = ET.Element("root")
	#pdb.set_trace()
	root = ET.Element("post",name=heading[::3])
	heading=escapechars(heading)
	Description=escapechars(Description)
	art1=escapechars(art1)
	art2=escapechars(art2)

	ET.SubElement(root, "heading").text = heading
	ET.SubElement(root, "Description").text = Description
	ET.SubElement(root, "heading1").text = art1
	l1=link1[30:]#.replace("%3A",":").replace("%2F","/")
	import re
	import urllib
	l1=urllib.unquote(l1).decode('utf8')
	l1=l1.split("&h=")[0]
	ET.SubElement(root, "link1").text = l1
	l2=link2[30:]#.replace("%3A",":").replace("%2F","/")
	#pdb.set_trace()
	l2=urllib.unquote(l2).decode('utf8')
	l2=l2.split("&h=")[0]
	ET.SubElement(root, "heading2").text = art2
	ET.SubElement(root, "link2").text = l2
	rootx.append(root)
	tree = ET.ElementTree(rootx)
	tree.write(xmlfilestr)


def wdwait(wd,timex=600):
	ref=timex/200
	for i in range(ref):
		time.sleep(200)
		wd.refresh()
