from django.shortcuts import render

from .contexts.skills import skill_cards
from .contexts.projects import project_cards
from .contexts.about_section import about_paragraphs


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