from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Section)
admin.site.register(Box)
admin.site.register(SectionKind)
