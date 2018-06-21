from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("Hey dude. You are at the polls index.")
