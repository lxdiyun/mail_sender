""" mail app views"""

from django.http import Http404
from django.http import HttpResponse

from mail.models import Receiver, Mail, generate_mail


def mail_demo_view(request, mail_id, receiver_id):
    """ final mail demo """
    mail = None
    receiver = None

    if mail_id:
        mail = Mail.objects.get(pk=mail_id)

    if receiver_id:
        receiver = Receiver.objects.get(pk=receiver_id)

    if mail and receiver:
        return HttpResponse(generate_mail(mail, receiver))
    else:
        return Http404("mail or receiver not exist")
