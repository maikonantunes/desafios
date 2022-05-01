from django.db import models


# Create your models here.

class Task(models.Model):
    STATUS_TASK = [
        ('CONCLUIDO', 'Concluido'),
        ('AGENDADO', 'Agendado')]
    status_task = models.CharField(choices=STATUS_TASK, default='AGENDADO', max_length=250)
    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
