from django import forms

class UserForm(forms.Form):

    title = models.CharField(label='title', max_length=128)
    language = models.CharField(label='language', max_length=32)
    code = models.CharField(label='code', max_length=256)
    descript = models.CharField(label='descript', max_length=256)
