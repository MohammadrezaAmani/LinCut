from django.db import models


class Link(models.Model):
    link = models.CharField(max_length=255)
    description = models.TextField(max_length=511, blank=True, null=True)
    owner = models.ForeignKey(
        "auth.User", related_name="snippets", on_delete=models.CASCADE
    )
    shortedLink = models.CharField(max_length=255)
    viewcount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.owner + " | " + self.link

    def __repr__(self) -> str:
        return self.owner + " | " + self.link
