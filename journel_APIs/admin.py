from django.contrib import admin
from .models import Author,JournalModel
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Author)
admin.site.register(JournalModel)




