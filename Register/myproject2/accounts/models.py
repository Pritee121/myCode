from django.db import models

class Signup(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=128, default='defaultpassword')  # Provide a default value
    gender = models.CharField(max_length=10)
