import os
import datetime
import time

#YOUR DB HOST
dbhost = 'DB_HOST'
#YOUR DB USER
dbuser = 'DB_USER'
#YOUR DB PASSWORD
dbpassword = 'DB_PASSWORD'
#YOUR DB NAME
dbname = 'DB_NAME'
#YOUR TABLE NAME
tablename = 'TABLE_NAME'

#PATH WHERE YOU WANT TO STORE YOUR BACKUP
backup = 'db_backup/'

datetime = time.strftime('%d%m%Y%H%M%S')

todaybackup = backup + datetime

os.mkdir(todaybackup)

os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tablename + " > " + todaybackup + "/" + tablename + ".sql")

print("backup created in: " + todaybackup)
