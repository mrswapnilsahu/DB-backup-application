import os
import datetime
import time

dbhost = 'localhost'
dbuser = 'testuser'
dbpassword = 'test123'
dbname = 'testdb'
# tab1 = 'patient'
# tab2 = 'patho_allot_test'
# tab3 = 'pay_boucher'
# tab4 = 'ipd_admit'
# tab5 = 'casualty'
# tab6 = 'pd_invoice'
# tab7 = 'pd_invoice_cr_scheme'
# tab8 = 'pd_invoice_ret'
# tab9 = 'smcard_topup'
# tab10 = 'pd_receipt'
# tab11 = 'account_voucher'
# tab12 = 'account_vouchpay'
# tab13 = 'acc_generatedchq'
# tab14 = 'hr_adv'
# tab15 = 'overt_assign'
# tab16 = 'hr_adv_emi_details'
# tab17 = 'pd_transaction'
# tab18 = 'transaction_bill'
# tab19 = 'smcard_topup'
# tab20 = 'pd_invoice_cr'
# tab21 = 'pd_transaction_scheme'
# tab22 = 'acc_generatedchq'

backup = 'db_backup/'

datetime = time.strftime('%d%m%Y%H%M%S')

todaybackup = backup + datetime

os.mkdir(todaybackup)

os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + " > " + todaybackup + "/" + dbname + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab2 + " > " + todaybackup + "/" + tab2 + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab3 + " > " + todaybackup + "/" + tab3 + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab4 + " > " + todaybackup + "/" + tab4 + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab5 + " > " + todaybackup + "/" + tab5 + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab6 + " > " + todaybackup + "/" + tab6 + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab7 + " > " + todaybackup + "/" + tab7 + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab8 + " > " + todaybackup + "/" + tab8 + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab9 + " > " + todaybackup + "/" + tab9 + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab10 + " > " + todaybackup + "/" + tab10 + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab11 + " > " + todaybackup + "/" + tab11 + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab12 + " > " + todaybackup + "/" + tab12 + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab13 + " > " + todaybackup + "/" + tab13 + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab14 + " > " + todaybackup + "/" + tab14 + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab15 + " > " + todaybackup + "/" + tab15 + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab16 + " > " + todaybackup + "/" + tab16 + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab17 + " > " + todaybackup + "/" + tab17 + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab18 + " > " + todaybackup + "/" + tab18 + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab19 + " > " + todaybackup + "/" + tab19 + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab20 + " > " + todaybackup + "/" + tab20 + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab21 + " > " + todaybackup + "/" + tab21 + ".sql")
# os.system("mysqldump -h " + dbhost + " -u " + dbuser + " -p" + dbpassword + " " + dbname + tab22 + " > " + todaybackup + "/" + tab22 + ".sql")

print("backup created in: " + todaybackup)
