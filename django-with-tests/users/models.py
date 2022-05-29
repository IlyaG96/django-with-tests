from django.db import models


class Dog(models.Model):
    name = models.CharField(
        'Имя',
        max_length=255,
    )
    breed = models.CharField(
        'Порода',
        max_length=255,
    )


class Owner(models.Model):
    name = models.CharField(
        'Имя',
        max_length=255,
    )
    dog = models.ForeignKey(
        Dog,
        verbose_name='собака',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='owner'
    )



