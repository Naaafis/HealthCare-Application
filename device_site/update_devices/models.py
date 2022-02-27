from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

    
class Device(models.Model):
    device_id = models.IntegerField(unique= True, default = None)
    device_type = models.CharField(max_length=255 )
    device_mac = models.CharField( max_length=255 )
    device_firmware_version = models.CharField(max_length=255 )
    device_software_version = models.CharField(max_length=255 )
    def __str__(self):
        return self.device_type
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    
class User(models.Model):
    associated_device = models.ForeignKey(Device, on_delete=models.CASCADE)
    user_name = models.CharField(max_length = 255, unique = True, default = None, blank=True)
    date_assigned = models.DateTimeField('Date Assigned')
    def __str__(self):
        return self.user_name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Data_Collection(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    #device_type = models.CharField(max_length=255)
    collection_reason = models.CharField(max_length=255)
    data_collected = models.IntegerField()
    time_collected = models.DateTimeField('Date Collected')
    def __str__(self):
        return self.collection_reason
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    

    