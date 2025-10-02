from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone



# Create your models here.
from django.contrib.auth.models import User

class signup(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.username

class Car(models.Model):
    brand=models.CharField(max_length=100)
    model_name=models.CharField(max_length=100)
    car_name=models.CharField(max_length=100)
    description=models.TextField()  
    current_price=models.FloatField()
    available_city=models.CharField(max_length=100)
    year=models.IntegerField()
    CAR_TYPES = (
        ('SEDAN','Sedan'),
        ('SUV','SUV'),
        ('HATCH','Hatchback'),
        ('CONVERTIBLE','Convertible'),
        ('VAN','Van'),
        ('TRUCK','Truck'),
    )
    car_type = models.CharField(max_length=20, choices=CAR_TYPES, default='SEDAN')
    image=models.ImageField(upload_to='car_images/')
    isavailable=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return f"{self.car_name} - {self.model_name} ({self.year})"


class Rental(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)

    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

    pickup_location = models.CharField(max_length=200, default='Unknown')
    dropoff_location = models.CharField(max_length=200, default='Unknown')

    price_per_day = models.FloatField(default=0.0)
    total_price = models.FloatField(default=0.0)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    payment_method = models.CharField(max_length=50, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)  # optional, for admin ordering
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.user.username} - {self.car.brand} {self.car.model_name}"
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True, blank=True)

    address = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.user.username} Profile"

class Promocode(models.Model):
    code= models.CharField(max_length=16,unique=True)
    discount_per=models.PositiveIntegerField(help_text="discount %")
    active=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} - {self.discount_per}%"
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    pickup_date = models.DateField()
    return_date = models.DateField()
    location = models.CharField(max_length=255)
    days = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.car.car_name} ({self.created_at.strftime('%Y-%m-%d')})"
class CarouselImage(models.Model):
    title = models.CharField(max_length=100)
    image= models.ImageField(upload_to='carousel_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else f"Carousel Image {self.id}"