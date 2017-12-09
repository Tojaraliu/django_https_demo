from django.shortcuts import render
from django.http import HttpResponse

def helloworld(request):
    info = {'sessionkey': request.session.session_key}
    return render(request, 'index.html', info)