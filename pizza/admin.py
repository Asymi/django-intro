from django.contrib import admin

# Register your models here.
from .models import Pizza
from .models import Base

admin.site.register(Pizza)
admin.site.register(Base)
