from django.contrib import admin

# Register your models here.

from .models import Batter, Pitcher

admin.site.register(Batter)
admin.site.register(Pitcher)