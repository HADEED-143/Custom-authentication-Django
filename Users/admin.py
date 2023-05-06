from django.contrib import admin
from . models import User, Employer, Laborer, Contractor

# Register your models here.
admin.site.register(User)
admin.site.register(Employer)
admin.site.register(Laborer)
admin.site.register(Contractor)