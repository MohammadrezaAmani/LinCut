from django.db import models

class Link(models.Model):
    link = models.CharField(max_length=255)
    description = models.TextField(max_length=511, blank=True, null=True)
    owner = models.CharField(max_length=255)
    shortedLink = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.owner + ' | ' + self.link
    
    def __repr__(self) -> str:
        return self.owner + ' | ' + self.link