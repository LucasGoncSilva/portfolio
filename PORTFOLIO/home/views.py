from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .context import skill_cards, project_cards


# Create your views here.
def index(req: HttpRequest) -> HttpResponse:
    if req.session.get("email_sent"):
        req.session["email_sent"] = False
        email_sent = True
    else:
        email_sent = False

    return render(
        req,
        "home/index.html",
        {
            "skill_cards": skill_cards,
            "project_cards": project_cards,
            "email_sent": email_sent,
        },
    )
