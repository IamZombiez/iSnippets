from django.db import models

# Create your models here.
class SnippetForm(models.Model):
    title = models.CharField(max_length=128)
    language = models.CharField(max_length=32)
    code = models.CharField(max_length=256)
    descript = models.CharField(max_length=256)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s by %s' % (self.title, self.language)
