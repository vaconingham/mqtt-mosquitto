from django.shortcuts import render

def index(request):
    return render(request, 'client/index.html')

def client(request, client_name):
    return render(request, 'client/client.html', {
        'client_name': client_name
    })