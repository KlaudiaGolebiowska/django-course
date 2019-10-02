from django.db import models


class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=100)
    text = models.TextField()

    def contains(self, word):
        return word in self.text

    def __str__(self):
        return self.title
