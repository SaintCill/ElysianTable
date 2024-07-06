from django.contrib import admin
from .models import Booking, Contact

# Register your models here.

admin.site.register(Booking)
admin.site.register(Contact)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name',  'message', 'created_at')
    search_fields = ('name', 'email', 'message')
