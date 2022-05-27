from django.shortcuts import get_object_or_404, render
import client1, client2

from .models import Client

def index(request):
    return render(request, 'client/index.html')

def client(request, client_name):
    client = get_object_or_404(Client, client_name=client_name)
    return render(request, 'client/client.html',{
        'client': client,
        'client_name': client_name
        })