"""urlconf for the mail application"""

from django.conf.urls import url, patterns
from django.views.generic import DetailView
from mail.models import Mail


urlpatterns = patterns('',
                       url(r'^mail/(?P<pk>\d+)$',
                           DetailView.as_view(model=Mail), name="mail_detail"),
                       url(r'^mail/(?P<mail_id>\d+)/(?P<receiver_id>\d+)$',
                           'mail.views.mail_demo_view', name="mail_demo")
                       )
