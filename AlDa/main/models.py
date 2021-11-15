from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum



class SubJobs(models.Model):
    Name = models.CharField('Название', max_length=255)
    CostForOne = models.DecimalField('Цена ед. без НДС', blank=False, null=False, max_digits=19, decimal_places=2)
    Quantity = models.BigIntegerField('Кол-во')
    DateOfContract = models.DateField(null=True)

    def __str__(self):
        return self.Name

    def CounterPartyes(self):
        return CounterParty.objects.filter(Accreditation=self).all()

    def SumValue(self):
        return CounterParty.objects.filter(Accreditation=self).aggregate(Sum('Value'))

    def Multyplay(self):
        return self.CostForOne * self.Quantity

    def Expired(self):
        return timezone.now().date() > self.DateOfContract

    def OneWeekExpired(self):
        return (timezone.now().date() + timedelta(days=7)) >= self.DateOfContract


class CounterParty(models.Model):
    Name = models.CharField('Название', max_length=255, null=True)
    Accreditation = models.ManyToManyField(SubJobs, null=True, blank=True)
    Hired = models.BooleanField(default=False)
    Value = models.DecimalField('Объем', blank=True, null=True, max_digits=19, decimal_places=2)


    def __str__(self):
        return self.Name


class Jobs(models.Model):
    Name = models.CharField('Название', max_length=255)
    CategoryOfWork = models.ManyToManyField(SubJobs, null=True, blank=True)

    def __str__(self):
        return self.Name


class PassportOfObject(models.Model):
    Name = models.CharField('Название', max_length=255)
    Jobs = models.ManyToManyField(Jobs, null=True, blank=True)

    def __str__(self):
        return self.Name





    # Create your models here.
