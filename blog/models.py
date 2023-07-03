from django.db import models

class Blog(models.Model):  # Use capitalized name for the model
    title = models.CharField(max_length=60)
    post = models.CharField(max_length=200)

    def __str__(self):
        return self.title
