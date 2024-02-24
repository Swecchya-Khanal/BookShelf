from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20) 
    desc = models.TextField()
    date = models.DateField(auto_now_add=True) 

    def __str__(self):
        return self.name
