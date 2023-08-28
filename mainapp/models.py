from django.db import models

class Ideas(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, default='Anonymous')
    idea = models.TextField()

    class Meta:
        ordering = ('created',)