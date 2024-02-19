from django.db import models

class Publisher_model(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    age = models.CharField(max_length=20)
    address = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=40)
    bio = models.TextField(max_length=200)
    profile_photo = models.ImageField()

    def __str__(self):
        return self.full_name


class Authors(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    age = models.FloatField(max_length=150)
    bio = models.TextField(max_length=200)
    phone_number = models.CharField(max_length=19)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name


class PublishingHouse(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=50)


    def __str__(self):
        return self.name

class journel_model(models.Model):
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0)
    ranking = models.FloatField()
    Publisher = models.ForeignKey(Publisher_model, on_delete=models.CASCADE)
    Publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    