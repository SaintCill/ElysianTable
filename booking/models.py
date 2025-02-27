from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Reservation for {self.name} on {self.date} at {self.time} '
    

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name}, {self.message}"