import smtplib
import time

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

#创建实例，构造MIMEMulipart对象为根容器
msg=MIMEMultipart()
#正文
mail_boby='hello.this is the mail content'
#发信邮箱
mail_from='yzxm365@sina.cn'
#收信邮箱
mail_to=['yzxm365@163.com']

#msg=MIMEText(mail_boby)
#定义标题
msg['Subject']=u'this is the title'
#定义发信人
msg['From']=mail_from
msg['To']=';'.join(mail_to)
msg["date"]=time.strftime('%a, %d %b %Y %H:%M:%S %z')
time.strftime('%a, %d %b %Y %H:%M:%S %z')
msg["date"]=time.strftime('%a, %d %b %Y %H:%M:%S %z')

#定义正文
txt=MIMEText(u'中文内容','plain','utf-8')
msg.attach(txt)
#图片路径
picfiles=[r'C:\Users\te3030\Desktop\33\1.png']
for file in picfiles:
    f=open(file,'rb')
    img=MIMEImage(f.read())
    f.close()
    msg.attach(img)
    
smtp=smtplib.SMTP()
smtp.connect("smtp.sina.cn")
smtp.login('yzxm365@sina.cn','zm520Y')
smtp.sendmail(mail_from,mail_to,msg.as_string())
smtp.quit()
print ('ok')
