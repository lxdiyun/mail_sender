"""mail models"""
from django.db import models
from django.core.urlresolvers import reverse

from jinja2 import Template

from tinymce.models import HTMLField


class Receiver(models.Model):
    """mail receiver"""
    mail_address = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    company_name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.company_name + ":" + self.title + "[" + self.mail_address +"]"


class Mail(models.Model):
    """mail content"""
    subject = models.CharField(max_length=1024)
    content = HTMLField()
    receivers = models.ManyToManyField('Receiver')

    def __unicode__(self):
        return self.subject

    def get_absolute_url(self):
        """url of the mail"""
        return reverse("mail_detail", kwargs={'pk': self.id})


def generate_mail(mail, receiver):
        template = Template(mail.content)
        html = template.render(obj=receiver)

        return html
