from django.http import HttpResponse

def index(request) -> HttpResponse:
    return HttpResponse("Hello, world. You're ath the polls index.")
