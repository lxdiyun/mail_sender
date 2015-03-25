""" admin models """
from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from mail.models import Receiver, Mail
from mail.actions import send_mail_to_draft_action, send_mail_immediately_action


class ReceiverAdmin(ImportExportModelAdmin):
    """ receiver admin"""
    list_display = ['mail_address', 'title', 'company_name']


class ReceiverInline(admin.TabularInline):
    """ Receiver inline admin """
    model = Mail.receivers.through


class MailAdmin(ImportExportModelAdmin):
    """ mail admin """
    filter_horizontal = ['receivers']
    actions = [send_mail_to_draft_action(),
               send_mail_immediately_action()]

admin.site.register(Receiver, ReceiverAdmin)
admin.site.register(Mail, MailAdmin)
