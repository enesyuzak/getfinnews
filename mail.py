# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 20:44:37 2020

@author: enesy
"""



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


class mail:


    def send_mail(subject,message):
        
        msg=MIMEMultipart()
        msg['from']="enesyuzak@yandex.com"
        msg['to']="mobile.android.tr@gmail.com"
        msg['subject']=subject
        
        msg_setting=MIMEText(message,"plain")
        msg.attach(msg_setting)
        
        try:
            mail=smtplib.SMTP("smtp.yandex.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login("enesyuzak@yandex.com","yanEg-167010")
            mail.sendmail(msg["from"],msg["to"],msg.as_string())
            print("Mail gönderildi")
            
        except:
            print("Hata: ", sys.exc_info()[0])
    
        finally:
            mail.close()

