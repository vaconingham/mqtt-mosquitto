from django.db import models
import uuid

def new_uuid():
    return uuid.uuid4()

class Client(models.Model):
    client_name = models.UUIDField(primary_key=True, default=new_uuid, blank=False, unique=True)
    clean_session = models.BooleanField(default=True)
    userdata = models.CharField(default='none', max_length=1024, blank=True)
    client_description = models.CharField(max_length=1024, blank=True)
    client_serial_number = models.CharField(max_length=128, blank=True)
    client_mac_address = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return str(self.client_name)


class DataOutput(models.Model):
    client_id = models.ForeignKey(Client, related_name='data_output', on_delete=models.CASCADE, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    current_value = models.FloatField(blank=True)
    one_minute_average = models.FloatField(blank=True)
    five_minute_average = models.FloatField(blank=True)
    thirty_minute_average = models.FloatField(blank=True)

    def __str__(self):
        return self.timestamp
