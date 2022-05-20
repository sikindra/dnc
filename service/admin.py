from django.contrib import admin
from service.models import Service
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'service_des', 'service_image')

admin.site.register(Service,ServiceAdmin)
# Register your models here.
