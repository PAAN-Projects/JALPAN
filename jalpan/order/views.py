from re import template
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def index(request):
    template = loader.get_template("order.html")
    return HttpResponse(template.render())
