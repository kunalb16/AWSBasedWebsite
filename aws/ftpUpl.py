#!/usr/bin/env python
import socket
import ftplib
import os
def uploadFileToFtp(filename="C:\\Users\\kubansal\\Desktop\\test.png"):
        host = socket.gethostbyname("www.wobka.com")
	try:
		logFtpSession = ftplib.FTP(host)
	except (socket.error, socket.gaierror), e:
		print 'ERROR: cannot reach "%s"' % "a"
		return
	#print '*** Connected to host "%s"' % "a"
	try:
		logFtpSession.login("kunalbansalftp@wobka.com", password)
	except ftplib.error_perm, e:
		print 'ERROR: cannot login'
		logFtpSession.quit()
		return
	#print '*** Logged in successfully'
	
	try:
		logFile = open(filename,'rb')                  
		logFtpSession.storbinary(('STOR '+filename), logFile) 
		#print("#File Uploaded#"),
		logFile.close()                                   
		logFtpSession.quit()
		os.remove(filename)
	except:
		import traceback
		print traceback.format_exc()
		print "Exception caught in uploading file"

	
#uploadFileToFtp()
