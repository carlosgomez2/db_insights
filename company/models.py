from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return u'/company/%d' % self.id
