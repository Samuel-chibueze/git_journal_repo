from django.contrib import admin
from .models import journel_model,Publisher_model,PublishingHouse,Authors

# Register your models here.
admin.site.register(journel_model)
admin.site.register(Publisher_model)
admin.site.register(PublishingHouse)
admin.site.register(Authors)
