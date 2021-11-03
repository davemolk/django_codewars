from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField


class Exercise(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    name = models.TextField("Kata name")
    slug = AutoSlugField("Kata Slug",
        unique=True, always_update=False, populate_from='name')
    cw_id = models.CharField("Codewars ID", max_length=255)
    languages = models.CharField("Langauges Used", max_length=255)
    description = models.TextField("Kata Description")
    tags = models.CharField("Kata Tags", max_length=255)
    rank = models.CharField("Kata Rank", max_length=255)
    url = models.URLField("Kata URL", null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('katas:detail', kwargs={'slug': self.slug})