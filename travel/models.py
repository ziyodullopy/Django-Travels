from django.db import models
from  django_countries.fields import CountryField
from django.contrib.auth.models import User

class LogoutModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timelogout = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
    
class LoginModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    timelogin = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

class RegisterModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    timereg = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username
    
class Places(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    country = CountryField()
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()


    def __str__(self):
        return self.name

class PlaceDetail(models.Model):
    place = models.ForeignKey(Places, on_delete=models.CASCADE, related_name='details')
    guide_price = models.IntegerField()
    taxi_price = models.IntegerField()
    food_price = models.IntegerField()
    
    def __str__(self):
        return self.place.name
    
    class Meta:
        verbose_name = 'Place Detail'
        verbose_name_plural = 'Place Details'


class OrderPlaces(models.Model):
    place = models.ForeignKey(Places, on_delete=models.SET_NULL, null=True, related_name='orders')
    phone_number = models.IntegerField(default=998)
    full_name = models.CharField(max_length=200)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Order Place"
        verbose_name_plural = "Order Place"


class Gallarey(models.Model):
    place = models.ForeignKey(Places, on_delete=models.CASCADE, related_name='gallarey', null=True)

    def __str__(self):
        return f"{self.place.name} Gallarey"

class TravelGallarey(models.Model):
    gallarey = models.ForeignKey(Gallarey, on_delete=models.CASCADE, related_name='travel_gallarey', null=True)
    img = models.ImageField(null=True)

    def __str__(self):
        return f"{self.gallarey.place.name} TravelGallarey"
    
class ContactUs(models.Model):

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(default=998)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name



class Rate(models.Model):
    NUMBER_RATES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    rate = models.IntegerField(choices=NUMBER_RATES, default=0)


    def __self__(self):
        return self.user.username
