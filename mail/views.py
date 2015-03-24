""" mail app views"""

from django.http import Http404
from django.http import HttpResponse

from mail.models import Receiver, Mail, generate_mail_conent


def mail_demo_view(request, mail_id, receiver_id):
    """ final mail demo """
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

    if mail and receiver:
        return HttpResponse(generate_mail_conent(mail, receiver))
    else:
        raise Http404("mail or receiver not exist")
