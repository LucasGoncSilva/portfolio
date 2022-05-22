from django.shortcuts import render
from django.core.mail import send_mail

from .contexts.skills import skill_cards
from .contexts.projects import project_cards
from .contexts.about_section import about_paragraphs
from PORTFOLIO.settings.base import EMAIL_HOST_USER, EMAIL_ADM


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            'Portfolio Contact Made',
            f'from: {name}\nemail: {email}\n\n\n{message}',
            EMAIL_HOST_USER,
            [EMAIL_ADM]
        )

        return render(request, 'home/index.html', {
            'skill_cards': skill_cards,
            'project_cards': project_cards,
            'about_paragraphs': about_paragraphs,
            'email_sent': True
        })

    return render(request, 'home/index.html', {
        'skill_cards': skill_cards,
        'project_cards': project_cards,
        'about_paragraphs': about_paragraphs,
        'email_sent': False
    })
