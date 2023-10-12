from django.db import models

class Vacancy(models.Model):
    company = models.CharField(max_length=100)
    programming_language = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=[
        ('Senior', 'Senior'),
        ('Middle', 'Middle'),
        ('Junior', 'Junior')
    ])
    def __str__(self):
        return self.company