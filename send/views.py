import smtplib
import email.message
from django.http import HttpResponseRedirect
from django.urls import reverse

from PORTFOLIO.settings.base import EMAIL_HOST_USER, EMAIL_ADM, EMAIL_HOST_PASSWORD


# Create your views here.
def contact_adm(subject: str, body: str) -> None:
    msg = email.message.Message()

    msg['From'] = EMAIL_HOST_USER
    password = EMAIL_HOST_PASSWORD
    msg['To'] = EMAIL_ADM

    msg.add_header('Content-Type', 'text/html')
    msg['Subject'] = subject
    msg.set_payload(body)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()    
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))


def mail(request: object) -> object:
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = str(request.POST.get('message'))

        message = message.replace('\n', '<br>')

        contact_adm(
            'Portfolio Contact Made',
            f'<p>from: {name}</p><p>email: {email}</p><br>_____<p>{message}</p>_____',
        )

        request.session['email_sent'] = True

    return HttpResponseRedirect(reverse('home:index'))
