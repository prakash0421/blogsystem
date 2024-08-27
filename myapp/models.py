# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from storages.backends.s3boto3 import S3Boto3Storage

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    ]

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='patient')
    profile_picture = models.ImageField(null=True, blank=True, storage=S3Boto3Storage(), upload_to='profile_pictures/')
    address_line1 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    pincode = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.username

class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('Mental Health', 'Mental Health'),
        ('Heart Disease', 'Heart Disease'),
        ('Covid19', 'Covid19'),
        ('Immunization', 'Immunization'),
    ]

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_post_images/', storage=S3Boto3Storage())
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    summary = models.TextField()
    content = models.TextField()
    draft = models.BooleanField(default=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
