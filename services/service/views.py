# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def main(request):
    return HttpResponse("Witaj na stronie głównej")
