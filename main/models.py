from django.db import models

# Create your models here.
class Guest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Travel(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    start_date = models.DateField()
    return_date = models.DateField()
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.guest.name} - {self.start_date} to {self.return_date}"
