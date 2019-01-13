import smtplib
from email.mime.text import MIMEText
from email.header    import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication



from setting import *


print(server,port)
smtpObj = smtplib.SMTP(server, port)
print(smtpObj.starttls())
smtpObj.login(login,passw)


file=open("data.csv","r",encoding='utf-8')
dat=file.read().split('\n')
file.close()
head=dat[0].split(',')
dat.pop(0)

data=[]
for i in dat:
    data.append(i.split(','))
file=open("text.txt",'r')
text = file.read()
file.close()
#out=[]
for lin in data:
    fiel=""
    mail=""
    tmail=text
    i=0
    while i<len(lin):
        if head[i]=='!@':
            mail=lin[i]
            i+=1
            continue
        if head[i]=='!F':
            fiel=lin[i]
            i+=1
            continue
        tmail= tmail.replace(head[i],lin[i])
        i+=1
    if fiel=="":
        msg = MIMEText(tmail, 'plain', 'utf-8')
        msg['Subject'] = Header('Регистрация', 'utf-8')
        msg['From'] = login
        msg['To'] = mail
        smtpObj.sendmail(login,mail,msg.as_string())
    else:
        msg = MIMEMultipart()
        
        msg['Subject'] = 'Регтстрация'
        msg['From'] = login
        msg['To'] = mail
        msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'
        attach = MIMEApplication (open(fiel, 'rb').read())
        attach.add_header ('Content-Disposition', 'attachment', filename=fiel)
        part1 = MIMEText(tmail, 'plain')
        msg.attach (attach)
        msg.attach(part1)
        
        smtpObj.sendmail(login,mail,msg.as_string())
#print(out)

print("end")
smtpObj.quit()