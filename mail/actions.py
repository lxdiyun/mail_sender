""" mail app action model """
import imaplib
import time

from django.conf import settings

from mail.models import generate_mail, Mail, Receiver


def send_mail_to_draft(mail_id, receiver_id):
    if mail_id:
        try:
            mail = Mail.objects.get(pk=mail_id)
        except Mail.DoesNotExist:
            mail = None

    if receiver_id:
        try:
            receiver = Receiver.objects.get(pk=receiver_id)
        except Receiver.DoesNotExist:
            receiver = None
    email = generate_mail(mail, receiver)
    print email

    imap = imaplib.IMAP4_SSL('imap.qq.com')
    imap.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    try:
        imap.append('Drafts', 
                    '', 
                    imaplib.Time2Internaldate(time.time()),
                    str(email))
    finally:
        try:
            imap.close()
        except:
            pass

    imap.logout()
