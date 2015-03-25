""" admin models """
from django.contrib import admin
from mail.models import Receiver, Mail
from mail.actions import send_mail_to_draft_action, send_mail_immediately_action


class ReceiverAdmin(admin.ModelAdmin):
    """ receiver admin"""
    list_display = ['mail_address', 'title', 'company_name']


class ReceiverInline(admin.TabularInline):
    """ Receiver inline admin """
    model = Mail.receivers.through


class MailAdmin(admin.ModelAdmin):
    """ mail admin """
    filter_horizontal = ['receivers']
    actions = [send_mail_to_draft_action(),
               send_mail_immediately_action()]

admin.site.register(Receiver, ReceiverAdmin)
admin.site.register(Mail, MailAdmin)
