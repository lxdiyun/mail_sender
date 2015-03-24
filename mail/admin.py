""" admin models """
from django.contrib import admin
from mail.models import Receiver, Mail


class ReceiverAdmin(admin.ModelAdmin):
    """ receiver admin"""
    list_display = ['mail_address', 'title', 'company_name']


class ReceiverInline(admin.TabularInline):
    """ Receiver inline admin """
    model = Mail.receivers.through


class MailAdmin(admin.ModelAdmin):
    """ mail admin """
    filter_horizontal = ['receivers']

admin.site.register(Receiver, ReceiverAdmin)
admin.site.register(Mail, MailAdmin)
