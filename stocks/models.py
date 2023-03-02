from django.db import models

# Create your models here.
class Stock(models.Model):
     SECTOR_CHOICES = (
          ('TC', 'Technology'),
          ('BK', 'Banking'), 
          ('FS', 'Fashion'), 
          ('EG', 'Energy'), 
     )

     name = models.CharField(max_length=25, null=False, blank=False)
     ticket = models.CharField(max_length=10, null=False, blank=False)
     price = models.FloatField(null=False, blank=False)
     sector = models.CharField(max_length=2, choices=SECTOR_CHOICES, default='')


     def __str__(self) -> str:
          return f"{self.name} - {self.ticket}"
     
class RealEstateInvestmentTrust(models.Model):
     SECTOR_CHOICES = (
          ('LG', 'Logistics'),
          ('SH', 'Shopping'), 
          ('RS', 'Residential')
     )
     name = models.CharField(max_length=25, null=False, blank=False)
     ticket = models.CharField(max_length=10, null=False, blank=False)
     price = models.FloatField(null=False, blank=False)
     sector = models.CharField(max_length=2, choices=SECTOR_CHOICES, default='')
