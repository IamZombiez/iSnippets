from django import forms

class UserForm(forms.Form):

    title = models.CharField(max_length=128)
    language = models.CharField(max_length=32)
    code = models.CharField(max_length=256)
    descript = models.CharField(max_length=256)
