import imp
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.
class Customer(models.Model):
    # models.Model is a build in class allow us to connect to database easily
    # For Django class mean "Table"
    # datatype = "Property" in table
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # Use User as foriegn key
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=5)
    email = models.EmailField()
    # "python3.8 manage.py makemigrations" is used to generate sql
    # add 'myapp' in settings.py in myproject
    # don't forget to save each change

    def __str__(self):
        return "%s"%(self.user)

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
        print('update_profile_signal: create a profile')