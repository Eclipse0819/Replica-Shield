from django.db import models
from django import forms

# Create your models here.

class Response(models.Model):

    title           = models.CharField(max_length = 20)
    
    leader          = models.CharField(max_length = 50)
    leader_email    = models.EmailField()

    member2         = models.CharField(max_length = 50)
    member3         = models.CharField(max_length = 50, blank = True)
    member4         = models.CharField(max_length = 50, blank = True)

    abstract        = models.TextField()


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['title', 'leader', 'leader_email', 'member2',
                  'member3', 'member4', 'abstract']
        