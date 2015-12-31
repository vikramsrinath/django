from django.db import models
from django.core.urlresolvers import reverse

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student_edit', kwargs={'pk': self.pk})
