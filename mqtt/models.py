from django.db import models


class Client(models.Model):
    client_name = models.CharField(
        primary_key=True, 
        max_length=255, 
        blank=False, 
        unique=True
        )
    clean_session = models.BooleanField(default=True)
    userdata = models.CharField(default='none', max_length=1024, blank=True)
    client_description = models.CharField(max_length=1024, blank=True)
    client_serial_number = models.CharField(max_length=128, blank=True)
    client_mac_address = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return str(self.client_name)


class DataOutput(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    client_id = models.ForeignKey(
        Client, 
        related_name='data_output', 
        on_delete=models.CASCADE, 
        blank=True, 
        editable=False
        )
    data_timestamp = models.CharField(max_length=50, blank=True)
    current_value = models.FloatField(blank=True)
    one_minute_average = models.FloatField(blank=True)
    five_minute_average = models.FloatField(blank=True)
    thirty_minute_average = models.FloatField(blank=True)

    def __str__(self):
        return str(self.client_id) + ' ' + str(self.data_timestamp)
