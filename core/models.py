from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ]

    name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    description = models.TextField()
    image = models.ImageField(upload_to='rooms/', null=True, blank=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        days = (self.check_out - self.check_in).days
        self.total_price = days * self.room.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.room.name}"


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(FoodItem)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        total = sum(item.price for item in self.items.all())
        self.total_price = total
        super().save(*args, **kwargs)


class TableReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guests = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"
