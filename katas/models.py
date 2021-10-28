from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField


class Exercise(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    name = models.CharField("Kata name", max_length=255)
    slug = AutoSlugField("Kata Slug",
        unique=True, always_update=False, populate_from='name')
    notes = models.TextField("Notes", blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('exercise_detail', kwargs={'slug': self.slug})