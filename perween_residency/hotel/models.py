from django.db import models

class Booking(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    room_type = models.CharField(max_length=100)

    guests = models.IntegerField()

    check_in = models.DateField()

    check_out = models.DateField()

    def __str__(self):
        return self.name


class Contact(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    def __str__(self):
        return self.name

class Customer(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name