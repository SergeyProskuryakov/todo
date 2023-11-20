from django.db import models
from datetime import datetime

# В этом файле создаём классы, описывающие структуры необходимых приложению таблиц

class Tasks(models.Model):
    # id создастся сам
    start = models.DateTimeField(default=datetime.now)
    end = models.DateTimeField()
    description = models.CharField(max_length=256, default='')
    done = models.BooleanField(default=False)

    def __str__ (self):
        return str(self.description)
    
class Categories(models.Model):
    description = models.CharField(max_length=256, default='')
    urgently = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    optional = models.BooleanField(default=False)
    entertainments = models.BooleanField(default=False)

    def __str__ (self):
        return str(self.description)