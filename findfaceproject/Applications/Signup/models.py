from django.db import models

# Create your models here.

class Subscriber(models.Model):

    email = models.EmailField()
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    #joined_in = models.DateField()

    def __str__(self):
        return self.username

    def __str__for_email(self):
        return self.email

    def __str__for_password(self):
        return self.password

    @models.permalink
    def get_absolute_url(self):
        return ('subscriner_details', (), {'email': self.email,
                                     'username': self.username,
                                     'password': self.password})




