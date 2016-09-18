#http://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=3&ved=0CC4QFjAC&url=http%3A%2F%2Fstackoverflow.com%2Fquestions%2F372885%2Fhow-do-i-connect-to-a-mysql-database-in-python&ei=wkOFVZD7LcSVuAT-rb64Bg&usg=AFQjCNH7Pv1DjfYtD3udnoRxlTf_aDSM2A&sig2=85XO_UxL5Of9eOR2VmrFkQ
#http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-rds.html
#http://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python
import MySQLdb,pdb
import traceback
import datetime
#pdb.set_trace()
def changeQuotes(word):
	word=list(word)
	for i in range(len(word)):
		if word[i]=='"':
			word[i]="'"
	word= "".join(word)
	return word
def main(posthash,postTitle,description,art1,link1,art2,link2):
	posthash=changeQuotes(posthash)
	postTitle=changeQuotes(postTitle)
	description=changeQuotes(description)
	art1=changeQuotes(art1)
	link1=changeQuotes(link1)
	art2=changeQuotes(art2)
	link2=changeQuotes(link2)
	t = datetime.datetime.utcnow()
	amz_date = t.strftime('%Y%m%dT%H%M%SZ')
	date_stamp = t.strftime('%Y%m%d') # Date w/o time, used in credential scope
	postTime=t.strftime('%Y%m%d %H:%M:%S')
	try:
		db = MySQLdb.connect(host="fbdata.ct65u9ws9w27.us-east-1.rds.amazonaws.com",user="kunal212",passwd="",db="fbdb",port=3306) # name of the data base
		cur = db.cursor()
		
		'''cur.execute(''CREATE TABLE fbtrendingdata(
			posttime varchar(1000),
			posthash varchar(1000),
			postTitle varchar(1000),
			description varchar(1000),
			art1 varchar(1000),
			link1 varchar(1000),
			art2 varchar(1000),
			link2 varchar(1000)
			)')
		'''
		 
		#print cur.execute('TRUNCATE TABLE fbtrendingdata;')
		try:
			cur.execute('Insert Into fbtrendingdata VALUES("'+postTime+'","'+posthash+'","'+postTitle+'","'+description+'","'+art1+'","'+link1+'","'+art2+'","'+link2+'")')
			print '\033[1;32mn\033[1;m',
		except:
			#print ('UPDATE fbtrendingdata SET postTime=\"'+postTime+'\" where posthash='+posthash+";")

			cur.execute('UPDATE fbtrendingdata SET postTime=\"'+postTime+'\" where posthash=\"'+posthash+"\";")
			print '\033[1;32mu\033[1;m',
		#print cur.execute('Insert Into Persons VALUES(23354,"dd","dfsdf","sd","asddd") ')

		'''		
		cur.execute('SELECT * FROM fbtrendingdata')
		#print len(cur.fetchall())

		for row in cur.fetchall() :
			print row
			print row[0]
		'''
		db.commit()
	except:
		print "exception caught"
		print traceback.format_exc()
	finally:
		db.close()


#main('kkrtcgcgc',"kkr","h","dd","dd","dd","dd")