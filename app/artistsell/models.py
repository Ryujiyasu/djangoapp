from django.db import models


class Artistsell(models.Model):
    id = models.BigAutoField(primary_key=True)
    artist_name = models.CharField(max_length=50)
    item = models.CharField(max_length=50)
    count=models.IntegerField()
    price=models.IntegerField()
    princesum=models.IntegerField()
    service_type=models.CharField(max_length=50)
    sell_type=models.CharField(max_length=50)
    date=models.DateField()