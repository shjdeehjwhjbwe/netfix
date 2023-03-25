from django.db import models
import rest_framework


class Actor(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    xxx = (
        (MALE, 'male'),
        (FEMALE, 'female')
    )
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True , null=True)
    brithdate = models.DateField( blank=True)
    gender = models.CharField(choices=xxx, max_length=450)
    avatar = models.URLField(blank=True)

    def __str__(self):
        return self.first_name
