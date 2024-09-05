from smtplib import SMTP
from email.message import Message

from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.urls import reverse
from django.conf import settings

from send.models import WakeDatabase


# Create your views here.
def contact_adm(subject: str, body: str) -> None:
    msg: Message = Message()

    msg["From"] = str(settings.EMAIL_HOST_USER)
    password: str = str(settings.EMAIL_HOST_PASSWORD)
    msg["To"] = str(settings.EMAIL_ADM)

    msg.add_header("Content-Type", "text/html")
    msg["Subject"] = subject
    msg.set_payload(body)

    s: SMTP = SMTP("smtp.gmail.com: 587")
    s.starttls()
    s.login(msg["From"], password)
    s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))


def mail(req: HttpRequest) -> HttpResponseRedirect:
    if req.method == "POST":
        name: str = str(req.POST.get("name"))
        email: str = str(req.POST.get("email"))
        message: str = (
            str(req.POST.get("message"))
            .replace("\n", "<br>")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )

        contact_adm(
            "Portfolio Contact Made",
            f"<p>from: {name}</p><p>email: {email}</p><br>_____<p>{message}</p>_____",
        )

        req.session["email_sent"] = True

    return HttpResponseRedirect(reverse("home:index"))


def wake_db(req: HttpRequest) -> HttpResponse:
    WakeDatabase.objects.create()

    e = WakeDatabase.objects.all()
    if e.count() > 3:
        e.delete()
    return HttpResponse(e.count())
