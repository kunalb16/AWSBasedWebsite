README 

** Quick summary**

* Website to get latest news from everywhere

**AWS SETUP**
* You would need to setup an Amazon EC2, Amazon S3, Amazon RDS and Security profiles related to them.

**SETUP Requirements ON Ubuntu AWS**

* http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html
* http://winscp.net/eng/docs/guide_amazon_ec2
* sudo wget https://ftp.mozilla.org/pub/mozilla.org/firefox/releases/23.0b10/linux-x86_64/en-US/firefox-2 3.0b10.tar.bz2
* http://www.cyberciti.biz/faq/howto-install-firefox-15-0-tar-bz2-in-linux/
* sudo yum install gcc
* sudo apt-get update
* sudo apt-get upgrade
* sudo apt-get install python-pip
* sudo apt-get install python-setuptools
* sudo apt-get install libjpeg-dev
* sudo apt-get install xvfb / sudo yum install xorg-x11-server-Xvfb.x86_64 (use yum search xvfb)
* sudo easy_install pyvirtualdisplay
* sudo apt-get install python-dev
* sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk

* sudo pip install pillow
* sudo apt-get install libmysqlclient-dev
*  sudo easy_install  MySQLdb / (use yum list \*mysql\* | grep dev to find and install close to mysql-devel.x86_64 name)
* easy_install unidecode
* http://stackoverflow.com/questions/20753607/while-upgrading-python-imaging-library-pil-it-tells-me-jpeg-support-not-avai
* http://raspberrypi.stackexchange.com/questions/9361/how-do-i-enable-jpeg-support-with-pil
* http://stackoverflow.com/questions/20060096/installing-pil-with-pip
* sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
* sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
* sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib
* sudo ln -s /usr/lib/arm-linux-gnueabihf/libjpeg.so /usr/lib
* http://www.chrishjorth.com/blog/free-aws-ec2-ubuntu-apache-php-mysql-setup/
 
**How to run**
* Start fb.py.(Might need to upgrade credentials a bit)
