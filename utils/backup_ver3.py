#!/usr/bin/python
#Filename: backup_ver3.py

import os
import time

#1.The files and directories to be backed up are specified in a list.
source = [' /home/leo/Documents/upload', ' /home/leo/Documents/download']
#If you are using Windows, use source = [r'C:\upload', r'C:\download'] or something like that

#2.The backup must be stored in a main backup directory
target_dir = '/home/leo/Documents/backup' #Remember to change this to what you will be using

#3.The files are backed up into a zip file.
#4.The name of the zip archive is the current date and time
today = target_dir + time.strftime('%Y%m%d')
#The current time is the name of the zip archive
now = time.strftime('%H%M%S')

comment = raw_input('Enter a comment -->')
print comment
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace('','_') + '.zip'

#Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today) #make directory
    print 'Successfully created directory', today

#The name of the zip file
#target = today + os.sep + now + '.zip'


#5.We use the zip commmand(in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr '%s' %s" % (target,''.join(source))

print zip_command

#Run the backup

if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'
