import smtplib
import time

from email.mime.text import MIMEText
mail_boby='hello.this is the mail content'
mail_from='yzxm365@sina.cn'
mail_to=['yzxm365@163.com']
msg=MIMEText(mail_boby)
msg['Subject']='this is the title'
msg['From']=mail_from
msg['To']=';'.join(mail_to)
msg["date"]=time.strftime('%a, %d %b %Y %H:%M:%S %z')
time.strftime('%a, %d %b %Y %H:%M:%S %z')
msg["date"]=time.strftime('%a, %d %b %Y %H:%M:%S %z')
smtp=smtplib.SMTP()
smtp.connect("smtp.sina.cn")
smtp.login('yzxm365@sina.cn','zm520Y')
smtp.sendmail(mail_from,mail_to,msg.as_string())
smtp.quit()
print ('ok')
