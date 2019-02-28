from logging import Manager

from django.db import models

class  Animal(models.Model):
    name = models.CharField(max_length=40)
    color = models.CharField(max_length=100)


    # 设置成抽象化,
    class  Meta:
        abstract = True



class  Cat(models.Model):
    # name = models.CharField(max_length=40)
    # color = models.CharField(max_length=40)
    eat = models.CharField(max_length=100)


class  Dog(models.Model):
    # name = models.CharField(max_length=40)
    # color = models.CharField(max_length=100)
    eat = models.CharField(max_length=100)
    sleep = models.CharField(max_length=100)


class  Fish(models.Model):
    # name = models.CharField(max_length=40)
    # color = models.CharField(max_length=100)
    swim = models.CharField(max_length=100)


class  Snake(models.Model):
    # name = models.CharField(max_length=40)
    # color = models.CharField(max_length=100)
    sleep = models.CharField(max_length=100)
