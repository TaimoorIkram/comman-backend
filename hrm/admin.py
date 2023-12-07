from django.contrib import admin
from .models import Member, Rank

# Register your models here.
admin.site.register(Rank)
admin.site.register(Member)