from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from google.appengine.api import mail


class HomeView(TemplateView):
    template_name = "home.html"

    def post(self, request, *args, **kwargs):
        mail.send_mail(
            sender="%s <%s>" % (request.POST.get('your-name'), request.POST.get('your-email')),
            to="Ajith Kumar <ajithwinds+profile@gmail.com>",
            subject="%s has sent you a message from your profile website" % request.POST.get('your-name'),
            body="""
Dear Ajith,

Company: %s

Website: %s

The message:

%s

Your Profile.
""" % (request.POST.get('company'), request.POST.get('website'), request.POST.get('message')))

        return HttpResponseRedirect(reverse('home'))
