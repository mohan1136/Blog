from django.contrib import admin
from users.models import Profile
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(Profile)
