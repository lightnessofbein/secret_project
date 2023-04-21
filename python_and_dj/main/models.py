from django.db import models


class Task(models.Model):
    title = models.CharField('Title', max_length=50)
    text =  models.TextField('Text')

    def _str_(self):
        return self.title