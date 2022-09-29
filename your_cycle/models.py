from django.db import models

# Create your models here.

class Cycle(models.Model):
    
    title = models.CharField(max_length=500)
    article = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title
