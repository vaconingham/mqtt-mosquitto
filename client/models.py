# from django.db import models

# class MQTTClient(models.Model):
#     client_id = models.BigAutoField(primary_key=True, blank=False, unique=True)
#     client_name = models.CharField(max_length=128, blank=False)
#     clean_session = models.BooleanField(default=True)
#     userdata = models.CharField(default='none', max_length=1024, blank=True)
#     client_description = models.CharField(max_length=1024, blank=True)
#     client_serial_number = models.CharField(max_length=128, blank=True)
#     client_mac_address = models.CharField(max_length=128, blank=True)

#     def __str__(self):
#         return self.name


# class DataOutput(models.Model):
#     timestamp = models.DateTimeField(auto_now_add=True)
#     current_value = models.FloatField(blank=True)
#     one_minute_average = models.FloatField(blank=True)
#     five_minute_average = models.FloatField(blank=True)
#     thirty_minute_average = models.FloatField(blank=True)

#     def __str__(self):
#         return self.pk
