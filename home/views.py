from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

from .contexts.skills import skill_cards
from .contexts.projects import project_cards
from .contexts.about_section import about_paragraphs
from PORTFOLIO.settings.base import EMAIL_HOST_USER, EMAIL_ADM


# Create your views here.
def index(request: object) -> object:
    if request.session.get('email_sent') == True:
        request.session['email_sent'] = False
        email_sent = True
    else:
        email_sent = False

    return render(request, 'home/index.html', {
        'skill_cards': skill_cards,
        'project_cards': project_cards,
        'about_paragraphs': about_paragraphs,
        'email_sent': email_sent
    })


def mail(request: object) -> object:
    if request.method == 'POST':
        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # message = request.POST.get('message')

        # send_mail(
        #     'Portfolio Contact Made',
        #     f'from: {name}\nemail: {email}\n\n\n{message}',
        #     EMAIL_HOST_USER,
        #     [EMAIL_ADM]
        # )

        request.session['email_sent'] = True

        return HttpResponseRedirect(reverse('home:index'))

    return HttpResponseRedirect(reverse('home:index'))