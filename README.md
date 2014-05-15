i733.com
========

www.i733.com

tornado==3.2
SQLAlchemy==0.9.4
#pyDes==2.0.1
pycrypto==2.6.1


celery==3.1.11
billiard>=3.3.0.17,<3.4 (from celery)
billiard==3.3.0.17
kombu>=3.0.15,<4.0 (from celery)
kombu==3.0.16
anyjson>=0.3.3 (from kombu>=3.0.15,<4.0->celery)
anyjson==0.3.3
amqp>=1.4.5,<2.0 (from kombu>=3.0.15,<4.0->celery)
amqp==1.4.5

# from concurrent.futures import ThreadPoolExecutor 这个并发库在python3自带在python2需要安装sudo pip install futures
futures==2.1.6

 sudo pip install Motor
Downloading/unpacking Motor
  Downloading motor-0.2.tar.gz (99kB): 99kB downloaded
  Running setup.py egg_info for package Motor

Requirement already satisfied (use --upgrade to upgrade): tornado>=3.1 in /usr/local/lib/python2.7/dist-packages (from Motor)
Downloading/unpacking greenlet>=0.4.0 (from Motor)
  Downloading greenlet-0.4.2.zip (74kB): 74kB downloaded
  Running setup.py egg_info for package greenlet

Downloading/unpacking pymongo==2.7 (from Motor)
  Downloading pymongo-2.7.tar.gz (376kB): 376kB downloaded
  Running setup.py egg_info for package pymongo
