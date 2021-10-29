from django.db import models
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=255)
    cw_id = models.CharField(max_length=255, null=True)
    languages = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    tags = models.CharField(max_length=255, null=True)
    rank = models.CharField(max_length=255, null=True)
    url = models.URLField(null=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])