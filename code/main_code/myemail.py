#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'dalton'

import smtplib
import email.utils


def sendemail(subject, text):
    fromaddr = 'bigdatadawgs@gmail.com'
    toaddrs  = 'bigdatadawgs@gmail.com'
    subject = subject
    text = text
    msg = 'Subject: %s\n\n%s' % (subject, text)


    # Credentials (if needed)
    username = 'bigdatadawgs'
    password = '3VJkf2CPAiJgVk'

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()