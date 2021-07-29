from django.db import models
import datetime

dob = models.DateField(max_length=8)
age = models.IntegerField()


def __str__(self):
    today = date.today()
    age = today.year - dob.year
    if today.month < dob.month or today.month == dob.month and today.day < dob.day:
        age -= 1
    return self.age
