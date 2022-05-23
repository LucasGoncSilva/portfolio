from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

from PORTFOLIO.settings.base import EMAIL_HOST_USER, EMAIL_ADM


# Create your views here.
def mail(request: object) -> object:
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

        request.session['email_sent'] = True

    return HttpResponseRedirect(reverse('home:index'))