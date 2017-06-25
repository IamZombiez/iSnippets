from django.db import models

# Create your models here.
class SnippetForm(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    language = models.CharField(max_length=32, blank=False, null=False)
    code = models.CharField(max_length=256, blank=False, null=False)
    descript = models.CharField(max_length=256, blank=False, null=False)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s by %s' % (self.title, self.language)
