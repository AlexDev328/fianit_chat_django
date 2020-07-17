from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    def __str__(self):
        return self.name+' '+self.city


class Message(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET("none"), default=1)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
