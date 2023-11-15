from django.db import models
from datetime import datetime

# В этом файле создаём классы, описывающие структуры необходимых приложению таблиц

class Tasks(models.Model):
    # id создастся сам
    start = models.DateTimeField(default=datetime.now)
    end = models.DateField()
    description = models.CharField(max_length=256, default='')
    done = models.BooleanField(default=False)