""" mail app action model """
import imaplib
import smtplib
import time

from django.conf import settings

from mail.models import generate_mail


def send_mail_to_draft_action():
    """ send mail to draft action """
    def send_mail_to_draft(modeladmin, request, queryset):
        """ send mails to draft folder action """
        emails = list()
        for mail in queryset:
            for receiver in mail.receivers.all():
                email = generate_mail(mail, receiver)
                emails.append(email)

        send_mail_to_folder('Drafts', emails)

    send_mail_to_draft.short_description = "send emails to draft"

    return send_mail_to_draft


def send_mail_to_folder(folder, emails):
    """ upload emails to sepecial folder """
    imap = imaplib.IMAP4_SSL('imap.qq.com')
    imap.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    try:
        for email in emails:
            imap.append(folder,
                        '',
                        imaplib.Time2Internaldate(time.time()),
                        str(email))
    finally:
        try:
            imap.close()
        except:
            pass

    imap.logout()


def send_mail_immediately_action():
    """ send mail immediatley action """
    def send_mail_immediately(modeladmin, request, queryset):
        """ send mails immediatley """
        emails = list()
        for mail in queryset:
            for receiver in mail.receivers.all():
                email = generate_mail(mail, receiver)
                emails.append(email)

        send_mail_by_smtp(emails)

    send_mail_immediately.short_description = "send emails immediatley"

    return send_mail_immediately


def send_mail_by_smtp(emails):
    """ send email by smtp immediatley """
    smtp = smtplib.SMTP_SSL('smtp.qq.com')
    smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    try:
        for email in emails:
            smtp.sendmail(email["From"], [email["To"]], str(email))
    finally:
        pass

    smtp.quit()
