from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from django.conf import settings


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    bio = models.TextField(max_length=200)
    phone_number = models.CharField(max_length=19)
    approved = models.BooleanField(default=False)
    date =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bio



VOL = [
    ("VOL 1", "Volume 1"),
    ("VOL 2", "Volume 2"),
    ("VOL 3", "Volume 3"),
    ("VOL 4", "Volume 4"),
]


def get_default_author():
    # Replace 2 with the id of the default author you want to use
    return Author.objects.get(id=2)

class JournalModel(models.Model):
    author  = models.ForeignKey(Author, default=get_default_author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    volume = models.CharField(max_length=50, choices=VOL, default="No volume")
    description = models.TextField(default="no description given by author")
    file = models.FileField(upload_to='documents/')
    date_published = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0)
    cover_image = models.ImageField(upload_to='images/', default='traderimg6.jpg')
    payment_proof = models.ImageField(upload_to='images/', default='traderimg6.jpg')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Title: {self.title} Author: {self.author}"


