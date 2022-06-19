# from doctest import OutputChecker
from django.shortcuts import get_object_or_404, render
from . import mqtt as client
from .models import Client, DataOutput


def index(request):
    return render(request, 'mqtt/index.html')

def client(request, client_name):
    data = DataOutput.objects.filter(client_id=client_name).latest('timestamp')
    client = get_object_or_404(Client, client_name=client_name)
    return render(request, 'mqtt/client.html',{
        'client': client,
        'client_name': client_name,
        'data': data
        })