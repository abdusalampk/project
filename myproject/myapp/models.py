from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='comedy')
    desc=models.TextField()

    def __str__(self):
        return self.name
class mentor(models.Model):
    name=models.CharField(max_length=250)
    place=models.TextField()
    img=models.ImageField(upload_to='ooty derox')

    def __str__(self):
        return self.name